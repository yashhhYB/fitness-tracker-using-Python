import streamlit as st
import pandas as pd
from model import predict, train_model  # Import the predict and train_model functions

# Title of the app
st.title("Self Health Tracker")

# Input fields for user data
age = st.number_input("Enter your age:")
weight = st.number_input("Enter your weight (kg):")
height = st.number_input("Enter your height (cm):")
bmi = st.number_input("Enter your BMI:")
body_temperature = st.number_input("Enter your body temperature (°C):")
heart_rate = st.number_input("Enter your heart rate (bpm):")
gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
bmi_duration = st.number_input("Enter your BMI duration (days):")
activity_level = st.selectbox("Select your activity level:", ["Sedentary", "Light", "Moderate", "Active"])

if st.button("Submit"):
    # Process the input data into a DataFrame
    input_data = pd.DataFrame({
        'age': [age],
        'weight': [weight],
        'height': [height],
        'bmi': [bmi],
        'body_temperature': [body_temperature],
        'heart_rate': [heart_rate],
        'gender': [gender],
        'bmi_duration': [bmi_duration],
        'activity_level': [activity_level]
    })

    # Load the trained model (this should be done outside the button click in a real app)
    data = pd.read_csv('data.csv')  # Load the dataset



    model = train_model(data)  # Load or train the model

    # Make predictions
    prediction, recommendation = predict(model, input_data)

    st.success(f"Predicted kilocalories burned: {prediction[0]}")  # Display prediction
    st.write(recommendation)  # Display exercise recommendation

# Displaying the data
st.write("Your entered data:")
st.write(f"Age: {age}, Weight: {weight}, Height: {height}, Activity Level: {activity_level}")
