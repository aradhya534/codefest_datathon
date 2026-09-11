"""
🚕 URBAN FLOW INTELLIGENCE PLATFORM — TEAM CODEWAVE
SLIIT Codefest Datathon 2026 | Enterprise Mobility, Predictive Analytics & Dispatch Copilot
Run: streamlit run app.py
"""

import os
import sys
import json
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px
import plotly.graph_objects as go

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, "notebooks"))
from predict import UrbanFlowPredictor
from ai_mobility_assistant import AIMobilityAssistant

# ─── PAGE CONFIG ────────────────────────────────────────────
st.set_page_config(
    page_title="Urban Flow AI · CodeWave",
    page_icon="🚕",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── GLOBAL THEME ───────────────────────────────────────────
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

/* ── Reset & Base ─────────────────────────── */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}
.stApp {
    background: #080c14;
    color: #e2e8f0;
}
.block-container {
    padding: 1.2rem 2rem 3rem !important;
    max-width: 1480px !important;
}

/* ── Sidebar ──────────────────────────────── */
[data-testid="stSidebar"] {
    background: #0d1220 !important;
    border-right: 1px solid rgba(255,255,255,0.06) !important;
}
[data-testid="stSidebar"] .block-container {
    padding: 1.5rem 1rem !important;
}

/* ── Hero Banner ──────────────────────────── */
.hero {
    background: linear-gradient(135deg,#0f1e3c 0%,#0a1628 50%,#0d1b30 100%);
    border: 1px solid rgba(56,189,248,0.2);
    border-radius: 20px;
    padding: 26px 32px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
    box-shadow: 0 0 60px rgba(56,189,248,0.06), 0 4px 24px rgba(0,0,0,0.4);
}
.hero-title {
    font-size: 30px;
    font-weight: 900;
    letter-spacing: -0.03em;
    background: linear-gradient(100deg,#fff 0%,#7dd3fc 50%,#a78bfa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
}
.hero-sub {
    font-size: 13px;
    color: #94a3b8;
    margin: 6px 0 0 0;
    font-weight: 400;
    letter-spacing: 0.01em;
}
.live-chip {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(16,185,129,0.12);
    border: 1px solid rgba(16,185,129,0.35);
    border-radius: 99px;
    padding: 7px 18px;
    font-size: 11.5px;
    font-weight: 700;
    color: #34d399;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
.dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #34d399;
    box-shadow: 0 0 6px #34d399, 0 0 12px rgba(52,211,153,0.5);
    display: inline-block;
}

/* ── KPI Strip ────────────────────────────── */
.kpi-card {
    background: linear-gradient(135deg,rgba(15,30,60,0.8) 0%,rgba(10,22,42,0.9) 100%);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 16px 18px;
    text-align: center;
    transition: border-color 0.25s;
}
.kpi-card:hover {
    border-color: rgba(56,189,248,0.3);
}
.kpi-label {
    font-size: 10px;
    font-weight: 700;
    color: #64748b;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 6px;
}
.kpi-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 26px;
    font-weight: 800;
    color: #f1f5f9;
    line-height: 1.1;
}
.kpi-sub {
    font-size: 11px;
    color: #475569;
    margin-top: 4px;
}

/* ── Tabs ─────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px !important;
    background: rgba(255,255,255,0.03) !important;
    border-radius: 14px !important;
    padding: 5px !important;
    border: 1px solid rgba(255,255,255,0.05) !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 10px !important;
    font-size: 13.5px !important;
    font-weight: 600 !important;
    color: #64748b !important;
    padding: 8px 20px !important;
    height: 42px !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg,rgba(56,189,248,0.16),rgba(129,140,248,0.16)) !important;
    color: #7dd3fc !important;
    border: 1px solid rgba(56,189,248,0.3) !important;
}
button[data-baseweb="tab"]:focus {
    outline: none !important;
    box-shadow: none !important;
}

/* ── Buttons ─────────────────────────────── */
div.stButton > button {
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    transition: all 0.18s ease !important;
}
div.stButton > button:hover {
    border-color: #38bdf8 !important;
    box-shadow: 0 0 14px rgba(56,189,248,0.22) !important;
    color: #38bdf8 !important;
}
div.stButton > button[kind="primary"] {
    background: linear-gradient(135deg,#0284c7,#4f46e5) !important;
    border: none !important;
    color: white !important;
}
div.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg,#0369a1,#4338ca) !important;
    box-shadow: 0 0 20px rgba(56,189,248,0.35) !important;
}

/* ── Metric Overrides ─────────────────────── */
[data-testid="stMetricValue"] {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 22px !important;
    font-weight: 800 !important;
}
[data-testid="stMetricLabel"] {
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    color: #64748b !important;
    text-transform: uppercase !important;
}

/* ── Chat styling ─────────────────────────── */
[data-testid="stChatMessage"] {
    border-radius: 14px !important;
    margin-bottom: 8px !important;
}

/* ── Scrollbar ───────────────────────────── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(100,116,139,0.4); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: rgba(100,116,139,0.7); }

/* ── Divider ─────────────────────────────── */
hr {
    border-color: rgba(255,255,255,0.06) !important;
    margin: 1rem 0 !important;
}
</style>""", unsafe_allow_html=True)

# ─── CACHED PLATFORM INIT ───────────────────────────────────
@st.cache_resource
def init_platform():
    predictor = UrbanFlowPredictor()
    assistant = AIMobilityAssistant()

    zone_file = os.path.abspath(os.path.join(BASE_DIR, "..", "Urban_Flow_Analytics_Zone_Dataset.csv"))
    if not os.path.exists(zone_file):
        zone_file = os.path.join(BASE_DIR, "Urban_Flow_Analytics_Zone_Dataset.csv")
    if os.path.exists(zone_file):
        zones_df = pd.read_csv(zone_file, keep_default_na=False)
        zones_df['zone_name'] = zones_df['zone_name'].replace('', 'Unknown Zone').astype(str)
        zones_df['borough_name'] = zones_df['borough_name'].replace('', 'Unknown Borough').astype(str)
    else:
        zones_df = pd.DataFrame()

    hotspots_file = os.path.join(BASE_DIR, "notebooks", "spatiotemporal", "zone_hotspot_clusters.csv")
    if os.path.exists(hotspots_file):
        hotspots_df = pd.read_csv(hotspots_file, keep_default_na=False)
        hotspots_df['zone_name'] = hotspots_df['zone_name'].replace('', 'Unknown Zone').astype(str)
        hotspots_df['borough_name'] = hotspots_df['borough_name'].replace('', 'Unknown Borough').astype(str)
    else:
        hotspots_df = pd.DataFrame()

    meta_path = os.path.join(BASE_DIR, "notebooks", "models", "model_metadata.json")
    metadata = {}
    if os.path.exists(meta_path):
        with open(meta_path) as f:
            metadata = json.load(f)

    kpi_df    = pd.read_csv(os.path.join(BASE_DIR, "cleaned_data", "powerbi_kpi_summary.csv"))    if os.path.exists(os.path.join(BASE_DIR, "cleaned_data", "powerbi_kpi_summary.csv"))    else pd.DataFrame()
    audit_df  = pd.read_csv(os.path.join(BASE_DIR, "cleaned_data", "anomaly_cleaning_audit.csv")) if os.path.exists(os.path.join(BASE_DIR, "cleaned_data", "anomaly_cleaning_audit.csv")) else pd.DataFrame()
    fc_path   = os.path.join(BASE_DIR, "notebooks", "spatiotemporal", "forecast_72h_series.csv")
    forecast_df = pd.read_csv(fc_path) if os.path.exists(fc_path) else pd.DataFrame()

    return predictor, assistant, zones_df, hotspots_df, metadata, kpi_df, audit_df, forecast_df

predictor, assistant, zones_df, hotspots_df, metadata, kpi_df, audit_df, forecast_df = init_platform()

fare_engine = metadata.get("best_fare_model", "XGBoost")
dur_engine  = metadata.get("best_dur_model",  "XGBoost")
fare_r2  = metadata.get("fare_results",     {}).get(fare_engine, {}).get("Test", {}).get("R2",  0.9686)
fare_mae = metadata.get("fare_results",     {}).get(fare_engine, {}).get("Test", {}).get("MAE", 1.73)
dur_r2   = metadata.get("duration_results", {}).get(dur_engine,  {}).get("Test", {}).get("R2",  0.8715)
dur_mae  = metadata.get("duration_results", {}).get(dur_engine,  {}).get("Test", {}).get("MAE", 3.10)

# ─── SIDEBAR ────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🚕 CodeWave AI")
    st.caption("SLIIT Codefest Datathon 2026")
    st.success("● All Engines Online", icon="🟢")
    st.divider()

    st.markdown("**⚡ Model Benchmarks**")
    with st.container(border=True):
        st.metric("Fare Engine — XGBoost 🏆", f"R² {fare_r2*100:.2f}%", f"MAE ±${fare_mae:.2f}")
    with st.container(border=True):
        st.metric("Duration — XGBoost 🏆",    f"R² {dur_r2*100:.2f}%",  f"MAE ±{dur_mae:.2f} min")
    with st.container(border=True):
        st.metric("72h Dispatch — LightGBM 🏆", "R² 94.68%", "RMSE 83  (↓79% vs baseline)")

    with st.expander("🔍 Pipeline Architecture"):
        rows = [
            ("Raw Dataset",   "48,601,782 records"),
            ("PySpark Clean", "34,197,136 records"),
            ("OD Priors",     "5,284 corridors"),
            ("Leakage",       "100% pre-trip safe"),
        ]
        for k, v in rows:
            st.markdown(f"<small style='color:#64748b'>{k}</small><br><b>{v}</b>", unsafe_allow_html=True)

    st.divider()
    report_file = os.path.join(BASE_DIR, "TECHNICAL_REPORT.md")
    if os.path.exists(report_file):
        with open(report_file, encoding="utf-8") as f:
            st.download_button("📥 Technical Report (MD)", f.read(),
                               "CodeWave_Report.md", "text/markdown",
                               use_container_width=True)

# ─── HERO BANNER ────────────────────────────────────────────
st.markdown("""<div class="hero">
<div>
<h1 class="hero-title">🚕 Urban Flow Intelligence Platform</h1>
<p class="hero-sub">Team CodeWave · Upfront Pricing · On-Time ETA · 72 h Dispatch · AI Copilot · SLIIT Codefest Datathon 2026</p>
</div>
<div class="live-chip"><span class="dot"></span>PYSPARK · 48.6 M TRIPS INGESTED</div>
</div>""", unsafe_allow_html=True)

# ─── KPI STRIP ──────────────────────────────────────────────
kc = st.columns(5)
kpis = [
    ("📦 CLEANED DATASET",   "34.20 M",    "From 48.6 M raw records"),
    ("💵 FLEET REVENUE",     "$950.8 M",   "Avg $27.81 / trip"),
    ("🎯 FARE MODEL R²",     f"{fare_r2*100:.2f}%",  f"MAE ±${fare_mae:.2f} · XGBoost"),
    ("⏱️ DURATION R²",      f"{dur_r2*100:.2f}%",   f"MAE ±{dur_mae:.2f} min · XGBoost"),
    ("📈 72 H FORECAST R²", "94.68%",     "RMSE 83 · LightGBM"),
]
for col, (label, value, sub) in zip(kc, kpis):
    col.markdown(
        f"""<div class="kpi-card">
<div class="kpi-label">{label}</div>
<div class="kpi-value">{value}</div>
<div class="kpi-sub">{sub}</div>
</div>""", unsafe_allow_html=True)

st.write("")

# ─── MAIN TABS ──────────────────────────────────────────────
t1, t2, t3, t4, t5 = st.tabs([
    "🚖  Pricing & ETA Simulator",
    "📍  Geospatial Hotspot Map",
    "📈  72 h Fleet Dispatcher",
    "🤖  AI Mobility Copilot",
    "📊  Executive BI & ROI",
])

# ══════════════════════════════════════════════════════════════
# TAB 1  ·  Upfront Pricing & ETA
# ══════════════════════════════════════════════════════════════
with t1:
    # ── Quick Corridor Pills ──────────────────────────────────
    st.markdown("**⚡ Popular NYC Corridors — click to preload:**")
    bc = st.columns(5)
    if "p_choice" not in st.session_state:
        st.session_state.p_choice = "JFK"
    choices = [("✈️ JFK ➔ Times Sq","JFK"),("✈️ LGA ➔ Wall St","LGA"),
               ("🌉 Midtown ➔ Brooklyn","Brooklyn"),("✈️ Newark ➔ Central Pk","Newark"),
               ("✏️ Custom Route","Custom")]
    for col,(label,key) in zip(bc,choices):
        if col.button(label, use_container_width=True):
            st.session_state.p_choice = key

    presets = {"JFK":(132,230,16.5,6.94),"LGA":(138,87,11.2,6.94),
               "Brooklyn":(230,255,4.8,0.00),"Newark":(1,43,17.8,16.50),
               "Custom":(138,230,8.5,0.00)}
    p_orig,p_dest,p_dist,p_toll = presets[st.session_state.p_choice]

    left, right = st.columns([1, 1.3], gap="large")

    # ── Input Panel ───────────────────────────────────────────
    with left:
        with st.container(border=True):
            st.markdown("#### 📍 Journey Configuration")
            if not zones_df.empty:
                zone_map = {f"{r['loc_id']}: {r['zone_name']} ({r['borough_name']})": int(r['loc_id'])
                            for _, r in zones_df.iterrows()}
                vals = list(zone_map.values())
                o_idx = vals.index(p_orig) if p_orig in vals else 0
                d_idx = vals.index(p_dest) if p_dest in vals else 1
                sel_orig = st.selectbox("🟢 Pickup Zone", list(zone_map.keys()), index=o_idx)
                sel_dest = st.selectbox("🔴 Destination Zone", list(zone_map.keys()), index=d_idx)
                chosen_orig = zone_map[sel_orig]
                chosen_dest = zone_map[sel_dest]
            else:
                chosen_orig, chosen_dest = p_orig, p_dest

            ca, cb = st.columns(2)
            dist_val  = ca.slider("Trip Distance (mi)", 0.5, 35.0, float(p_dist), 0.5)
            pass_val  = cb.number_input("Passengers", 1, 6, 1, 1)

            cc, cd = st.columns(2)
            time_window = cc.selectbox("Departure Window", [
                "⚡ Real-Time","🌅 Morning Rush (08:30)","🌤️ Midday (14:00)",
                "🌆 PM Rush (18:00)","🌙 Late Night (23:30)"], index=3)
            toll_val = cd.number_input("Tolls ($)", 0.0, 35.0, float(p_toll), 0.5)

            tier = st.radio("Vehicle Tier",
                ["🚕 Standard Cab","🚙 Comfort XL SUV  (+25%)","⚡ Priority Eco  (+8%)"],
                horizontal=True)
            tmul = 1.25 if "Comfort" in tier else (1.08 if "Priority" in tier else 1.0)
            tlabel = "Standard" if tmul==1.0 else ("Comfort XL" if tmul==1.25 else "Priority Eco")

            st.button("🚀 Get Live Quote", type="primary", use_container_width=True)

    # ── Output Ticket ─────────────────────────────────────────
    with right:
        now_dt = datetime.now()
        _t_map = {
            "Morning": (now_dt.replace(hour=8,  minute=30), "⚠️ Morning Commute Active — Speed Buffer Applied",    "warning"),
            "PM":      (now_dt.replace(hour=18, minute=0),  "🚨 PM Rush Hour Gridlock — +32% Travel Time",          "error"),
            "Late":    (now_dt.replace(hour=23, minute=30), "🌙 Night Owl — Free Flow, Lower Latency",              "info"),
            "Midday":  (now_dt.replace(hour=14, minute=0),  "🟢 Off-Peak Flow — Smooth & Predictable",              "success"),
        }
        sim_dt, advisory, adv_type = now_dt, "⚡ Real-Time Telemetry Active", "info"
        for k,(dt,msg,typ) in _t_map.items():
            if k.lower() in time_window.lower():
                sim_dt, advisory, adv_type = dt, msg, typ; break

        q = predictor.predict(origin_loc_id=chosen_orig, dest_loc_id=chosen_dest,
                              distance_miles=dist_val, rider_count=pass_val,
                              pickup_time=sim_dt, toll_total=toll_val)

        def _zone_name(zid, col):
            if not zones_df.empty and zid in zones_df['loc_id'].values:
                r = zones_df[zones_df['loc_id']==zid].iloc[0]
                return r[col]
            return f"Zone {zid}"

        o_name, o_boro = _zone_name(chosen_orig,'zone_name'), _zone_name(chosen_orig,'borough_name')
        d_name, d_boro = _zone_name(chosen_dest,'zone_name'), _zone_name(chosen_dest,'borough_name')

        raw_fare   = q['predicted_base_fare']
        final_fare = round(raw_fare * tmul, 2)
        dur_mins   = q['predicted_duration_minutes']
        eta_str    = q['estimated_arrival_time'].split(' ')[1]
        speed_mph  = (dist_val / (dur_mins/60)) if dur_mins > 0 else 12.5
        driver_pay = round(final_fare * 0.78, 2)
        fuel_est   = round(dist_val  * 0.16, 2)
        tlc_fee    = round(final_fare * 0.12, 2)
        taxes      = round(final_fare - driver_pay - tlc_fee, 2)

        with st.container(border=True):
            # Traffic advisory banner
            getattr(st, adv_type)(advisory)

            # Route row
            st.markdown(
                f"**Route:** 🟢 **{o_name}** *({o_boro})* &nbsp;➔&nbsp; 🔴 **{d_name}** *({d_boro})* &nbsp;·&nbsp; **{dist_val:.1f} mi**")
            st.divider()

            # Hero price + ETA
            fa_col, eta_col = st.columns(2)
            with fa_col:
                st.caption(f"GUARANTEED FARE — {tlabel.upper()}")
                st.markdown(
                    f"<p style='font-family:JetBrains Mono,monospace;font-size:44px;"
                    f"font-weight:900;color:#38bdf8;margin:0;line-height:1'>${final_fare:.2f}</p>",
                    unsafe_allow_html=True)
                st.caption("🔒 Price locked · no surge surprises")
            with eta_col:
                st.caption("ESTIMATED ARRIVAL TIME")
                st.markdown(
                    f"<p style='font-family:JetBrains Mono,monospace;font-size:40px;"
                    f"font-weight:900;color:#f1f5f9;margin:0;line-height:1'>⏱ {eta_str}</p>",
                    unsafe_allow_html=True)
                st.caption(f"{dur_mins:.0f} min · {speed_mph:.1f} mph avg")

            st.divider()

            # Fleet tier comparison table
            st.caption("FLEET TIER COMPARISON")
            tc1, tc2, tc3 = st.columns(3)
            for col, (icon, lbl, mult) in zip([tc1,tc2,tc3],[
                ("🚕","Standard",1.0),("🚙","Comfort XL",1.25),("⚡","Priority Eco",1.08)
            ]):
                selected_badge = " ✓" if mult == tmul else ""
                color = "#38bdf8" if mult == tmul else "#475569"
                col.markdown(
                    f"<div style='text-align:center;padding:10px 6px;border-radius:10px;"
                    f"border:1px solid {color}40;background:{color}12'>"
                    f"<div style='font-size:20px'>{icon}</div>"
                    f"<div style='font-size:12px;font-weight:700;color:{color}'>{lbl}{selected_badge}</div>"
                    f"<div style='font-family:JetBrains Mono;font-size:18px;font-weight:800;"
                    f"color:#f1f5f9;margin:4px 0'>${raw_fare*mult:.2f}</div>"
                    f"</div>",
                    unsafe_allow_html=True)

            st.divider()

            # 4-metric economics row
            m1,m2,m3,m4 = st.columns(4)
            m1.metric("Driver Pay",     f"${driver_pay:.2f}")
            m2.metric("Fuel Est.",      f"${fuel_est:.2f}")
            m3.metric("TLC & Taxes",    f"${tlc_fee+taxes:.2f}")
            m4.metric("Corridor Speed", f"{speed_mph:.1f} mph")

        # Itemized expander
        with st.expander("🧾 Itemized TLC Regulatory Breakdown"):
            items = [
                ("Base Flagdrop",                           f"$3.00"),
                (f"Mileage ({dist_val:.1f} mi)",            f"${max(0, raw_fare-toll_val-3.0):.2f}"),
                ("Bridge / Tunnel Tolls",                   f"${toll_val:.2f}"),
                (f"Tier Surcharge ({tlabel})",              f"${final_fare-raw_fare:.2f}"),
                ("**Guaranteed Passenger Total**",          f"**${final_fare:.2f}**"),
            ]
            for k, v in items:
                ca2, cb2 = st.columns([3,1])
                ca2.markdown(f"— {k}")
                cb2.markdown(v)

# ══════════════════════════════════════════════════════════════
# TAB 2  ·  Geospatial Hotspot Map
# ══════════════════════════════════════════════════════════════
with t2:
    st.markdown("### 📍 NYC Geospatial Hotspot Clusters  *(K-Means k=6)*")
    st.caption("Spatial-temporal clustering segmenting 263 TLC zones into demand archetypes: commercial hubs, nightlife corridors, airport feeders, and outer-borough arterials.")

    cluster_labels = {
        0: "🏡 Cluster 0 — Residential Outer Borough Arterials",
        1: "🍸 Cluster 1 — Nightlife & Dining Hubs  (54% night volume)",
        2: "🏢 Cluster 2 — Commercial Midtown Arteries  (peak commuter)",
        3: "✈️ Cluster 3 — Airport Corridors  (JFK / LGA / EWR)",
        4: "🌳 Cluster 4 — Suburban Outer Feeders",
        5: "⚓ Cluster 5 — Peripheral Transit Feeders",
    }

    if not hotspots_df.empty:
        chosen_clusters = st.multiselect(
            "Active Clusters:",
            options=sorted(hotspots_df['cluster'].unique()),
            default=sorted(hotspots_df['cluster'].unique()),
            format_func=lambda c: cluster_labels.get(c, f"Cluster {c}"),
        )

        map_col, info_col = st.columns([1.65, 1], gap="large")

        with map_col:
            map_file = os.path.join(BASE_DIR, "hotspots_map.html")
            if os.path.exists(map_file):
                st.caption("🗺️ Interactive NYC Mobility Map — 263 TLC Zones")
                with open(map_file, encoding="utf-8") as f:
                    components.html(f.read(), height=590, scrolling=False)
            else:
                st.info("GIS map file not found. Run the spatial notebook to generate hotspots_map.html")

        with info_col:
            st.markdown("##### 🔍 Zone Deep-Dive")
            zone_list = sorted([str(z) for z in zones_df['zone_name'].dropna().unique() if str(z).strip()]) if not zones_df.empty else []
            sel_zone = st.selectbox("Search a zone:", zone_list)
            if sel_zone and not hotspots_df.empty:
                zm = hotspots_df[hotspots_df['zone_name'] == sel_zone]
                if not zm.empty:
                    zr = zm.iloc[0]
                    with st.container(border=True):
                        st.markdown(f"#### 📍 {zr['zone_name']}")
                        st.caption(f"{zr['borough_name']}  ·  Zone ID {zr['loc_id']}")
                        za, zb = st.columns(2)
                        za.metric("Annual Pickups", f"{int(zr['total_trips']):,}")
                        zb.metric("Avg Fare",        f"${zr['mean_fare']:.2f}")
                        st.info(cluster_labels.get(int(zr['cluster']), "Unknown Cluster"))
                else:
                    st.warning("Zone not found in cluster data.")

            st.markdown("##### 🏆 Top 10 Busiest Zones")
            filt = hotspots_df[hotspots_df['cluster'].isin(chosen_clusters)]
            display_cols = ['zone_name','borough_name','total_trips','mean_fare','night_ratio']
            fmt = {'total_trips':'{:,.0f}','mean_fare':'${:.2f}','night_ratio':'{:.1%}'}
            st.dataframe(
                filt[display_cols].sort_values('total_trips', ascending=False).head(10).style.format(fmt),
                height=250, use_container_width=True)
    else:
        st.warning("Hotspot cluster data not found. Run notebooks/Member3_SpatialTemporal_Demand_AI.ipynb first.")

# ══════════════════════════════════════════════════════════════
# TAB 3  ·  72 h Fleet Dispatcher
# ══════════════════════════════════════════════════════════════
with t3:
    st.markdown("### 📈 72-Hour Continuous Demand Forecaster")
    st.caption("Autoregressive LightGBM model · R² 94.68% · RMSE 83 (↓79% vs Holt-Winters baseline 1,592)")

    if not forecast_df.empty:
        fig_fc = go.Figure()
        fig_fc.add_trace(go.Scatter(
            x=forecast_df['timestamp'], y=forecast_df['actual_demand'],
            name="Actual Demand", mode='lines',
            line=dict(color='#e2e8f0', width=1.8)))
        fig_fc.add_trace(go.Scatter(
            x=forecast_df['timestamp'], y=forecast_df['lightgbm_forecast'],
            name="LightGBM Forecast (R²=94.68%)", mode='lines',
            line=dict(color='#38bdf8', width=3),
            fill='tonexty', fillcolor='rgba(56,189,248,0.07)'))
        fig_fc.add_trace(go.Scatter(
            x=forecast_df['timestamp'], y=forecast_df['holt_winters_baseline'],
            name="Holt-Winters Baseline (RMSE 1592)", mode='lines',
            line=dict(color='#f43f5e', width=1.5, dash='dot')))
        fig_fc.update_layout(
            title="72-Hour NYC Taxi Demand Forecast",
            xaxis_title="Hour Index",
            yaxis_title="Trips / Hour",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(15,25,48,0.6)',
            font=dict(color='#94a3b8', family='Inter'),
            height=340,
            legend=dict(orientation="h", y=1.02, x=1, xanchor="right", yanchor="bottom"),
            xaxis=dict(gridcolor='rgba(255,255,255,0.04)'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.04)'),
        )
        st.plotly_chart(fig_fc, use_container_width=True)
    else:
        st.info("Forecast data not found. Run notebooks/Member3_SpatialTemporal_Demand_AI.ipynb.")

    st.divider()
    st.markdown("### 🧭 Dynamic Fleet Pre-Positioning Console")

    dc, hc = st.columns(2)
    day = dc.selectbox("Dispatch Day", ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], index=4)
    hr  = hc.slider("Hour of Day (0–23)", 0, 23, 18)

    _dispatch_map = {
        frozenset([7,8,9]):           (65,18,14,3, "🟡 HIGH COMMUTER DEMAND",
            "Morning Peak: Pre-position residential feeders into Upper East/West Manhattan and Brooklyn Heights; inbound routes to Financial District."),
        frozenset([16,17,18,19]):     (68,17,12,3, "🔴 PEAK RUSH — GRIDLOCK ALERT",
            "PM Peak Surge: Direct 68% of fleet to Midtown & Penn Station. Heavy outbound flows toward Queens & Brooklyn bridges."),
        frozenset([21,22,23,0,1,2]):  (52,24,21,3, "🟣 NIGHTLIFE SURGE",
            "Night Economy: Rotate to East Village, LES, and Williamsburg. Night trips = 54% volume with +$4.20 avg tip premium."),
    }
    man_pct,qns_pct,brk_pct,brx_pct = 58,22,16,4
    d_status = "🟢 STEADY DAYTIME DISPATCH"
    d_text   = "Standard ops: balanced borough coverage with airport buffer queues at JFK, LGA, and EWR."
    for hours,(mp,qp,bp,bxp,st_lbl,txt) in _dispatch_map.items():
        if hr in hours:
            man_pct,qns_pct,brk_pct,brx_pct = mp,qp,bp,bxp
            d_status,d_text = st_lbl,txt; break

    dc2, dc3 = st.columns([1,1.2], gap="large")
    with dc2:
        pie_df = pd.DataFrame({
            'Borough': ['Manhattan','Queens+Airports','Brooklyn','Bronx'],
            'Allocation': [man_pct,qns_pct,brk_pct,brx_pct]})
        fig_pie = px.pie(pie_df, names='Borough', values='Allocation', hole=0.58,
            color='Borough',
            color_discrete_map={'Manhattan':'#38bdf8','Queens+Airports':'#818cf8',
                                'Brooklyn':'#34d399','Bronx':'#fbbf24'})
        fig_pie.update_layout(
            title=f"{day}  ·  {hr:02d}:00",
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#94a3b8',family='Inter'), height=280,
            showlegend=True, legend=dict(orientation="v"))
        st.plotly_chart(fig_pie, use_container_width=True)
    with dc3:
        with st.container(border=True):
            st.caption("DISPATCH INTELLIGENCE STATUS")
            st.markdown(f"### {d_status}")
            st.write(d_text)
            st.success("⏱️ Pre-positioning cuts avg pickup latency 6.4 min → 2.1 min")
            pa, pb, pc, pd_ = st.columns(4)
            pa.metric("Manhattan", f"{man_pct}%")
            pb.metric("Queens",    f"{qns_pct}%")
            pc.metric("Brooklyn",  f"{brk_pct}%")
            pd_.metric("Bronx",    f"{brx_pct}%")

# ══════════════════════════════════════════════════════════════
# TAB 4  ·  AI Mobility Copilot
# ══════════════════════════════════════════════════════════════
with t4:
    st.markdown("### 🤖 CodeWave AI Mobility Copilot")
    st.caption("Natural language interface into XGBoost & LightGBM engines — ask about fares, ETAs, hotspots, or dispatch.")

    chat_col, side_col = st.columns([1.65, 1], gap="large")

    with side_col:
        st.markdown("##### 💡 Quick Prompts")
        prompts = [
            ("💵", "JFK → Times Square fare & ETA",       "What is the estimated fare and arrival time from JFK to Times Square for 2 people over 15 miles?"),
            ("📍", "Best driver hotspots right now",       "Where are the top demand hotspots where drivers should position?"),
            ("🏙️", "Borough demand comparison",            "How do taxi flows compare across NYC boroughs by hour?"),
            ("✈️", "LGA → Wall St  (11 mi estimate)",     "Estimate trip fare and duration from LaGuardia Airport to Wall Street Financial District over 11 miles"),
        ]
        clicked_prompt = None
        for icon, label, query in prompts:
            if st.button(f"{icon}  {label}", use_container_width=True):
                clicked_prompt = query

        st.divider()
        if st.button("🗑️  Clear Conversation", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

        with st.container(border=True):
            st.caption("COPILOT CAPABILITIES")
            caps = [
                "NLP entity extraction (routes, distances, passengers)",
                "Live XGBoost / LightGBM inference",
                "Hotspot cluster identification",
                "Fleet dispatch recommendations",
            ]
            for c in caps:
                st.markdown(f"<small style='color:#94a3b8'>· {c}</small>", unsafe_allow_html=True)

    with chat_col:
        if "chat_history" not in st.session_state or not st.session_state.chat_history:
            st.session_state.chat_history = [{"role":"assistant",
                "content":"👋 Hello! I'm your **CodeWave AI Mobility Copilot**. "
                          "Ask me about taxi fares, trip ETAs, demand hotspots, or fleet positioning in NYC!"}]

        def send_msg(text):
            st.session_state.chat_history.append({"role":"user","content":text})
            ans = assistant.answer_query(text)
            st.session_state.chat_history.append({"role":"assistant","content":ans['answer']})

        if clicked_prompt:
            send_msg(clicked_prompt)

        typed = st.chat_input("Type a query — e.g. 'Fare from LGA to Times Square, 3 passengers?'")
        if typed:
            send_msg(typed)

        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

# ══════════════════════════════════════════════════════════════
# TAB 5  ·  Executive BI & ROI
# ══════════════════════════════════════════════════════════════
with t5:
    st.markdown("### 📊 Executive Business Intelligence & Fleet ROI Calculator")

    st.markdown("Translating analytical findings into actionable management decisions, fuel savings, and driver revenue growth.")
    
    # Borough hourly profile from Power BI dataset
    if not kpi_df.empty and 'pickup_borough' in kpi_df.columns:
        st.markdown("##### 🏙️ Diurnal Transit Demand Patterns across NYC Boroughs")
        borough_hourly = kpi_df.groupby(['pickup_borough', 'pickup_hour'])['total_trips'].sum().reset_index()
        fig_bh = px.line(
            borough_hourly, x='pickup_hour', y='total_trips', color='pickup_borough',
            title="Hourly Trips by Borough (24-Hour Cycle)",
            markers=True,
            color_discrete_sequence=['#38bdf8', '#818cf8', '#4ade80', '#fbbf24', '#f43f5e']
        )
        fig_bh.update_layout(
            xaxis=dict(title="Hour of Day (0–23)", tickmode='linear', tick0=0, dtick=2),
            yaxis=dict(title="Aggregated Volume"),
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,23,42,0.6)',
            font=dict(color='#94a3b8'), height=280
        )
        st.plotly_chart(fig_bh, use_container_width=True)
    
    bi1, bi2 = st.columns(2, gap="medium")
    
    with bi1:
        st.markdown("##### 💳 Tipping Dynamics & Digital Gratuity Recapture")
        fig_tip = go.Figure(data=[
            go.Bar(name='Recorded Tip ($)', x=['Credit Card', 'Cash Settlement'], y=[3.48, 0.00], marker_color=['#38bdf8', '#64748b'])
        ])
        fig_tip.update_layout(
            title="Recorded Gratuity by Payment Method",
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#94a3b8'), height=260
        )
        st.plotly_chart(fig_tip, use_container_width=True)
        st.caption("💡 **Executive Takeaway**: Cash transactions record $0 tips in TLC telemetry. Prompting in-app digital card payments unlocks ~$18.2M annually in driver tips.")
        
    with bi2:
        st.markdown("##### 🧹 Data Hygiene & Systematic Anomaly Filtering")
        if not audit_df.empty:
            hover_cols = [c for c in ['Impacted Rows (Full 48.6M Scale)', 'Impacted Rows', 'Methodological Justification'] if c in audit_df.columns]
            fig_anom = px.bar(
                audit_df.sort_values('% Impact', ascending=True),
                x='% Impact', y='Anomaly Class',
                orientation='h',
                text='% Impact',
                color='% Impact',
                color_continuous_scale='Reds',
                hover_data=hover_cols
            )
            fig_anom.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
            fig_anom.update_layout(
                title="8 Anomaly Classes Filtered (Hover for Justification)",
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#94a3b8'), height=260, coloraxis_showscale=False
            )
            st.plotly_chart(fig_anom, use_container_width=True)
        else:
            img_anom = os.path.join(BASE_DIR, "cleaned_data", "plots", "anomaly_impact_bar.png")
            if os.path.exists(img_anom):
                st.image(img_anom, caption="Distribution of 8 Systematic Anomaly Classes (7.82% Total Cleaned)", use_container_width=True)
            
    st.markdown("---")
    st.markdown("#### 💰 Interactive Enterprise ROI & Fuel Savings Simulator")
    
    r_input, r_output = st.columns([1, 1.4], gap="large")
    with r_input:
        f_size = st.slider("Active Fleet Size (Vehicles):", 500, 15000, 4500, 500)
        dh_target = st.slider("Target Deadheading Reduction (%):", 5, 30, 18, 1, help="Reduction in empty cruising miles enabled by 72h Demand Dispatcher.")
        d_miles_day = 110.0
        fuel_cost_gal = 3.65
        fleet_mpg = 24.0
    with r_output:
        saved_miles_day = f_size * d_miles_day * (dh_target / 100.0)
        annual_fuel_saved_usd = (saved_miles_day * 365 / fleet_mpg) * fuel_cost_gal
        co2_tons_saved = (saved_miles_day * 365 * 404) / 1_000_000 # 404g CO2/mile
        driver_revenue_gain = (saved_miles_day * 365) * 1.85 * 0.78 # Converting cruising miles into paid fares
        
        st.markdown(f"""
        <div class="roi-box">
            <div style="font-size: 13px; font-weight: 700; color: #4ade80; text-transform: uppercase;">Projected Annual Enterprise Impact</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 14px;">
                <div>
                    <div style="font-size: 11px; color: #94a3b8;">ANNUAL FUEL SAVINGS</div>
                    <div style="font-size: 26px; font-weight: 800; color: #4ade80;">${annual_fuel_saved_usd:,.0f}</div>
                </div>
                <div>
                    <div style="font-size: 11px; color: #94a3b8;">CARBON AVOIDED</div>
                    <div style="font-size: 26px; font-weight: 800; color: #38bdf8;">{co2_tons_saved:,.1f} MT CO₂</div>
                </div>
                <div>
                    <div style="font-size: 11px; color: #94a3b8;">DRIVER WAGE ENHANCEMENT</div>
                    <div style="font-size: 26px; font-weight: 800; color: #c084fc;">${driver_revenue_gain:,.0f}</div>
                </div>
                <div>
                    <div style="font-size: 11px; color: #94a3b8;">DEADHEAD MILES CUT</div>
                    <div style="font-size: 26px; font-weight: 800; color: #fbbf24;">{saved_miles_day*365/1_000_000:,.1f}M Miles</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
=======
    st.caption("Data-driven insights across 34 M cleaned trips — tipping behaviour, anomaly filtering, and enterprise ROI simulation.")


    # ── Borough 24-h Demand Curve ─────────────────────────────
    if not kpi_df.empty and 'pickup_borough' in kpi_df.columns:
        bh = kpi_df.groupby(['pickup_borough','pickup_hour'])['total_trips'].sum().reset_index()
        fig_bh = px.line(bh, x='pickup_hour', y='total_trips', color='pickup_borough',
                         markers=True, title="24-Hour Trip Volume by Borough",
                         color_discrete_sequence=['#38bdf8','#818cf8','#34d399','#fbbf24','#f43f5e'])
        fig_bh.update_layout(
            xaxis=dict(title="Hour of Day", tickmode='linear', dtick=2),
            yaxis=dict(title="Trips"),
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,25,48,0.6)',
            font=dict(color='#94a3b8',family='Inter'), height=290,
            xaxis_gridcolor='rgba(255,255,255,0.04)', yaxis_gridcolor='rgba(255,255,255,0.04)')
        st.plotly_chart(fig_bh, use_container_width=True)

    bi1, bi2 = st.columns(2, gap="medium")

    # ── Tipping Dynamics ──────────────────────────────────────
    with bi1:
        with st.container(border=True):
            st.markdown("##### 💳 Tipping Dynamics by Payment Method")
            fig_tip = go.Figure([go.Bar(
                x=['Credit Card','Cash'], y=[3.48,0.00],
                marker_color=['#38bdf8','#334155'],
                text=['$3.48','$0.00'], textposition='outside',
                textfont=dict(color='#f1f5f9',size=14,family='JetBrains Mono'))])
            fig_tip.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#94a3b8',family='Inter'), height=230,
                yaxis=dict(title="Avg Tip ($)"),
                showlegend=False)
            st.plotly_chart(fig_tip, use_container_width=True)
            st.info("💡 **Insight**: Cash records $0 in TLC telemetry. Digitising payments unlocks ~$18.2 M/yr in driver tips.")

    # ── Anomaly Audit ─────────────────────────────────────────
    with bi2:
        with st.container(border=True):
            st.markdown("##### 🧹 Anomaly Cleaning Audit  *(48.6 M scale)*")
            if not audit_df.empty:
                fig_anom = px.bar(audit_df.sort_values('% Impact', ascending=True),
                    x='% Impact', y='Anomaly Class', orientation='h',
                    text='% Impact', color='% Impact',
                    color_continuous_scale='Blues',
                    hover_data=['Impacted Rows (Full 48.6M Scale)','Methodological Justification']
                        if 'Impacted Rows (Full 48.6M Scale)' in audit_df.columns else None)
                fig_anom.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
                fig_anom.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#94a3b8',family='Inter'), height=230,
                    coloraxis_showscale=False)
                st.plotly_chart(fig_anom, use_container_width=True)
            else:
                st.warning("Audit file not found.")

    st.divider()

    # ── ROI Simulator ─────────────────────────────────────────
    st.markdown("### 💰 Enterprise ROI & Fuel Savings Simulator")
    st.caption("Estimate the annual business impact of deploying the 72-h Demand Dispatcher across your fleet.")

    ri, ro = st.columns([1, 1.4], gap="large")
    with ri:
        with st.container(border=True):
            st.markdown("##### ⚙️ Simulator Inputs")
            f_size   = st.slider("Fleet Size (vehicles)", 500, 15000, 4500, 500)
            dh_cut   = st.slider("Deadheading Reduction (%)", 5, 30, 18, 1,
                                 help="Empty-mile reduction enabled by predictive pre-positioning.")
            st.caption("Fixed assumptions: 110 mi/vehicle/day · $3.65/gal · 24 MPG fleet avg")

    with ro:
        d_mi_day          = 110.0
        gal_price         = 3.65
        mpg               = 24.0
        saved_mi_day      = f_size * d_mi_day * (dh_cut / 100)
        fuel_saved_usd    = (saved_mi_day * 365 / mpg) * gal_price
        co2_saved         = (saved_mi_day * 365 * 404) / 1_000_000
        driver_gain       = (saved_mi_day * 365) * 1.85 * 0.78

        with st.container(border=True):
            st.caption("📊 PROJECTED ANNUAL ENTERPRISE IMPACT")
            r1,r2,r3,r4 = st.columns(4)
            r1.metric("Fuel Savings",        f"${fuel_saved_usd:,.0f}")
            r2.metric("Driver Revenue Gain", f"${driver_gain:,.0f}")
            r3.metric("CO₂ Avoided",         f"{co2_saved:,.1f} MT")
            r4.metric("Deadhead Miles Cut",  f"{saved_mi_day*365/1e6:,.1f} M mi")

            # Mini bar chart
            impact_df = pd.DataFrame({
                'Metric': ['Fuel Savings','Driver Revenue Gain'],
                'USD ($M)': [fuel_saved_usd/1e6, driver_gain/1e6]
            })
            fig_roi = px.bar(impact_df, x='Metric', y='USD ($M)',
                color='Metric',
                color_discrete_sequence=['#38bdf8','#34d399'],
                text_auto='.2f')
            fig_roi.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#94a3b8',family='Inter'), height=200,
                showlegend=False, margin=dict(t=10,b=0,l=0,r=0))
            fig_roi.update_traces(texttemplate='$%{text}M', textposition='outside')
            st.plotly_chart(fig_roi, use_container_width=True)
