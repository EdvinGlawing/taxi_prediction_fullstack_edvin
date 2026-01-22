import streamlit as st
from taxipred.utils.constants import IMAGE_PATH

st.markdown("# Edvins Taxi Price Predictor")

st.markdown(""" This is a streamlit app that uses a ML model to calculate taxi trip prices.
To use this application, press Taxi Price Predictor on the sidebar and input your trip details.

""")

st.image(IMAGE_PATH/"taxipredpic.png") # AI generated picture