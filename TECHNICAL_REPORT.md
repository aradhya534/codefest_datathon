# 🚕 Urban Flow Analytics — Official Technical Report
## SLIIT Codefest Datathon 2026 | Team CodeWave

---

### Executive Summary
Urban Flow Analytics is an end-to-end urban mobility intelligence and automated dispatching platform built for large-scale metropolitan taxi fleets. Leveraging over 48.6 million NYC Taxi and Limousine Commission (TLC) trip telemetry records across 265 urban zones, the platform delivers:
1. **Guaranteed Upfront Pricing Engine**: Gradient-boosted fare estimation achieving **$R^2 = 96.86\%$** and an MAE of **$1.73**.
2. **Dynamic Arrival Estimator (ETA)**: Minute-level travel duration predictions with **$R^2 = 87.15\%$** and MAE of **3.10 minutes**.
3. **72-Hour Fleet Demand Forecaster**: Multi-horizon autoregressive time series forecaster achieving **$R^2 = 94.68\%$** (an 80% error reduction over traditional Holt-Winters baselines).
4. **Spatial Hotspot Clustering**: Unsupervised K-Means clustering ($k = 6$) identifying commuter arteries, nightlife hubs, and airport transfer pipelines.
5. **AI Mobility Copilot**: A natural language agent providing real-time pricing and fleet management guidance.

---

### Section 1: Data Engineering & Anomaly Detection (Member 1)
- **Scale:** 48,601,782 raw telemetry records ingested across 12 monthly periods.
- **Data Quality & Scrubbing:** Systematic removal of 8 distinct anomaly classes:
  1. *Temporal Inversion ($\Delta t \le 0$):* Drop-off preceding pickup (984k rows, 2.025%).
  2. *Negative or Sub-minimum Base Fare ($< \$2.50$):* Chargebacks and system logging faults (1.01M rows, 2.083%).
  3. *Extreme Outlier Fares ($> \$250$):* Out-of-state charters (14.8k rows, 0.031%).
  4. *Zero-Distance Trips with Positive Fare:* Idle wait fees without spatial displacement (692k rows, 1.424%).
  5. *Invalid Passenger Count ($\le 0$):* Pressure sensor dropouts (415k rows, 0.854%).
  6. *Non-Revenue / Disputed Trips (Codes 3, 4, 6):* Disputes and voided transactions (895k rows, 1.842%).
  7. *Physical Speed Outliers ($> 80\text{ mph}$ or $< 1\text{ mph}$):* GPS calculation errors and traffic stalls (354k rows, 0.729%).
  8. *Excessive Duration ($> 180\text{ min}$):* Unclosed meter sessions (18.2k rows, 0.038%).
- **Clean Retention:** 34,204,452 verified valid trips (70.38% retention).

---

### Section 2: Supervised Predictive Modeling (Member 2)
#### 2.1 Upfront Base Fare Prediction
- **Target:** `base_fare`
- **Features:** Distance, passenger count, rate class, origin/destination zone encodings, cyclical temporal signals ($\sin/\cos$ of hour and day of week), airport indicators, and corridor prior speed baselines.
- **Model Comparison:**
  - *Linear Regression Baseline:* $R^2 = 0.8725$, $\text{RMSE} = 6.61$, $\text{MAE} = \$3.32$
  - *LightGBM Regressor:* $R^2 = 0.9681$, $\text{RMSE} = 3.31$, $\text{MAE} = \$1.76$
  - *XGBoost Regressor (Champion):* $R^2 = 0.9686$, $\text{RMSE} = 3.28$, $\text{MAE} = \$1.73$

#### 2.2 Dynamic Trip Duration (ETA) Prediction
- **Target:** `trip_duration_min`
- **Model Comparison:**
  - *Linear Regression Baseline:* $R^2 = 0.7529$, $\text{MAE} = 4.43\text{ min}$
  - *LightGBM Regressor:* $R^2 = 0.8680$, $\text{MAE} = 3.16\text{ min}$
  - *XGBoost Regressor (Champion):* $R^2 = 0.8715$, $\text{MAE} = 3.10\text{ min}$

---

### Section 3: Spatial-Temporal Forecasting & AI Copilot (Member 3)
#### 3.1 72-Hour Ahead Demand Dispatching
- **Horizon:** 72 consecutive hours evaluated against holdout test series.
- **Baseline (Holt-Winters):** $R^2 = 73.4\%$, $\text{RMSE} = 412.5$
- **Autoregressive LightGBM Forecaster:** $R^2 = 94.68\%$, $\text{RMSE} = 81.2$ (**80.3% error reduction**).

#### 3.2 Geospatial Hotspot Clustering ($k = 6$)
- Cluster 0: Residential outer-borough arterials.
- Cluster 1: Nightlife and dining hubs (54% night volume, highest average tips).
- Cluster 2: Commercial & Midtown arteries (intense daytime commuter volume).
- Cluster 3: Airport transfer corridors (JFK/LGA high-ticket trips).
- Cluster 4: Suburban outer feeders.
- Cluster 5: Peripheral transit feeders.

---

### Section 4: Operational Economics & Enterprise ROI
- **Deadhead Cruising Reduction:** $18\%$ targeted reduction through proactive vehicle prepositioning.
- **Annual Fleet Fuel Savings:** Projected **\$3.6M+ USD** across a 4,500-vehicle fleet.
- **Carbon Emission Abatement:** Over **$14,200\text{ MT of CO}_2$** avoided per year.
- **Driver Income Gain:** Over **\$4.8M USD** in converted paid passenger miles.
