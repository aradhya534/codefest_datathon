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
| **Sub-minimum/Negative Base Fare** | $\text{base\_fare} < \$2.50$ | Removed | 9,995 | 1.999% |
| **Extreme Outlier Fare** | $\text{base\_fare} > \$250.00$ | Filtered | 149 | 0.030% |
| **Zero Distance with Nonzero Fare** | $\text{dist} \le 0 \land \text{fare} > 0$ | Removed | 6,852 | 1.370% |
| **Zero or Negative Riders** | $\text{rider\_count} \le 0$ | Removed | 3,614 | 0.723% |
| **Voided / Non-revenue Trips** | $\text{method} \in \{3, 4, 6\}$ | Removed | 8,597 | 1.719% |
| **Extreme Physical Speed** | $\text{speed} > 85\text{ mph} \lor < 1\text{ mph}$ | Filtered | 616 | 0.123% |
| **Excessive Duration** | $t_{\text{duration}} > 180\text{ min}$ (3h) | Filtered | 45 | 0.009% |
| **Total Cleaned Sample** | — | — | **460,649 clean rows** | **7.87% removed** |

---

## 4. Modeling Architecture & Model Selection

Three distinct inductive learning paradigms were benchmarked:
1. **Linear Regression (Baseline with Median Imputation & Z-score Scaling):** Serves as an interpretable parametric baseline.
2. **XGBoost (eXtreme Gradient Boosting with Histogram-based tree binning):** Optimized for depth-wise feature interaction and robust variance reduction.
3. **LightGBM (Light Gradient Boosting Machine):** Employs leaf-wise tree growth with depth limits for superior convergence and gradient-based sampling.

### Data Partitioning Strategy
- **Training Set:** 70% (322,453 records)
- **Validation Set:** 15% (69,098 records)
- **Out-of-Sample Test Set:** 15% (69,098 records)
- Fixed deterministic random seed (`SEED = 42`).

---

## 5. Empirical Performance & Benchmark Comparison

### 5.1 Task 2.1 — Base Fare Prediction ($)

| Model Architecture | Val RMSE (\$) | Val MAE (\$) | Val $R^2$ | Test RMSE (\$) | Test MAE (\$) | Test $R^2$ |
|---|---|---|---|---|---|---|
| **Linear Regression (Baseline)** | 6.715 | 3.351 | 0.8717 | 6.615 | 3.321 | 0.8725 |
| **LightGBM** | 3.361 | 1.753 | 0.9679 | 3.309 | 1.757 | 0.9681 |
| **XGBoost (Winner 🏆)** | **3.347** | **1.730** | **0.9681** | **$3.283** | **$1.727** | **0.9686** |

- **Test $R^2$ Score:** **96.86%** of total fare variance explained!
- **Mean Absolute Error (MAE):** **\$1.73** (on average, fare estimates are accurate within \$1.73).
- **5-Fold Cross-Validation RMSE:** $\$3.4762 \pm 0.0812$.

---

### 5.2 Task 2.2 — Trip Duration Prediction (Minutes)

| Model Architecture | Val RMSE (min) | Val MAE (min) | Val $R^2$ | Test RMSE (min) | Test MAE (min) | Test $R^2$ |
|---|---|---|---|---|---|---|
| **Linear Regression (Baseline)** | 7.065 | 4.416 | 0.7611 | 7.204 | 4.428 | 0.7529 |
| **LightGBM** | 5.215 | 3.135 | 0.8698 | 5.266 | 3.158 | 0.8680 |
| **XGBoost (Winner 🏆)** | **5.152** | **3.073** | **0.8729** | **5.196 min** | **3.096 min** | **0.8715** |

- **Test $R^2$ Score:** **87.15%** of trip duration variance explained!
- **Mean Absolute Error (MAE):** **3.10 minutes** (ETA is accurate down to ~3 minutes).
- **5-Fold Cross-Validation RMSE:** $5.5334 \pm 0.0512\text{ min}$.

---

## 6. Rationale for Evaluation Metric Selection

As mandated by the evaluation rubrics, metric selection was governed by domain operational considerations:

1. **Root Mean Squared Error (RMSE) — Primary Optimization Metric:**
   - *Mathematical formulation:* $\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$
   - *Domain justification:* In passenger transportation, outlier errors (e.g., predicting an arrival time off by 25 minutes or a fare miscalculated by $30) cause catastrophic customer dissatisfaction and chargebacks. Because RMSE penalizes large residuals quadratically, models optimized on RMSE avoid severe over- or under-estimations.
2. **Mean Absolute Error (MAE) — Operational Interpretability:**
   - *Mathematical formulation:* $\text{MAE} = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$
   - *Domain justification:* MAE provides direct real-world meaning for stakeholders and marketing: "On average, upfront base fares are within $\pm \$1.73$ of the true meter value, and trip ETA is accurate within $\pm 3.10$ minutes."
3. **Coefficient of Determination ($R^2$ Score) — Relative Variance Explained:**
   - *Mathematical formulation:* $R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$
   - *Domain justification:* Demonstrates that gradient boosting models account for over **87.15% of trip duration variability** and **96.86% of fare variance**, thoroughly outperforming standard linear approximations.

---

## 7. Feature Importance & Operational Insights

Key drivers identified via Gini impurity / gain importance:
1. **Trip Distance (`distance_miles`)**: Accounts for >68% of total split gain for fares and >55% for duration.
2. **Corridor Historical Speed Prior (`od_speed_prior` & `expected_travel_time_min`)**: Ingests route-specific traffic bottlenecks without data leakage, significantly lifting duration $R^2$.
3. **Rate Class ID (`rate_class_id`) & Airport Indicators**: Fixed rates for airport transfers (JFK Flat Rate, Newark surcharge) significantly perturb linear relationships.
4. **Diurnal Time Features (`sin_hour`, `cos_hour`, `is_rush_hour`)**: Exhibit massive impact on duration prediction due to peak-period arterial bottlenecks.

---

## 8. Exported Deliverables Summary

- **Fare Model:** `fare_model_xgboost.pkl` ($R^2 = 0.9686$) & `fare_model_lightgbm.pkl` ($R^2 = 0.9681$)
- **Duration Model:** `duration_model_xgboost.pkl` ($R^2 = 0.8715$)
- **Corridor Speed Priors:** `corridor_speed_priors.json`
- **Model Metadata & Manifest:** `model_metadata.json`
- **Reproducible Inference Engine:** `predict.py`
- **Data Partitions:** `fare_train.csv`, `fare_val.csv`, `fare_test.csv`, `duration_train.csv`, `duration_val.csv`, `duration_test.csv`
