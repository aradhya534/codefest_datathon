<<<<<<< HEAD
# 🎬 SLIIT Codefest Datathon 2026 — Official Demo Video Script
## Project: Urban Flow Analytics | Team: CodeWave
**Target Duration:** 3:30 – 4:30 Minutes  
**Format:** Screen Recording with Voiceover Narration

---

## 📋 Pre-Demo Setup Checklist (Do This Before Recording)
1. **Terminal 1:** Run Streamlit app:
   ```bash
   cd "c:\Users\EL GHANDOUR\Desktop\SUSL\COMPETITIONS\Datathon\codefest_datathon"
   streamlit run app.py
   ```
   Open `http://localhost:8501` in Fullscreen (Press `F11` in Chrome/Edge).
2. **Browser Tab 2:** Have `dashboard.html` open in another tab.
3. **Browser Tab 3:** Have `hotspots_map.html` open in another tab.
4. **Resolution:** Recommended 1080p (1920x1080) at 60fps with clear audio.

---

## ⏱️ Video Breakdown & Narration Script

### 🕒 [0:00 – 0:35] Scene 1: Executive Introduction & The Core Problem
* **On Screen:** Start on the top of the Streamlit App (`http://localhost:8501`). Point out the **CodeWave AI Hero Banner** and the **5 Top KPI Cards** (34.2M Clean Rides, $950.8M Revenue, 96.86% Fare R², 87.15% ETA R², 94.68% Demand Forecast).
* **Narration (What to say):**
  > "Judges and evaluators, welcome to **Urban Flow Analytics**, developed by **Team CodeWave** for the SLIIT Codefest Datathon 2026.
  > 
  > Urban mobility platforms face three existential operational challenges:
  > First, passengers suffer from post-trip fare shock and inaccurate arrival estimations.
  > Second, fleet operators waste millions in deadhead cruising miles due to blind dispatching.
  > And third, massive sensor telemetries contain severe data noise.
  > 
  > To solve this, CodeWave built an end-to-end intelligence platform processing over 48.6 million NYC taxi trips across 265 zones, powered by high-performance supervised learning, 72-hour autoregressive forecasting, and an AI mobility copilot."

---

### 🕒 [0:35 – 1:25] Scene 2: Tab 1 — Guaranteed Upfront Pricing & ETA Simulator
* **On Screen:** Click on **Tab 1: Instant Pricing & ETA Simulator**.
  1. In the sidebar or Route dropdown, select **"✈️ JFK Airport ➔ Times Square"** (16.5 miles, toll $6.94).
  2. Select Departure Time Window: **"🌆 Evening Rush Hour (18:00)"**.
  3. Click **"🚀 Re-Calculate Guaranteed Price & ETA"**.
  4. Highlight the **Upfront Fare Lock Card** ($70+ range), the **Estimated Trip Duration**, and expand the **Itemized TLC Breakdown**.
* **Narration (What to say):**
  > "In Tab 1, we demonstrate our **No-Surprises Upfront Pricing Engine**.
  > 
  > Unlike legacy meters that calculate fares after arrival, our engine locks in a legally guaranteed quote before vehicle dispatch with an outstanding **96.86% R² and an MAE of just $1.73**, powered by XGBoost.
  > 
  > Simultaneously, our **Dynamic ETA Estimator** predicts travel duration at **87.15% R²**. It dynamically captures cyclical time features and empirical corridor prior speeds across 5,284 zone pairs.
  > 
  > Here, an evening rush-hour trip from JFK to Midtown automatically adjusts for corridor congestion, calculates driver net payout at 78%, and provides passengers with transparent itemized TLC pricing with zero surge surprises at drop-off."

---

### 🕒 [1:25 – 2:10] Scene 3: Tab 2 — Geospatial Hotspots & Zone Clustering
* **On Screen:** Click on **Tab 2: Geospatial Hotspots & Zones**.
  1. Scroll slightly to show the interactive **Folium Map of NYC Taxi Zones** with color-coded clusters.
  2. Use the **Filter Map by Cluster Persona** multiselect to isolate *Cluster 2 (Commercial/Midtown)* and *Cluster 1 (Nightlife Hubs)*.
  3. Under Zone Analytics, pick a zone like **"Midtown Center"** or **"JFK Airport"** to show annual pickups, mean fare, and cluster identity.
* **Narration (What to say):**
  > "Moving to Tab 2: Understanding urban flow requires geospatial intelligence. We deployed **unsupervised K-Means clustering (k = 6)** across 265 TLC taxi zones, achieving an optimal silhouette score.
  > 
  > Our model automatically separates distinct urban personas:
  > - Cluster 2 captures dense Midtown commercial arteries with over 80% daytime commuter density.
  > - Cluster 1 isolates nightlife corridors like East Village and Williamsburg, where nighttime rides make up over 54% of volume and generate significantly higher gratuities.
  > - Cluster 3 isolates airport transfers with high average ticket values.
  > 
  > Dispatchers can inspect any zone's velocity and demand profiles in real time."

