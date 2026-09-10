# Section: Supervised Predictive Modeling & Estimation (Member 2)

## 1. Problem Formulation & Operational Objectives

In modern urban ride services, static pricing and heuristic travel estimations lead to customer friction and operational inefficiency. This module addresses two core supervised learning challenges under strict **pre-trip information constraints** (no post-trip telemetry such as actual speed or elapsed time is permitted during inference):

1. **Task 2.1 — Upfront Base Fare Prediction ("No-Surprises Upfront Pricing Engine"):**
   - **Target:** `base_fare` (metered base fare before optional gratuities and tolls).
   - **Objective:** Compute guaranteed upfront fares prior to vehicle dispatch to establish price transparency and rider trust.
2. **Task 2.2 — On-Time Arrival Estimator ("Dynamic ETA Engine"):**
   - **Target:** `trip_duration_min` (Total elapsed trip time in minutes, computed as $(t_{\text{dropoff}} - t_{\text{pickup}}) / 60$).
   - **Objective:** Deliver minute-level arrival accuracy accounting for congestion, time-of-day traffic, and spatial constraints.

---

## 2. Feature Engineering & Pre-Trip Representation

All features are strictly engineered using signals available **prior to departure**:

| Feature Category | Features | Rationale |
|---|---|---|
| **Trip Physics & Topology** | `distance_miles`, `origin_loc_id`, `dest_loc_id`, `inter_borough` | Captures baseline transit distance and cross-borough boundary penalties. |
| **Temporal & Cyclicality** | `pickup_hour`, `pickup_dayofweek`, `pickup_month`, `is_weekend`, `is_rush_hour`, `is_night` | Encodes diurnal congestion cycles (morning/evening rush hours) and weekend demand shifts. |
| **Spatial Classifications** | `pickup_borough_enc`, `dropoff_borough_enc`, `pickup_service_zone_enc`, `dropoff_service_zone_enc` | Ingests macro-level TLC zone characteristics joined from `Urban_Flow_Analytics_Zone_Dataset.csv`. |
| **Special Transit Modifiers** | `is_airport_pickup`, `is_airport_dropoff`, `rate_class_id`, `rider_count`, `toll_total` | Captures airport transit surcharges (JFK: 132, LGA: 138, EWR: 1), fixed rate classes, and predictable bridge/tunnel toll paths. |

---

## 3. Data Cleaning & Anomaly Quantification

Data hygiene was executed systematically with full empirical quantification across ~500,000 sampled trips:

| Anomaly Type | Condition | Action Taken | Records Impacted | % Impact |
|---|---|---|---|---|
| **Temporal Inversion / Zero Duration** | $t_{\text{duration}} \le 0$ | Removed | 9,475 | 1.895% |
| **Negative Fare Values** | $\text{base\_fare} < 0$ | Removed | 9,530 | 1.906% |
| **Zero Distance with Nonzero Fare** | $\text{dist} = 0 \land \text{fare} > 0$ | Removed | 7,187 | 1.437% |
| **Zero or Negative Riders** | $\text{rider\_count} \le 0$ | Removed | 3,758 | 0.752% |
| **Voided / Non-revenue Trips** | $\text{method} \in \{3, 6\}$ | Removed | 3,958 | 0.792% |
| **Extreme Physical Speed** | $\text{speed} > 120\text{ mph} \lor \text{NaN}$ | Filtered | 115 | 0.023% |
| **Outlier Duration** | $t_{\text{duration}} > 300\text{ min}$ (5h) | Filtered | 214 | 0.043% |
| **Total Cleaned Sample** | — | — | **466,344 clean rows** | **6.73% removed** |

---

## 4. Modeling Architecture & Model Selection

Three distinct inductive learning paradigms were benchmarked:
1. **Linear Regression (ElasticNet/OLS with Median Imputation & Z-score Scaling):** Serves as an interpretable parametric baseline.
2. **XGBoost (eXtreme Gradient Boosting with Histogram-based tree binning):** Optimized for depth-wise feature interaction and high variance reduction.
3. **LightGBM (Light Gradient Boosting Machine):** Employs leaf-wise tree growth for faster convergence and gradient-based one-side sampling.

### Data Partitioning Strategy
- **Training Set:** 70% (326,440 records)
- **Validation Set:** 15% (69,952 records)
- **Out-of-Sample Test Set:** 15% (69,952 records)
- Fixed deterministic random seed (`SEED = 42`).

---

## 5. Empirical Performance & Benchmark Comparison

