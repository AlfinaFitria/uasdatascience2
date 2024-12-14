# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13rkE-sSkRl46j0laYibHKAtOJQz1-m6g
"""




import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('wine_quality_model.pkl')

# Define the app title
st.title("Wine Quality Prediction App")
st.markdown("This app predicts the quality of wine (low, medium, or high) based on its chemical properties.")

# Sidebar inputs
st.sidebar.header("Input Features")

def user_input_features():
    fixed_acidity = st.sidebar.slider('Fixed Acidity', 4.0, 16.0, 8.0)
    volatile_acidity = st.sidebar.slider('Volatile Acidity', 0.1, 1.5, 0.5)
    citric_acid = st.sidebar.slider('Citric Acid', 0.0, 1.0, 0.3)
    residual_sugar = st.sidebar.slider('Residual Sugar', 0.5, 15.0, 2.5)
    chlorides = st.sidebar.slider('Chlorides', 0.01, 0.1, 0.05)
    free_sulfur_dioxide = st.sidebar.slider('Free Sulfur Dioxide', 1.0, 72.0, 15.0)
    total_sulfur_dioxide = st.sidebar.slider('Total Sulfur Dioxide', 6.0, 289.0, 46.0)
    density = st.sidebar.slider('Density', 0.990, 1.004, 0.996)
    pH = st.sidebar.slider('pH', 2.9, 4.0, 3.3)
    sulphates = st.sidebar.slider('Sulphates', 0.3, 2.0, 0.6)
    alcohol = st.sidebar.slider('Alcohol', 8.0, 15.0, 10.0)

    data = {
        'fixed acidity': fixed_acidity,
        'volatile acidity': volatile_acidity,
        'citric acid': citric_acid,
        'residual sugar': residual_sugar,
        'chlorides': chlorides,
        'free sulfur dioxide': free_sulfur_dioxide,
        'total sulfur dioxide': total_sulfur_dioxide,
        'density': density,
        'pH': pH,
        'sulphates': sulphates,
        'alcohol': alcohol
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Display user input features
st.subheader("User Input Features")
st.write(input_df)

# Predict quality
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

# Map predictions to labels
quality_mapping = {0: "Low", 1: "Medium", 2: "High"}

# Display prediction
st.subheader("Prediction")
st.write(f"The predicted wine quality is: **{quality_mapping[prediction[0]]}**")

# Display prediction probabilities
st.subheader("Prediction Probabilities")
st.write("The probabilities for each quality label are:")
pred_proba_df = pd.DataFrame(prediction_proba, columns=['Low', 'Medium', 'High'])
st.write(pred_proba_df)

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ Alfina Fitria")
