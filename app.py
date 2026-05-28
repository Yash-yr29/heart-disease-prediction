import streamlit as st
import pandas as pd
import joblib

# LOAD MODEL
model = joblib.load("model/best_model.pkl")

# TITLE
st.title("Heart Disease Prediction System")
st.write("Enter Patient Details")


# USER INPUTS
age = st.number_input("Age")
resting_bp = st.number_input("Resting Blood Pressure (mmHg)")
cholesterol = st.number_input("Cholesterol (mg/dl)")
fasting_bs = st.selectbox(
    "Fasting Blood Sugar (1: if FastingBS > 120 mg/dl, 0: otherwise)",
    [0, 1]
)
max_hr = st.number_input("Maximum Heart Rate")
oldpeak = st.number_input(
    "Oldpeak(Numeric value measured in depression)",
    step=0.1
)
sex = st.selectbox(
    "Sex",
    ["M", "F"]
)
chest_pain = st.selectbox(
    "Chest Pain Type",
    ["ATA -Atypical Angina", "NAP -Non-Anginal Pain", "TA - Typical Angina", "ASY - Asymptomatic]"]
)
resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVH"]
)
exercise_angina = st.selectbox(
    "Exercise Angina",
    ["Y", "N"]
)

st_slope = st.selectbox(
    "ST Slope",
    ["Flat", "Up", "Down"]
)

# PREDICTION BUTTON

if st.button("Predict"):

    #INPUT DATA
    input_data = pd.DataFrame({

        'Age': [age],
        'RestingBP': [resting_bp],
        'Cholesterol': [cholesterol],
        'FastingBS': [fasting_bs],
        'MaxHR': [max_hr],
        'Oldpeak': [oldpeak],
        'Sex_M': [1 if sex == "M" else 0],
        'ChestPainType_ATA': [1 if chest_pain == "ATA" else 0],
        'ChestPainType_NAP': [1 if chest_pain == "NAP" else 0],
        'ChestPainType_TA': [1 if chest_pain == "TA" else 0],
        'RestingECG_Normal': [1 if resting_ecg == "Normal" else 0],
        'RestingECG_ST': [1 if resting_ecg == "ST" else 0],
        'ExerciseAngina_Y': [1 if exercise_angina == "Y" else 0],
        'ST_Slope_Flat': [1 if st_slope == "Flat" else 0],
        'ST_Slope_Up': [1 if st_slope == "Up" else 0]
    })

    # PREDICTION
    prediction = model.predict(input_data)

    # OUTPUT
    if prediction[0] == 1:
        st.error("Heart Disease Detected")
    else:
        st.success("No Heart Disease Detected")