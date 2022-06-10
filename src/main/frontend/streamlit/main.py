import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

st.subheader('Number of pickups by hour')
st.subheader('Map of all pickups at %s:00' % hour_to_filter)
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
