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

@app.post("/predict")
def predict_price(trip: TaxiUserInput):
    return {
        "message": "Prediction endpoint running",
        "input_received": trip.model_dump()
    }