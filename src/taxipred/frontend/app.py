import streamlit as st

pages = [
    st.Page("pages/home.py", title="Home"),
    st.Page("pages/price_predictor.py", title="Taxi Price Predictor")
]

pg = st.navigation(pages)

pg.run()
