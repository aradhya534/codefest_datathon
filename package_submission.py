"""
Automated Submission Packager — SLIIT Codefest Datathon 2026
Strictly complies with the official Datathon submission guidelines:
1. Technical Report (PDF/MD)
2. Source code including TeamName_FinalNotebook.ipynb
3. Trained Models (.pkl)
4. Clearly separated dataset splits (train/val/test)
5. Demo Video Script & Links
Output ZIP: TeamName_CodefestDatathon2026.zip
"""

import os
import sys
import zipfile
import shutil

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def make_submission_zip(team_name="CodeWave"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    zip_filename = f"{team_name}_CodefestDatathon2026.zip"
    zip_filepath = os.path.join(base_dir, zip_filename)
    
    print(f"📦 Packaging submission for team: {team_name}...")
    print(f"Target file: {zip_filename}")
    
    # Official final notebook name requirement: TeamName_FinalNotebook.ipynb
    official_nb_name = f"{team_name}_FinalNotebook.ipynb"
    src_master_nb = os.path.join(base_dir, "notebooks", "CodeWave_FinalNotebook.ipynb")
    dst_team_nb = os.path.join(base_dir, "notebooks", official_nb_name)
    
    if os.path.exists(src_master_nb) and src_master_nb != dst_team_nb:
        shutil.copyfile(src_master_nb, dst_team_nb)
        created_temp_nb = True
    else:
        created_temp_nb = False
        
    included_files = [
        "TECHNICAL_REPORT.md",
        "MEMBER2_REPORT_SECTION.md",
        "DEMO_VIDEO_SCRIPT.md",
        "app.py",
        "dashboard.html",
        "hotspots_map.html",
        "readme.md",
        "requirements.txt",
        "setup.py"
    ]
    
    notebook_files = [
        official_nb_name,
        "EDA_taxi_data.ipynb",
        "Member2_PredictiveModeling.ipynb",
        "Member3_SpatialTemporal_Demand_AI.ipynb",
        "predict.py",
        "ai_mobility_assistant.py"
    ]
    
    included_dirs = [
        ("notebooks", [f for f in notebook_files if os.path.exists(os.path.join(base_dir, "notebooks", f))]),
        ("cleaned_data", ["urban_flow_cleaned.csv", "powerbi_kpi_summary.csv", "anomaly_cleaning_audit.csv"]),
        ("cleaned_data/plots", os.listdir(os.path.join(base_dir, "cleaned_data", "plots")) if os.path.exists(os.path.join(base_dir, "cleaned_data", "plots")) else []),
        ("notebooks/models", ["fare_model_lightgbm.pkl", "duration_model_xgboost.pkl", "model_metadata.json", "cleaning_log.json"]),
        ("notebooks/models/plots", os.listdir(os.path.join(base_dir, "notebooks", "models", "plots")) if os.path.exists(os.path.join(base_dir, "notebooks", "models", "plots")) else []),
        ("notebooks/models/splits", os.listdir(os.path.join(base_dir, "notebooks", "models", "splits")) if os.path.exists(os.path.join(base_dir, "notebooks", "models", "splits")) else []),
        ("notebooks/spatiotemporal", ["demand_forecast_lgb.pkl", "hotspot_kmeans_model.pkl", "member3_metrics.json", "zone_hotspot_clusters.csv"]),
        ("notebooks/spatiotemporal/plots", os.listdir(os.path.join(base_dir, "notebooks", "spatiotemporal", "plots")) if os.path.exists(os.path.join(base_dir, "notebooks", "spatiotemporal", "plots")) else [])
    ]
    
    count = 0
    with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in included_files:
            fp = os.path.join(base_dir, f)
            if os.path.exists(fp):
                zf.write(fp, arcname=f)
                count += 1
                print(f"  + {f}")
                
        for dir_name, fnames in included_dirs:
            for fn in fnames:
                fp = os.path.join(base_dir, dir_name, fn)
                if os.path.isfile(fp):
                    arc_path = os.path.join(dir_name, fn)
                    zf.write(fp, arcname=arc_path)
                    count += 1
                    print(f"  + {arc_path}")
                    
    # Clean up temp notebook if copied
    if created_temp_nb and os.path.exists(dst_team_nb):
        os.remove(dst_team_nb)
        
    size_mb = os.path.getsize(zip_filepath) / (1024 * 1024)
    print("\n" + "=" * 55)
    print(f"✅ Created {zip_filename} ({size_mb:.2f} MB)")
    print(f"Total files packaged: {count}")
    print(f"Official notebook included: notebooks/{official_nb_name}")
    print("=" * 55)

if __name__ == "__main__":
    tname = sys.argv[1] if len(sys.argv) > 1 else "CodeWave"
    make_submission_zip(tname)
