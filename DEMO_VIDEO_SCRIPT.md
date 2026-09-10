# 🎬 3–5 Minute YouTube Demo Video Presentation Script
## SLIIT Codefest Datathon 2026 — Urban Flow Analytics Data Challenge

> **Target Duration:** 4 minutes (optimal within the 3–5 minute rule)  
> **Format:** Screen recording with voiceover (Slides / Notebook / Dashboard / Terminal)  
> **Upload Setting:** Unlisted YouTube Video  

---

### Timeline & Scene-by-Scene Breakdown

| Timestamp | Scene / Screen Display | Speaker Role | Key Talking Points |
|---|---|---|---|
| **0:00 – 0:45** | Title Slide & Solution Architecture Diagram | Team Lead / Member 1 | Problem statement, 12 months TLC data, end-to-end 3-tier architecture. |
| **0:45 – 1:30** | `notebooks/EDA_taxi_data.ipynb` & Anomaly Chart | Member 1 | 8 systematic anomalies quantified (7.84% removed), diurnal demand heatmap, OD matrix. |
| **1:30 – 2:45** | `notebooks/Member2_PredictiveModeling.ipynb` & Plots | Member 2 | Upfront Fare (LightGBM $R^2=96.2\%$, MAE=\$1.88) & Duration ETA (XGBoost $R^2=86.0\%$, MAE=3.2 min). Metric justifications (RMSE vs MAE). |
| **2:45 – 3:45** | `notebooks/Member3_SpatialTemporal_Demand_AI.ipynb` & Terminal | Member 3 | 72h Fleet Demand Forecaster ($R^2=94.7\%$), K-Means Hotspot clusters ($k=6$), Live AI Mobility Assistant demo. |
| **3:45 – 4:30** | `dashboard.html` & Conclusion | All Members | Management recommendations, deadheading reduction by 22%, submission deliverables summary. |

---

### Full Spoken Voiceover Script

#### [0:00 – 0:45] Scene 1: Introduction & Architecture Overview
**Visual:** Slide 1 showing Team Name: **CodeWave**, Project Title, and the Mermaid Solution Architecture Diagram.  
**Voiceover:**  
> *"Hello judges and welcome to our presentation by team CodeWave for the Urban Flow Analytics Data Challenge at SLIIT Codefest Datathon 2026.*  
> *Urban transit systems generate millions of data points, but raw logs are plagued by sensor failures and extreme traffic variability. To solve this, our team developed a comprehensive three-tier AI architecture: robust data hygiene, high-precision supervised pricing and ETA models, and spatial-temporal demand forecasting with an interactive AI Mobility Assistant.*  
> *Crucially, our architecture enforces a strict pre-trip information boundary, ensuring every customer prediction is leak-free and production-ready."*

---

#### [0:45 – 1:30] Scene 2: Data Quality & Exploratory Analysis (Member 1)
**Visual:** Screen recording of `notebooks/EDA_taxi_data.ipynb`, showing the Anomaly Impact Table and Heatmap.  
**Voiceover:**  
> *"Starting with Data Quality, across 12 months of taxi data, raw logs contained critical corruptions. As seen in our anomaly audit, we systematically identified and justified eight anomaly classes: negative fares, zero-duration trips, speed outliers exceeding 85 miles per hour, and disputed records. In total, 7.84% of corrupted records were isolated.*  
> *Our exploratory analysis reveals strong diurnal rhythm—peaking at 41,000 trips during the 18:00 evening rush hour, with Manhattan driving 74% of urban volume and Queens dominating high-value airport transit flows."*

---

#### [1:30 – 2:45] Scene 3: Predictive Modeling & Upfront Pricing (Member 2)
**Visual:** Screen recording of `notebooks/Member2_PredictiveModeling.ipynb`, zooming in on the Model Comparison Table, Feature Importance, and Residual Plots.  
**Voiceover:**  
> *"Moving to Predictive Modeling, our first task was the 'No-Surprises Upfront Pricing Engine'. Benchmarking OLS Linear Regression against XGBoost and LightGBM on an out-of-sample test set, our tuned LightGBM model emerged as the champion, explaining an outstanding 96.20% of fare variance with an RMSE of just $3.58 and an average error of only $1.87.*  
> *For the 'On-Time Arrival Estimator', urban congestion demands non-linear modeling. Our tuned XGBoost model achieved an R-squared of 85.96%, predicting trip duration down to plus-or-minus 3.19 minutes.*  
> *We selected RMSE as our primary optimization metric to quadratically penalize extreme estimation errors, safeguarding passenger trust, while MAE provides intuitive dollar and minute interpretations for operations."*

---

#### [2:45 – 3:45] Scene 4: Spatial-Temporal Forecasting & AI Mobility Assistant (Member 3)
**Visual:** Screen recording of `Member3_SpatialTemporal_Demand_AI.ipynb` showing the 72-hour forecast curve, followed by opening terminal running `python notebooks/ai_mobility_assistant.py`.  
**Voiceover:**  
> *"For Task 3, 'The Fleet Dispatcher', fleet efficiency depends on anticipating ride demand. We built a multi-lag autoregressive LightGBM time-series forecaster spanning an 8,000-hour grid. Forecasting 72 hours out, it achieved an R-squared of 94.68% and an 80% error reduction over the Holt-Winters baseline.*  
> *Simultaneously, unsupervised K-Means clustering with k=6 delineated mega-commercial hubs, nightlife epicenters, and residential feeders.*  
> *To operationalize this, we built the AI Mobility Assistant. As you can see live in the terminal, dispatchers or customers can ask natural English queries—like 'Estimate fare and ETA from JFK to Times Square for 2 passengers'—and our agent translates the query, runs inference, and returns exact upfront figures instantly."*

---

#### [3:45 – 4:30] Scene 5: Executive Dashboard & Strategic Recommendations
**Visual:** Screen recording interacting with `dashboard.html`, hovering over KPIs and charts.  
**Voiceover:**  
> *"Finally, our Executive Dashboard synthesizes these analytics into three high-impact business decisions:  
> First, deploy upfront pricing to eliminate meter anxiety, estimated to lift repeat rides by 14%.  
> Second, use our 72-hour demand forecast to preposition vehicles into high-density clusters, cutting deadheading by 22%.  
> And third, introduce in-app digital tipping prompts to recapture gratuity revenue lost on cash trips.*  
> *All source code notebooks, trained PKL models, split datasets, and our 20-page technical report are fully packaged and reproducible.*  
> *Thank you for your time!"*

---

### Tips for Recording
1. **Screen Resolution:** Record at 1080p (1920x1080) for sharp text clarity.
2. **Audio:** Use a clear microphone and speak at a steady, confident pace.
3. **Pacing:** Practice speaking along with the timestamps to ensure you finish within 4 minutes.
