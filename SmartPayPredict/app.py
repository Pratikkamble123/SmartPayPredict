
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="SmartPayPredict", layout="centered")

st.title("💼 SmartPayPredict: Salary Forecasting System")

model = joblib.load("salary_predictor.pkl")

# Input form
with st.form("salary_form"):
    name = st.text_input("Employee Name")
    experience = st.number_input("Years of Experience", min_value=0, max_value=50)
    education = st.selectbox("Education Level", ["Bachelors", "Masters", "PhD"])
    role = st.selectbox("Job Role", ["Data Scientist", "Software Engineer", "Web Developer"])
    city = st.selectbox("City Tier", ["1", "2", "3"])
    skills = st.multiselect("Technical Skills", ["Python", "Java", "SQL", "Spring", "HTML", "CSS", "JavaScript"])
    cert = st.radio("Certifications", ["Yes", "No"])
    company = st.selectbox("Company Size", ["Small", "Medium", "Large"])
    submitted = st.form_submit_button("Predict Salary")

    if submitted:
        input_df = pd.DataFrame([{
            "Experience": experience,
            "Education": education,
            "Role": role,
            "City_Tier": city,
            "Skills": ",".join(skills),
            "Certifications": cert,
            "Company_Size": company
        }])

        prediction = model.predict(input_df)[0]
        st.success(f"💰 Estimated Salary for {name}: ₹ {int(prediction):,}")
