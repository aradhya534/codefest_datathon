# 🎥 Demo Video Script (3–5 Minutes) • SLIIT Codefest Datathon 2026
## Team Name: CodeWave • Project: Urban Flow Analytics

> **Format:** 3 to 5 Minutes • Unlisted YouTube Video  
> **Presenter Roles:** Team CodeWave (1 or multiple presenters)  
> **Visuals:** Slides / Screen-recording of Notebooks, Streamlit App (`app.py`), GIS Map, and BI Dashboard.

---

### ⏱️ Timeline & Presentation Flow

#### [0:00 – 0:45] Intro & Problem Statement (The Urban Challenge)
* **Visual:** Slide 1 showing Title, Team CodeWave, and NYC traffic congestion imagery.
* **Spoken Script:**
  > *"Greetings judges! We are Team CodeWave, and welcome to our presentation for the SLIIT Codefest Datathon 2026. 
  > New York City's taxi network moves millions of passengers daily, but it faces major operational bottlenecks: unpredictable metered fares causing booking cancellations, inefficient fleet allocation leading to 34% idle cruising miles, and severe rush-hour corridor congestion. 
  > To solve this, we engineered Urban Flow Analytics — a high-performance big-data platform combining Apache Spark, extreme gradient boosting, 72-hour continuous demand forecasting, interactive executive dashboards, and an AI Mobility Copilot."*

---

#### [0:45 – 1:30] Distributed Data Engineering & PySpark Pipeline (Member 1)
* **Visual:** Screen-record `EDA_taxi_data.ipynb` in Colab / local notebook showing 48,601,782 row count, left zone joins, and the 6 anomaly filters.
* **Spoken Script:**
  > *"Rather than relying merely on a small sample, our team tackled 100% of the competition dataset. 
  > Using Apache Spark and PySpark on an 8GB cluster, we ingested all 12 monthly CSV files totaling 48,601,782 records. 
  > We implemented left outer joins with zone metadata, and applied a rigorous 6-point quantitative anomaly filter. We flagged negative fares, zero-distance trips with positive meter charges, invalid passenger counts, time inversions, and physical speed outliers over 80 mph. 
  > After conditional airport rate imputation, we retained 34.2 million high-fidelity clean records, partitioned into chronological 70% Train, 15% Validation, and 15% Test Parquet files with zero temporal leakage."*

---

#### [1:30 – 2:30] Predictive Modeling: Upfront Pricing & ETA Estimators (Member 2)
* **Visual:** Show `Member2_PredictiveModeling.ipynb` regression tables, SHAP feature importance plots, and `predict.py` in terminal or Streamlit UI.
* **Spoken Script:**
  > *"Next, we tackled guaranteed upfront pricing and on-time arrival. 
  > Using only pre-trip features to ensure practical real-time execution, our XGBoost champion model achieved an extraordinary R² of 96.86% and a Mean Absolute Error of just ±$1.73 on unseen test data. This outperforms linear baselines by nearly 10% R²!
  > For our dynamic trip duration ETA engine, XGBoost reached an R² of 87.15% with an MAE of ±3.10 minutes, leveraging historical corridor speed priors across over 5,200 origin-destination pairs. 
  > Our SHAP explainability confirms that distance, airport flat rates, and corridor congestion priors drive accurate, transparent quotes for riders."*

---

#### [2:30 – 3:30] Spatio-Temporal Demand Forecaster & Hotspot GIS (Member 3)
* **Visual:** Switch to `hotspots_map.html` (Folium dark map with pulsing cluster hubs) and 72-hour demand forecast graphs.
* **Spoken Script:**
  > *"To empower fleet dispatchers, Member 3 developed our 72-Hour Continuous Demand Forecaster. 
  > Using an autoregressive LightGBM architecture with 24-hour and 168-hour seasonal lags, we achieved an R² of 94.68% and reduced prediction error by over 79% compared to traditional Holt-Winters exponential smoothing. 
  > Complementing this, our unsupervised K-Means model (k=6, Silhouette score 0.45) classified the 263 NYC zones into distinct mobility clusters: from Manhattan commuter arteries to Airport super-hubs and outer-borough residential zones, beautifully visualized in our interactive Folium GIS map."*

---

#### [3:30 – 4:30] Live Interactive Demonstrations: Streamlit Platform & Executive Dashboard
* **Visual:** Screen-record `streamlit run app.py` demonstrating:
  1. Real-time Fare & ETA calculation (e.g. JFK to Times Square).
  2. Tab 2: Hotspot Map.
  3. Tab 3: 72h Forecast curves.
  4. Tab 4: AI Mobility Assistant answering *"What is the peak travel hour in Manhattan?"*.
  5. Open `dashboard.html` showing the executive ROI simulator.
* **Spoken Script:**
  > *"We translated our machine learning models into full enterprise applications. 
  > Here is our live Streamlit platform. When an operator selects a corridor — say, JFK Airport to Times Square — our API returns a guaranteed upfront fare quote and minute-level ETA in under 15 milliseconds. 
  > Under Track 5, our AI Mobility Assistant allows city officials to query fleet data in plain English without writing a single line of SQL or Python.
  > Furthermore, under Track 6, our Executive BI Dashboard tells a complete data story with an interactive ROI Simulator demonstrating over $3.2M in annual profit recovery through predictive pre-dispatching."*

---

#### [4:30 – 5:00] Conclusion & Submission Compliance
* **Visual:** Final slide showing GitHub repository link, package zip structure, and Team CodeWave member details.
* **Spoken Script:**
  > *"In summary, Team CodeWave has delivered a complete, reproducible, and production-ready solution: 48.6 million records processed via PySpark, 96.86% pricing accuracy, 72-hour dispatching, and full interactive dashboards. 
  > All notebooks, models, and scripts are packaged strictly in accordance with Datathon guidelines. Thank you for your time, and we look forward to the judges' interview!"*

---

### 💡 Tips for Recording the Video
1. **Tool:** Use **OBS Studio**, **Camo**, or **Zoom Screen Recording** at 1080p.
2. **Audio:** Ensure clear audio using a good headset/microphone.
3. **Upload:** Upload to YouTube as **Unlisted** (anyone with the link can view; not publicly searchable).
4. **Link:** Paste the unlisted YouTube link in your final contest submission portal / form.
