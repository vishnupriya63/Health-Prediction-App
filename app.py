import streamlit as st
import numpy as np
import joblib
from database import create_table, insert_patient

# Load model
model = joblib.load("model.pkl")

create_table()

st.title("🏥 Health Prediction App (Diabetes Prediction)")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age")
hypertension = st.number_input("Hypertension (0 or 1)")
heart_disease = st.number_input("Heart Disease (0 or 1)")
smoking_history = st.selectbox("Smoking History", ["never", "former", "current"])
bmi = st.number_input("BMI")
hba1c = st.number_input("HbA1c Level")
glucose = st.number_input("Blood Glucose Level")

# Convert categorical → numeric (VERY IMPORTANT)
gender_val = 1 if gender == "Male" else 0
smoking_map = {"never": 0, "former": 1, "current": 2}
smoking_val = smoking_map[smoking_history]

if st.button("Predict"):
    input_data = np.array([[gender_val, age, hypertension, heart_disease,
                            smoking_val, bmi, hba1c, glucose]])

    prediction = model.predict(input_data)[0]

    result = "⚠️ Diabetic" if prediction == 1 else "✅ Not Diabetic"

    st.success(result)

    insert_patient("User", age, result)