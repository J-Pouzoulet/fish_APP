import streamlit as st
import pandas as pd
import numpy as np
import requests as rq
import json

st.image('https://dailytravelpill.com/wp-content/uploads/2020/04/busan-jagalchi-fish-market-fb.jpg')

dict_height = {'Bream': 19.0, 'Roach': 10.0, 'Whitefish' : 13.0, 'Parkki' : 12.0, 'Perch' : 13.0, 'Pike' : 11.0, 'Smelt' : 3.0}

col1, col2 = st.columns(2)

with col1:

    option = st.radio(
        'Which fish species weight would you like to predict?',
        ('Bream', 'Roach', 'Whitefish', 'Parkki', 'Perch', 'Pike', 'Smelt'))

with col2:
    
    max_H = float(dict_height[option])
    Height = st.number_input('Insert a number')
    if Height >= max_H:
        Height = max_H
    Height = st.slider(
    'Select a {option} Height',
    0.0, max_H, (Height))
    st.write('The current Height is ', Height)
    st.write(f'Note that the Height of {option} cannot exceed {max_H} cm')
    #st.write('Values:', Height)

if st.button('Predict Fish Weight'):
    #call fast_api when opened in local uvicorn server 
    res = rq.get(f'http://127.0.0.1:8000/?Species={option}&Height={Height}').json()
    Weight = int(float(res['Weight']))
    st.write(f'Your {option} likely weight {Weight} g')
else:
    pass