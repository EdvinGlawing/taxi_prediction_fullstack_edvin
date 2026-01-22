from pathlib import Path

DATA_PATH = Path(__file__).parents[1] / "data"
TAXI_CSV_PATH = DATA_PATH / "taxi_trip_pricing.csv"
CLEAN_TAXI_CSV_PATH = DATA_PATH /"cleaned_taxi_data.csv"
MODEL_PATH = DATA_PATH /"taxi_price_predictor.joblib"
IMAGE_PATH = Path(__file__).parents[1] / "images"