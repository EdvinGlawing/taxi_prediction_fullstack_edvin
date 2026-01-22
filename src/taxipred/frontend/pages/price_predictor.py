import streamlit as st
import httpx

st.title("Taxi Price Predictor")

Trip_Distance_km = st.number_input(
    "Distance (km)",
    min_value=0.1,
    value=5.0,
    step=0.1
)

Passenger_Count = st.number_input(
    "Number of passengers",
    min_value=1,
    max_value=4,
    value=1
)

Weather = st.selectbox(
    "Weather conditions",
    ["Clear", "Rain", "Snow"]
)

Traffic_Conditions = st.selectbox(
    "Traffic conditions",
    ["Low", "Medium", "High"]
)

Day_of_Week = st.selectbox(
    "Day of Week",
    ["Weekday", "Weekend"]
)

Time_of_Day = st.selectbox(
    "Time of Day",
    ["Morning", "Afternoon", "Evening"]
)

if st.button("Predict price"):
    payload = {
        "Trip_Distance_km": Trip_Distance_km,
        "Passenger_Count": Passenger_Count,
        "Weather": Weather,
        "Traffic_Conditions": Traffic_Conditions,
        "Day_of_Week": Day_of_Week,
        "Time_of_Day": Time_of_Day
    }

    try:
        response = httpx.post(
            "http://127.0.0.1:8000/predict",
            json=payload,
            timeout=5
        )
        response.raise_for_status()

        result = response.json()
        st.success(f"Estimated price: {result['predicted_price']} USD")

    except Exception as e:
        st.error("Could not get prediction from backend.")
        st.write(e)