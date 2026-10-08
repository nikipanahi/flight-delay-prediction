import streamlit as st
import pandas as pd
import joblib

rf = joblib.load('rf.joblib')
st.title('Flight Data Prediction')
st.write('Enter your flight data to predict its delay.')
distance = st.number_input("Distance", min_value=0.0, value=500.0)
airline = st.selectbox("Airline Name", ['United Air Lines Inc.',
 'American Airlines Inc.',
 'JetBlue Airways',
 'Delta Air Lines Inc.',
 'ExpressJet Airlines Inc.',
 'Envoy Air',
 'US Airways Inc.',
 'Southwest Airlines Co.',
 'Virgin America',
 'AirTran Airways Corporation',
 'Alaska Airlines Inc.',
 'Endeavor Air Inc.',
 'Frontier Airlines Inc.',
 'Hawaiian Airlines Inc.',
 'Mesa Airlines Inc.',
 'SkyWest Airlines Inc.'])
year = st.number_input("Year:", value=2026)
month = st.number_input("Month:", min_value=1, max_value=12, value=6)
day = st.number_input("Day:", min_value=1, max_value=31, value=15)
dep_time = st.number_input("Dep Time:", value=1200.0)
sched_dep_time = st.number_input("Sched Dep Time:", value=1200.0)
origin_encoded = st.number_input("Origin Encoded :", value=0)
dest_encoded = st.number_input("Dest Encoded :", value=1)
air_time = st.number_input("Air Time:", value=150.0)
distance = st.number_input("Distance:", value=500.0)
hour = st.number_input(" Departure (Hour):", min_value=0, max_value=23, value=12)
name_encoded = st.number_input("Airline Code  (Name Encoded):", value=0)

st.title('Flight Delay Prediction')
input_data =pd.DataFrame({
    'year': [year],
    'month': [month],
    'day': [day],
    'dep_time':[dep_time],
    'sched_dep_time': [sched_dep_time],
    'origin_encoded': [origin_encoded],
    'dest_encoded': [dest_encoded],
    'air_time': [air_time],
    'distance':[distance],
    'hour': [hour],
    'name_encoded': [name_encoded]
})
if st.button('Predict'):
    prediction_delay=rf.predict_proba(input_data)
    prediction=prediction_delay[0][1]*100
    if (prediction>50):
        st.error(f"The flight has probably {prediction:.1f}% delay.")
    else:
        st.success('No delay')
        st.write(f"Probability of flight delay: {prediction:.1f}%")
