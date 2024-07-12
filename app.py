import streamlit as st
import pandas as pd
import numpy as np
import requests

''' # Taxifare's Prediction Website'''

st.markdown('''
This website takes as inputs the pickup/drop-off locations, date&time and number of passengers in order to get how much would be the taxifare.

Plase fill the cells below:
            ''')

date_time= st.text_input('Date & Time', '')
st.write('Your pickup time is: ', date_time)


p_longitude= st.text_input('Pickup Longitude', '')
st.write("Your location's longitude is: ", p_longitude)


p_latitude= st.text_input('Pickup Latitude', '')
st.write("Your location's latitude is: ", p_latitude)


d_longitude= st.text_input('Drop-off Longitude', '')
st.write("Your destination's longitude is: ", d_longitude)


d_latitude= st.text_input('Drop-off Latitude', '')
st.write("Your destination's latitude is: ", d_latitude)

st.markdown('''


            ''')

passengers = st.slider('Select number of passengers', 1, 7, 1)
st.write("Number of Passengers: ", passengers)


parametros = {'pickup_datetime': date_time,
              'pickup_longitude': p_longitude,
              'pickup_latitude': p_latitude,
              'dropoff_longitude': d_longitude,
              'dropoff_latitude': d_latitude,
              'passenger_count': passengers,
}

url = 'https://taxifare.lewagon.ai/predict'
response = requests.get(url,params=parametros)
valor = response.json()

if st.button('Calculate Taxifare'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write('Fare amount: $USD', valor['fare'])

else:
    st.write('Push once all fields are filled')

def get_map_data():

    return pd.DataFrame(
            [(40.5,-73.7),(40.9, -74.3)],
            columns=['lat', 'lon']
        )

df = get_map_data()
st.map(df)
