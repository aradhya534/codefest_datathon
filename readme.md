# 🚕 Urban Flow Analytics — SLIIT Codefest Datathon 2026
### 🏆 Team Name: CodeWave

An end-to-end urban mobility intelligence platform featuring **Guaranteed Upfront Pricing (96.2% R²)**, **Dynamic Arrival Estimations (86.0% R²)**, **72-Hour Demand Dispatching (94.7% R²)**, **Spatial Hotspot Clustering (k=6)**, and an **AI Mobility Assistant**.

---

## 📂 Project Architecture

```
codefest_datathon/
├── TECHNICAL_REPORT.md                        ← Comprehensive 20-Page Technical Report
├── DEMO_VIDEO_SCRIPT.md                       ← 3-5 Minute YouTube Demo Video Script
├── dashboard.html                             ← Executive Business Dashboard (Interactive Chart.js)
├── hotspots_map.html                          ← Geospatial Interactive NYC Mobility Map (Folium)
├── app.py                                     ← Interactive Streamlit Platform (4 Tabs)
├── package_submission.py                      ← 1-Click Packager -> CodeWave_CodefestDatathon2026.zip
│
├── cleaned_data/                              ← Member 1 Data Quality Deliverables
│   ├── urban_flow_cleaned.csv                 ← Master Cleaned Dataset Sample
│   ├── powerbi_kpi_summary.csv                ← Power BI Management Aggregates
│   ├── anomaly_cleaning_audit.csv             ← Quantitative 8-Anomaly Impact Audit
│   └── plots/                                 ← Heatmaps, OD Matrices, Anomaly Bars
│
├── notebooks/
│   ├── CodeWave_FinalNotebook.ipynb           ← [Official Master Notebook] Complete End-to-End Pipeline
│   ├── EDA_taxi_data.ipynb                    ← [Member 1] Data Preprocessing & EDA
│   ├── Member2_PredictiveModeling.ipynb       ← [Member 2] Supervised Fare & Duration ML
│   ├── Member3_SpatialTemporal_Demand_AI.ipynb ← [Member 3] Demand Forecaster & AI Assistant
│   ├── predict.py                             ← Real-time Upfront Fare & Duration Inference API
│   ├── ai_mobility_assistant.py               ← Natural Language AI Mobility Agent
│   │
│   ├── models/                                ← Trained Models & Deliverables
│   │   ├── fare_model_lightgbm.pkl            ← Upfront Base Fare Model (R² = 0.9620)
│   │   ├── duration_model_xgboost.pkl         ← On-Time Arrival Estimator (R² = 0.8596)
│   │   ├── splits/                            ← Clearly Separated Train/Val/Test CSV Splits
│   │   └── plots/                             ← SHAP Attribution, Residuals, Feature Importances
│   │
│   └── spatiotemporal/                        ← Spatial-Temporal Models & Hotspots
│       ├── demand_forecast_lgb.pkl            ← 72h Autoregressive Demand Forecaster (R² = 0.9468)
│       ├── hotspot_kmeans_model.pkl           ← Hotspot Clusters Model (k = 6)
│       ├── zone_hotspot_clusters.csv          ← Labeled Zone Classifications
│       └── plots/                             ← 72h Forecast Curves & Scatter Plots
```

---

## ⚡ Quick Start & Interactive Apps

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch Streamlit Web Platform
```bash
streamlit run app.py
```
*Access the Real-Time Fare & ETA Simulator, Hotspot Map, 72h Demand Curves, and AI Assistant in your browser.*

### 3. Open Executive Business Dashboard
Double-click `dashboard.html` to open the interactive executive management dashboard in any web browser.

### 4. Try the AI Mobility Assistant (CLI)
```bash
python notebooks/ai_mobility_assistant.py
```

### 5. Generate Official Submission ZIP
```bash
python package_submission.py CodeWave
```
*Builds `CodeWave_CodefestDatathon2026.zip` strictly complying with all Datathon formatting and naming rules.*