---

### 🕒 [2:10 – 3:00] Scene 4: Tab 3 — 72-Hour Fleet Demand Forecaster
* **On Screen:** Click on **Tab 3: Fleet Dispatcher (72h Forecast)**.
  1. Hover over the **Interactive 72-Hour Demand Plotly Curve**, showing the white line (Actual Demand), blue line (LightGBM forecast), and red dashed line (Holt-Winters baseline).
  2. Scroll down to the **Dispatch & Prepositioning Console**. Move the **Dispatch Hour slider** from 08:00 (Morning Rush) to 18:00 (Evening Rush) to 23:00 (Nightlife).
  3. Show how the **Borough Allocation Donut Chart** and the **Operational Directive** update dynamically.
* **Narration (What to say):**
  > "In Tab 3, we introduce our predictive flagship: **The Fleet Demand Dispatcher**.
  > 
  > Traditional time-series models like ARIMA or Holt-Winters degrade quickly over multi-day horizons. We trained an **autoregressive LightGBM time-series forecaster** that predicts demand up to 72 hours in advance with **94.68% R²**, delivering an **80% error reduction** over traditional baselines.
  > 
  > Below, our interactive dispatch console translates this curve into direct operational actions. When we switch from morning commute to evening rush hour, the system directs 68% of available vehicles to Midtown outbound corridors. At night, it redirects fleets to entertainment clusters—slashing customer wait times from 6.4 minutes to just 2.1 minutes."

---

### 🕒 [3:00 – 3:45] Scene 5: Tab 4 — AI Mobility Copilot
* **On Screen:** Click on **Tab 4: CodeWave AI Mobility Copilot**.
  1. Click the first prompt button: **"💵 Fare & ETA from JFK to Times Square (2 riders)"**.
  2. Watch the copilot answer in natural language with verified model figures.
  3. Click prompt 2: **"📍 Where should drivers position right now?"**.
  4. Type a quick question in the chat bar: `How much is a ride from LGA to Financial District over 11 miles?` and press Enter.
* **Narration (What to say):**
  > "In Tab 4, we empower both dispatchers and passengers with the **CodeWave AI Mobility Copilot**.
  > 
  > The copilot parses natural language queries, extracts entities like pickup landmarks, drop-off points, mileage, and rider counts, and interfaces directly with our trained inference models.
  > 
  > Whether asking for an instant upfront quote or strategic advice on driver prepositioning, the copilot provides immediate, mathematically verified answers without needing manual dashboard filtering."

---

### 🕒 [3:45 – 4:20] Scene 6: Tab 5 & Business Dashboards — ROI & Executive BI
* **On Screen:** Click on **Tab 5: Executive BI & ROI Calculator**.
  1. Show the **Borough Diurnal Profile** chart and the **8 Anomaly Classes Filtered** chart.
  2. Adjust the **Deadheading Reduction Slider** in the Enterprise ROI box (e.g. set to 18% or 20%).
  3. Highlight the calculated **Annual Fuel Savings ($ millions)** and **Carbon Avoided (MT CO₂)**.
  4. (Optional quick 5-second switch to `dashboard.html` tab): Show the executive Chart.js KPIs.
* **Narration (What to say):**
  > "Finally, in Tab 5, we translate machine learning into boardroom-level financial impact.
  > 
  > First, our data cleaning audit shows how Member 1 methodologically scrubbed 8 distinct anomaly classes, safeguarding revenue calculations.
  > 
  > Second, our Enterprise ROI Simulator demonstrates that by cutting deadhead cruising miles by just 18% across a 4,500-vehicle fleet, operators save over **$3.6 million in fuel annually**, eliminate thousands of metric tons of CO₂, and increase driver net income.
  > 
  > Together with our standalone Executive Dashboard, CodeWave delivers a complete, production-ready urban intelligence platform."

---

### 🕒 [4:20 – 4:35] Scene 7: Conclusion & Wrap-up
* **On Screen:** Return to the top of the Streamlit app showing the CodeWave AI header.
* **Narration (What to say):**
  > "From distributed big data hygiene to 96.8% upfront fare locks, 72-hour predictive dispatching, and conversational AI, CodeWave demonstrates how modern data science transforms urban mobility.
  > 
  > Thank you for your time, and we look forward to your questions!"
=======
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
>>>>>>> cb5b4028f1f1188a748dce6ff2ddf07a213a053b
