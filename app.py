import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("aqi_model.pkl", "rb"))

st.title("🌫 AQI Prediction App")
st.write("Enter environmental parameters to predict AQI")

# Input fields
PM25 = st.number_input("PM2.5", value=80.0)
PM10 = st.number_input("PM10", value=100.0)
SO2 = st.number_input("SO2", value=20.0)
NO2 = st.number_input("NO2", value=40.0)
CO = st.number_input("CO", value=1.0)
O3 = st.number_input("O3", value=60.0)
TEMP = st.number_input("Temperature (°C)", value=25.0)
PRES = st.number_input("Pressure", value=1010.0)
DEWP = st.number_input("Dew Point", value=10.0)
RAIN = st.number_input("Rainfall", value=0.0)
WSPM = st.number_input("Wind Speed", value=3.0)

# Features in same order as training
features = np.array([[PM25, PM10, SO2, NO2, CO, O3,
                      TEMP, PRES, DEWP, RAIN, WSPM]])

if st.button("Predict AQI"):
    prediction = model.predict(features)
    st.success(f"Predicted AQI: {prediction[0]:.2f}")
