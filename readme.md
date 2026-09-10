# Urban Flow Analytics — SLIIT Codefest Datathon 2026

## Project Structure
```
notebooks/
├── EDA_taxi_data.ipynb                  ← Member 1: EDA & Data Quality
├── Member2_PredictiveModeling.ipynb     ← Member 2: Fare & Duration Prediction
└── models/                              ← Trained .pkl models + dataset splits
```

## Branches
| Branch | Owner | Task |
|---|---|---|
| `master` | shared | base skeleton |
| `feature/member2-predictive-modeling` | Member 2 | Fare + Duration ML |
| `feature/member1-preprocessing` | Member 1 | EDA + Cleaning |
| `feature/member3-spatiotemporal` | Member 3 | Demand forecasting + AI agent |

## Setup
```bash
pip install -r requirements.txt
```

## Data
Place the 12 monthly CSVs in `../../Urban_Flow_Analytics_Dataset_csv/`  
Place `Urban_Flow_Analytics_Zone_Dataset.csv` in `../../`
