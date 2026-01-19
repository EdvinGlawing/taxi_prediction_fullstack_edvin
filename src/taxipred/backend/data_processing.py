from taxipred.utils.constants import CLEAN_TAXI_CSV_PATH, MODEL_PATH
import pandas as pd
import json
import joblib

class TaxiData:
    def __init__(self):
        self.df = pd.read_csv(CLEAN_TAXI_CSV_PATH)
        self.model = joblib.load(MODEL_PATH)

    def to_json(self):
        return json.loads(self.df.to_json(orient="records"))
        
    def predict_price(self, input_data: dict) -> float:
        input_df = pd.DataFrame([input_data])
        prediction = self.model.predict(input_df)[0]
        return float(prediction)