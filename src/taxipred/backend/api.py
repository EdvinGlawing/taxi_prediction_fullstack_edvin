from fastapi import FastAPI
from taxipred.backend.data_processing import TaxiData

app = FastAPI()

taxi_data = TaxiData()


@app.get("/")
def health_check():
    return {"status": "ok"}
