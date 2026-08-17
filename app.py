import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("diabetes_model.sav", "rb"))
scaler = pickle.load(open("scaler.sav", "rb"))

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺"
)

st.title("🩺 Diabetes Prediction System")
st.write("Enter the patient's details below to predict diabetes.")

# Input fields
pregnancies = st.number_input(
    "Pregnancies",
    min_value=0,
    max_value=20,
    value=0
)

glucose = st.number_input(
    "Glucose",
    min_value=0,
    max_value=300,
    value=120
)

blood_pressure = st.number_input(
    "Blood Pressure",
    min_value=0,
    max_value=200,
    value=70
)

skin_thickness = st.number_input(
    "Skin Thickness",
    min_value=0,
    max_value=100,
    value=20
)

insulin = st.number_input(
    "Insulin",
    min_value=0,
    max_value=900,
    value=80
)

bmi = st.number_input(
    "BMI",
    min_value=0.0,
    max_value=70.0,
    value=25.0
)

diabetes_pedigree = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0,
    max_value=3.0,
    value=0.5
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=30
)

# Prediction
if st.button("Predict Diabetes"):

    input_data = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree,
        age
    ]])

    # Apply same scaling used during training
    input_data_scaled = scaler.transform(input_data)

    prediction = model.predict(input_data_scaled)

    if prediction[0] == 0:
        st.success("The person is NOT diabetic.")
    else:
        st.error("The person is diabetic.")