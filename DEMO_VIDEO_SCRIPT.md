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
