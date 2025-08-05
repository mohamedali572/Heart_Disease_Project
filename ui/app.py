import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('../models/final_model.pkl')

st.title("Heart Disease Prediction")

# Example input fields
age = st.number_input("Age", 20, 100, 50)
cholesterol = st.number_input("Cholesterol", 100, 400, 200)
bp = st.number_input("Blood Pressure", 80, 200, 120)

if st.button("Predict"):
    # Dummy example: replace with actual feature vector
    features = pd.DataFrame([[age, cholesterol, bp]], columns=['age', 'cholesterol', 'bp'])
    prediction = model.predict(features)
    st.write("Prediction:", "Heart Disease" if prediction[0] == 1 else "No Heart Disease")
