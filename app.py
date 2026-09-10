"""
Urban Flow Analytics — Interactive Management & Dispatch Web Application
Built with Streamlit for SLIIT Codefest Datathon 2026
Run via: streamlit run app.py
"""

import os
import sys
import json
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import streamlit.components.v1 as components

# Ensure imports
sys.path.append(os.path.join(os.path.dirname(__file__), "notebooks"))
from predict import UrbanFlowPredictor
from ai_mobility_assistant import AIMobilityAssistant

# Page Config
st.set_page_config(
    page_title="Urban Flow Analytics | Codefest 2026",
    page_icon="🚕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-title { font-size: 32px; font-weight: 800; color: #38bdf8; margin-bottom: 4px; }
    .sub-title { font-size: 15px; color: #94a3b8; margin-bottom: 24px; }
    .kpi-box { background: #1e293b; border-radius: 10px; padding: 18px; border: 1px solid #334155; }
    .kpi-title { font-size: 13px; color: #94a3b8; font-weight: 600; text-transform: uppercase; }
    .kpi-value { font-size: 26px; font-weight: 800; color: #f8fafc; margin-top: 6px; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] { font-size: 15px; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# Initialize Models
@st.cache_resource
def load_system():
    predictor = UrbanFlowPredictor()
    assistant = AIMobilityAssistant()
    zone_csv = os.path.join(os.path.dirname(__file__), "..", "Urban_Flow_Analytics_Zone_Dataset.csv")
    if not os.path.exists(zone_csv):
        zone_csv = os.path.join(os.path.dirname(__file__), "Urban_Flow_Analytics_Zone_Dataset.csv")
    zones = pd.read_csv(zone_csv) if os.path.exists(zone_csv) else pd.DataFrame()
    return predictor, assistant, zones

predictor, assistant, zones_df = load_system()

# Sidebar
st.sidebar.image("https://img.icons8.com/isometric/100/taxi.png", width=70)
st.sidebar.title("Urban Flow AI")
st.sidebar.caption("Team CodeWave | SLIIT Codefest Datathon 2026")
st.sidebar.markdown("---")
st.sidebar.markdown("### 🏆 Production ML Engines")
st.sidebar.markdown("- **Fare Prediction**: `LightGBM` (R² = **96.20%**, MAE = **$1.88**)")
st.sidebar.markdown("- **Duration ETA**: `XGBoost` (R² = **85.96%**, MAE = **3.19 min**)")
st.sidebar.markdown("- **72h Forecaster**: `LightGBM` (R² = **94.68%**, **80% error cut**)")
st.sidebar.markdown("- **Clustering**: `K-Means` (k = **6**, Silhouette = **0.449**)")
st.sidebar.markdown("---")
st.sidebar.info("💡 Strict pre-trip information boundaries enforced. No data leakage.")

# Header
st.markdown('<div class="main-title">🚕 Urban Flow Analytics — Mobility Intelligence Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">End-to-End Pricing Engine, Dynamic ETA, 72-Hour Demand Dispatcher & AI Assistant</div>', unsafe_allow_html=True)

# Top KPIs
k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown('<div class="kpi-box"><div class="kpi-title">Cleaned Ride Volume</div><div class="kpi-value">497,642</div><div style="color: #4ade80; font-size:12px; margin-top:4px;">↑ 7.84% Anomalies Isolated</div></div>', unsafe_allow_html=True)
with k2:
    st.markdown('<div class="kpi-box"><div class="kpi-title">Gross Fleet Revenue</div><div class="kpi-value">$13.84 M</div><div style="color: #38bdf8; font-size:12px; margin-top:4px;">Avg $27.81 per trip</div></div>', unsafe_allow_html=True)
with k3:
    st.markdown('<div class="kpi-box"><div class="kpi-title">Upfront Pricing Accuracy</div><div class="kpi-value">96.20%</div><div style="color: #4ade80; font-size:12px; margin-top:4px;">LightGBM Champion (MAE ±$1.88)</div></div>', unsafe_allow_html=True)
with k4:
    st.markdown('<div class="kpi-box"><div class="kpi-title">72h Demand Forecast</div><div class="kpi-value">94.68%</div><div style="color: #c084fc; font-size:12px; margin-top:4px;">80% Error Reduction</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🚖 Real-Time Fare & ETA Simulator",
    "📍 Hotspot Clusters & Geospatial Map",
    "📈 Fleet Dispatcher 72h Forecast",
    "🤖 AI Mobility Assistant (NLU)"
])

# ── TAB 1: FARE & ETA SIMULATOR ────────────────────────────
with tab1:
    st.markdown("### ⚡ Guaranteed Upfront Fare & On-Time Arrival Estimator")
    st.markdown("Simulate passenger pricing and minute-level trip arrival before dispatch.")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        # Zone dropdown options
        if not zones_df.empty:
            zone_options = {f"{r['loc_id']}: {r['zone_name']} ({r['borough_name']})": r['loc_id'] for _, r in zones_df.iterrows()}
        else:
            zone_options = {"138: LaGuardia Airport (Queens)": 138, "230: Midtown Center (Manhattan)": 230, "132: JFK Airport (Queens)": 132}
            
        origin_label = st.selectbox("Pickup Location (Origin Zone)", list(zone_options.keys()), index=min(137, len(zone_options)-1))
        dest_label   = st.selectbox("Dropoff Destination", list(zone_options.keys()), index=min(229, len(zone_options)-1))
        
        orig_id = zone_options[origin_label]
        dest_id = zone_options[dest_label]
        
        distance = st.slider("Trip Distance (Miles)", min_value=0.5, max_value=35.0, value=8.5, step=0.5)
        riders = st.number_input("Passenger Count", min_value=1, max_value=6, value=1)
        tolls = st.number_input("Bridge / Tunnel Toll ($)", min_value=0.0, max_value=25.0, value=6.94 if (orig_id in [132, 138] or dest_id in [132, 138]) else 0.0)
        
        if st.button("🚀 Calculate Guaranteed Price & ETA", type="primary", use_container_width=True):
            pred_res = predictor.predict(
                origin_loc_id=orig_id,
                dest_loc_id=dest_id,
                distance_miles=distance,
                rider_count=riders,
                pickup_time=datetime.now(),
                toll_total=tolls
            )
            st.session_state['last_pred'] = pred_res
            
    with col_b:
        if 'last_pred' in st.session_state:
            p = st.session_state['last_pred']
            st.success("✅ Prediction Successfully Generated!")
            
            p_col1, p_col2 = st.columns(2)
            with p_col1:
                st.metric(label="Guaranteed Base Fare", value=f"${p['predicted_base_fare']:.2f}")
            with p_col2:
                st.metric(label="Estimated Trip Time", value=f"{p['predicted_duration_minutes']:.1f} mins")
                
            st.markdown(f"**⏰ Scheduled Departure:** `{p['pickup_time']}`")
            st.markdown(f"**🏁 Expected Arrival:** `{p['estimated_arrival_time']}`")
            st.markdown(f"**⚙️ Serving Model Engines:** `{p['model_fare_engine']}` (Fare) & `{p['model_duration_engine']}` (Duration)")
            
            # Show SHAP Interpretability chart
            shap_img_path = os.path.join(os.path.dirname(__file__), "notebooks", "models", "plots", "shap_fare_summary.png")
            if os.path.exists(shap_img_path):
                st.image(shap_img_path, caption="SHAP Global Feature Attribution — Why this fare was calculated", use_column_width=True)
        else:
            st.info("👈 Select trip details and click 'Calculate' to see upfront price and arrival timestamp.")

# ── TAB 2: HOTSPOT CLUSTERS & MAP ──────────────────────────
with tab2:
    st.markdown("### 📍 Urban Travel Hotspots & Geospatial Clustering ($k=6$)")
    st.markdown("Unsupervised segmentation of 265 taxi zones based on trip volume, revenue, and rush/night patterns.")
    
    hotspots_csv = os.path.join(os.path.dirname(__file__), "notebooks", "spatiotemporal", "zone_hotspot_clusters.csv")
    if os.path.exists(hotspots_csv):
        h_df = pd.read_csv(hotspots_csv)
        
        c_filter = st.multiselect("Filter by Operational Cluster:", options=sorted(h_df['cluster'].unique()), default=sorted(h_df['cluster'].unique()))
        filtered_zones = h_df[h_df['cluster'].isin(c_filter)][['loc_id', 'zone_name', 'borough_name', 'cluster', 'total_trips', 'mean_fare', 'rush_ratio', 'night_ratio']]
        
        st.dataframe(
            filtered_zones.sort_values('total_trips', ascending=False).style.format({
                'mean_fare': '${:.2f}',
                'rush_ratio': '{:.1%}',
                'night_ratio': '{:.1%}',
                'total_trips': '{:,.0f}'
            }),
            use_container_width=True,
            height=300
        )
        
    map_file = os.path.join(os.path.dirname(__file__), "hotspots_map.html")
    if os.path.exists(map_file):
        st.markdown("#### 🗺️ Interactive NYC Mobility Cluster Map")
        with open(map_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        components.html(html_content, height=520)

# ── TAB 3: 72H DEMAND FORECAST ─────────────────────────────
with tab3:
    st.markdown("### 📈 The Fleet Dispatcher: 72-Hour Passenger Demand Forecasting")
    st.markdown("Multi-lag Autoregressive LightGBM forecaster delivering an **80% reduction in error** over Holt-Winters.")
    
    forecast_plot = os.path.join(os.path.dirname(__file__), "notebooks", "spatiotemporal", "plots", "demand_forecast_72h.png")
    if os.path.exists(forecast_plot):
        st.image(forecast_plot, caption="Citywide 72-Hour Ahead Passenger Demand Curve (Test Horizon)", use_column_width=True)
        
    st.markdown("""
    #### 💡 Dispatcher Actionable Directives:
    1. **Preposition for Peak 18:00 Rush:** Shift available vehicles to Midtown Center and Financial District between 16:30 and 17:30 to absorb 41,000+ hourly demand.
    2. **Late-Night Entertainment Rotation:** Reposition evening fleets toward Cluster 1 (Lower East Side, East Village, Williamsburg) after 21:00 where night volume reaches 54%.
    3. **Airport Early Morning Queueing:** Ensure Queens airport supply buffers (JFK/LGA) are restocked by 05:30 to capture high-margin inbound flight transfers.
    """)

# ── TAB 4: AI MOBILITY ASSISTANT ───────────────────────────
with tab4:
    st.markdown("### 🤖 The AI Mobility Assistant Agent (Natural Language Dispatcher)")
    st.markdown("Ask operational, pricing, or hotspot questions in plain English.")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I am your AI Mobility Assistant. Ask me anything like *'Estimate fare and ETA from JFK to Times Square for 2 people'* or *'Where are the top demand hotspots?'*"}
        ]
        
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    if prompt := st.chat_input("Ask a question about fares, ETA, hotspots, or demand..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        res = assistant.answer_query(prompt)
        bot_reply = res["answer"]
        
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        with st.chat_message("assistant"):
            st.markdown(bot_reply)
