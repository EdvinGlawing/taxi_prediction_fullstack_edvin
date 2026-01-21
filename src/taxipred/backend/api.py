from fastapi import FastAPI
from taxipred.backend.data_processing import TaxiData
from pydantic import BaseModel, Field


app = FastAPI()

taxi_data = TaxiData()

class TaxiUserInput(BaseModel):
    Trip_Distance_km: float = Field(gt=0)
    Passenger_Count: int = Field(ge=1, le=4)
    Weather: str
    Traffic_Conditions: str
    Day_of_Week: str
    Time_of_Day: str

@app.get("/")
def health_check():
    return {"status": "API running"}

def build_model_input(trip: TaxiUserInput) -> dict:
    # Start with all model features set to 0
    model_input = {feature: 0 for feature in taxi_data.features}

    # We make assumptions in the categories the
    # user does not have any input.
    base_fare = 3.5
    per_km_rate = 1.2
    per_minute_rate = 0.3
    avg_speed_kmh = 43

    # Calculate trip duration 
    trip_duration_minutes = (trip.Trip_Distance_km / avg_speed_kmh) * 60

    # Numerical features
    model_input["Trip_Distance_km"] = trip.Trip_Distance_km
    model_input["Passenger_Count"] = trip.Passenger_Count
    model_input["Base_Fare"] = base_fare
    model_input["Per_Km_Rate"] = per_km_rate
    model_input["Per_Minute_Rate"] = per_minute_rate
    model_input["Trip_Duration_Minutes"] = trip_duration_minutes

    # One-hot encoded categorical features
    weather_col = f"Weather{trip.Weather}"
    traffic_col = f"Traffic_Conditions{trip.Traffic_Conditions}"
    day_col = f"Day_of_Week{trip.Day_of_Week}"
    time_col = f"Time_of_Day{trip.Time_of_Day}"

    for col in [weather_col, traffic_col, day_col, time_col]:
        if col in model_input:
            model_input[col] = 1

    return model_input

@app.post("/predict")
def predict_price(trip: TaxiUserInput):
    model_input = build_model_input(trip)
    price = taxi_data.model.predict([list(model_input.values())])[0]

    return {
        "predicted_price": round(float(price), 2)
}