### 5.1 Task 2.1 — Base Fare Prediction ($)

| Model Architecture | Val RMSE (\$) | Val MAE (\$) | Val $R^2$ | Test RMSE (\$) | Test MAE (\$) | Test $R^2$ |
|---|---|---|---|---|---|---|
| **Linear Regression (Baseline)** | 12.989 | 5.336 | 0.6202 | 13.313 | 5.330 | 0.6102 |
| **XGBoost** | 10.463 | 3.067 | 0.7536 | 10.487 | 3.098 | 0.7581 |
| **LightGBM (Winner)** | **9.811** | **3.079** | **0.7834** | **10.110** | **3.101** | **0.7752** |
| **Tuned LightGBM** | — | — | — | **$10.091** | **$3.097** | **0.7760** |

- **5-Fold Cross-Validation RMSE:** $\$9.9455 \pm 0.4580$
- **Optimal Hyperparameters:** `learning_rate=0.03`, `max_depth=7`, `n_estimators=400`

---

### 5.2 Task 2.2 — Trip Duration Prediction (Minutes)

| Model Architecture | Val RMSE (min) | Val MAE (min) | Val $R^2$ | Test RMSE (min) | Test MAE (min) | Test $R^2$ |
|---|---|---|---|---|---|---|
| **Linear Regression (Baseline)** | 7.994 | 5.251 | 0.6843 | 8.192 | 5.251 | 0.6795 |
| **LightGBM** | 5.842 | 3.407 | 0.8315 | 6.074 | 3.392 | 0.8238 |
| **XGBoost (Winner)** | **5.689** | **3.288** | **0.8401** | **5.930** | **3.267** | **0.8320** |
| **Tuned XGBoost** | — | — | — | **5.791 min** | **3.132 min** | **0.8398** |

- **5-Fold Cross-Validation RMSE:** $5.5590 \pm 0.0807\text{ min}$
- **Optimal Hyperparameters:** `learning_rate=0.05`, `max_depth=8`, `n_estimators=600`

---

## 6. Rationale for Evaluation Metric Selection

As mandated by the evaluation rubrics, metric selection was governed by domain operational considerations:

1. **Root Mean Squared Error (RMSE) — Primary Optimization Metric:**
   - *Mathematical formulation:* $\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$
   - *Domain justification:* In passenger transportation, outlier errors (e.g., predicting an arrival time off by 25 minutes or a fare miscalculated by $30) cause catastrophic customer dissatisfaction and chargebacks. Because RMSE penalizes large residuals quadratically, models optimized on RMSE avoid severe over- or under-estimations.
2. **Mean Absolute Error (MAE) — Operational Interpretability:**
   - *Mathematical formulation:* $\text{MAE} = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$
   - *Domain justification:* MAE provides direct real-world meaning for stakeholders and marketing: "On average, upfront base fares are within $\pm \$3.09$ of the true meter value, and trip ETA is accurate within $\pm 3.13$ minutes."
3. **Coefficient of Determination ($R^2$ Score) — Relative Variance Explained:**
   - *Mathematical formulation:* $R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$
   - *Domain justification:* Demonstrates that gradient boosting models account for over **84% of trip duration variability** and **77.6% of fare variance**, thoroughly outperforming standard linear approximations.

---

## 7. Feature Importance & Operational Insights

Key drivers identified via Gini impurity / gain importance:
1. **Trip Distance (`distance_miles`)**: Accounts for >68% of total split gain across both models, representing the primary physical cost driver.
2. **Rate Class ID (`rate_class_id`) & Airport Indicators**: Fixed rates for airport transfers (JFK Flat Rate, Newark surcharge) significantly perturb linear relationships.
3. **Diurnal Time Features (`pickup_hour`, `is_rush_hour`)**: Exhibit massive impact on duration prediction due to peak-period arterial bottlenecks.
4. **Origin & Destination Zone Locality**: Reflects dense urban grid speeds (Manhattan) versus expressway speeds (Queens / Brooklyn connectors).

---

## 8. Exported Deliverables Summary

- **Fare Model:** `fare_model_lightgbm.pkl` (1.0 MB)
- **Duration Model:** `duration_model_xgboost.pkl` (8.6 MB)
- **Model Metadata & Manifest:** `model_metadata.json`
- **Reproducible Inference Engine:** `predict.py`
- **Data Partitions:** `fare_train.csv`, `fare_val.csv`, `fare_test.csv`, `duration_train.csv`, `duration_val.csv`, `duration_test.csv`
