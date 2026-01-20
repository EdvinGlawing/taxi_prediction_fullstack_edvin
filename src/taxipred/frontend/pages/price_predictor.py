import streamlit as st
import httpx

st.title("Taxi Price Predictor")

distance_km = st.number_input(
    "Distance (km)",
    min_value=0.1,
    value=5.0,
    step=0.1
)

passengers = st.number_input(
    "Number of passengers",
    min_value=1,
    max_value=4,
    value=1
)

weather = st.selectbox(
    "Weather conditions",
    ["Clear", "Rain", "Snow"]
)

traffic = st.selectbox(
    "Traffic conditions",
    ["Low", "Medium", "High"]
)

if st.button("Predict price"):
    payload = {
        "distance_km": distance_km,
        "passengers": passengers,
        "weather": weather,
        "traffic": traffic
    }

    try:
        response = httpx.post(
            "http://127.0.0.1:8000/predict",
            json=payload,
            timeout=5
        )
        response.raise_for_status()

        result = response.json()
        st.success(f"Estimated price: {result['predicted_price']} SEK")

    except Exception as e:
        st.error("Could not get prediction from backend.")
        st.write(e)
