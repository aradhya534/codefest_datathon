"""
Inference Module for Member 2: Urban Flow Analytics
Allows real-time prediction of upfront base fare and trip duration.
Used by Dashboard (Member 1) and AI Mobility Assistant (Member 3).
"""

import os
import json
import joblib
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")
ZONE_CSV = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "Urban_Flow_Analytics_Zone_Dataset.csv"))

class UrbanFlowPredictor:
    def __init__(self, models_dir=MODELS_DIR, zone_file=ZONE_CSV):
        self.models_dir = models_dir
        self.meta_path = os.path.join(models_dir, "model_metadata.json")
        
        with open(self.meta_path, "r") as f:
            self.metadata = json.load(f)
            
        self.fare_model_name = self.metadata["best_fare_model"].lower()
        self.dur_model_name = self.metadata["best_dur_model"].lower()
        
        fare_model_file = os.path.join(models_dir, f"fare_model_{self.fare_model_name}.pkl")
        dur_model_file = os.path.join(models_dir, f"duration_model_{self.dur_model_name}.pkl")
        
        self.fare_model = joblib.load(fare_model_file)
        self.dur_model = joblib.load(dur_model_file)
        self.features = self.metadata["features"]
        
        # Load zone data for borough lookup
        if os.path.exists(zone_file):
            self.zones = pd.read_csv(zone_file).set_index("loc_id")
        else:
            self.zones = None

    def _prepare_features(self, origin_loc_id, dest_loc_id, distance_miles, rider_count=1,
                          pickup_time=None, rate_class_id=1, toll_total=0.0):
        if pickup_time is None:
            pickup_time = datetime.now()
        elif isinstance(pickup_time, str):
            pickup_time = pd.to_datetime(pickup_time)
            
        pickup_hour = pickup_time.hour
        pickup_dayofweek = pickup_time.weekday()
        pickup_month = pickup_time.month
        
        is_weekend = int(pickup_dayofweek >= 5)
        is_rush_hour = int(pickup_hour in [7, 8, 9, 17, 18, 19])
        is_night = int((pickup_hour >= 22) or (pickup_hour < 6))
        
        AIRPORT_ZONES = {132, 138, 1}
        is_airport_pickup = int(origin_loc_id in AIRPORT_ZONES)
        is_airport_dropoff = int(dest_loc_id in AIRPORT_ZONES)
        
        # Lookup boroughs if available
        pickup_borough_enc = 0
        dropoff_borough_enc = 0
        pickup_service_zone_enc = 0
        dropoff_service_zone_enc = 0
        inter_borough = 0
        
        if self.zones is not None:
            o_info = self.zones.loc[origin_loc_id] if origin_loc_id in self.zones.index else None
            d_info = self.zones.loc[dest_loc_id] if dest_loc_id in self.zones.index else None
            
            if o_info is not None and d_info is not None:
                inter_borough = int(o_info["borough_name"] != d_info["borough_name"])
                
        feature_dict = {
            'distance_miles': float(distance_miles),
            'rider_count': float(rider_count),
            'rate_class_id': float(rate_class_id),
            'origin_loc_id': int(origin_loc_id),
            'dest_loc_id': int(dest_loc_id),
            'pickup_hour': int(pickup_hour),
            'pickup_dayofweek': int(pickup_dayofweek),
            'pickup_month': int(pickup_month),
            'is_weekend': int(is_weekend),
            'is_rush_hour': int(is_rush_hour),
            'is_night': int(is_night),
            'is_airport_pickup': int(is_airport_pickup),
            'is_airport_dropoff': int(is_airport_dropoff),
            'inter_borough': int(inter_borough),
            'pickup_borough_enc': int(pickup_borough_enc),
            'dropoff_borough_enc': int(dropoff_borough_enc),
            'pickup_service_zone_enc': int(pickup_service_zone_enc),
            'dropoff_service_zone_enc': int(dropoff_service_zone_enc),
            'toll_total': float(toll_total)
        }
        
        df_feats = pd.DataFrame([feature_dict])[self.features]
        return df_feats, pickup_time

    def predict(self, origin_loc_id, dest_loc_id, distance_miles, rider_count=1,
                pickup_time=None, rate_class_id=1, toll_total=0.0):
        """
        Returns upfront fare ($), estimated duration (mins), and estimated dropoff datetime.
        """
        X, p_time = self._prepare_features(
            origin_loc_id=origin_loc_id,
            dest_loc_id=dest_loc_id,
            distance_miles=distance_miles,
            rider_count=rider_count,
            pickup_time=pickup_time,
            rate_class_id=rate_class_id,
            toll_total=toll_total
        )
        
        pred_fare = max(2.50, float(self.fare_model.predict(X)[0]))
        pred_duration = max(1.0, float(self.dur_model.predict(X)[0]))
        eta_time = p_time + timedelta(minutes=pred_duration)
        
        return {
            "predicted_base_fare": round(pred_fare, 2),
            "predicted_duration_minutes": round(pred_duration, 1),
            "pickup_time": p_time.strftime("%Y-%m-%d %H:%M:%S"),
            "estimated_arrival_time": eta_time.strftime("%Y-%m-%d %H:%M:%S"),
            "model_fare_engine": self.fare_model_name,
            "model_duration_engine": self.dur_model_name
        }

if __name__ == "__main__":
    predictor = UrbanFlowPredictor()
    # Test a sample trip: LGA Airport (138) to Midtown Manhattan (230), 9.5 miles
    result = predictor.predict(
        origin_loc_id=138,
        dest_loc_id=230,
        distance_miles=9.5,
        rider_count=1,
        pickup_time="2025-05-10 18:30:00",
        toll_total=6.94
    )
    print("--- Sample Prediction Output ---")
    print(json.dumps(result, indent=2))
