import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open('/Users/blessy/Desktop/project/House_prediction_model.pk1','rb'))

st.header('House Price Prediction')
data = pd.read_csv('/Users/blessy/Desktop/project/Cleaned_data.csv')

loc = st.selectbox('Choose the location',data['location'].unique())
sqft = st.number_input('Enter Total Sqft')
beds = st.number_input('Enter No Of Bedrooms')
bath = st.number_input('Enter No Of Bathrooms')
balc = st.number_input('Enter No Of Balconies')

input = pd.DataFrame([[loc,sqft,bath,balc,beds]],columns=['location','total_sqft','bath','balcony'	,'bedrooms'])


if st.button("Predict price"):
    output = model.predict(input)
    out_str = f"Price of the house is ₹ {output[0] * 100000:,.2f}"
    st.success(out_str)
    