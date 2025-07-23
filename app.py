import streamlit as st
import pandas as pd
import joblib

try:
    model = joblib.load("best_regression_model.pkl")
except FileNotFoundError:
    st.error("Error: 'best_regression_model.pkl' not found. Please ensure the model file is in the correct directory.")
    st.stop()

st.set_page_config(
    page_title="💼 Employee Salary Predictor",
    page_icon="💰",
    layout="wide"
)

st.markdown("""
    <style>
        .stApp {
            background-color: #EEA0D4;
            font-family: 'Segoe UI', sans-serif;
            color: #000000;
        }
        .main-container {
            padding: 0;
            margin: 2rem auto;
            width: 92%;
            max-width: 1000px;
            border-radius: 20px;
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.2);
            color: #000000;
            overflow: hidden;
        }
        .header-area {
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center 35%;
            min-height: 250px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            border-top-left-radius: 20px;
            border-top-right-radius: 20px;
            padding-bottom: 30px;
        }
        .big-title {
            font-size: 3.6rem;
            text-align: center;
            font-weight: 800;
            color: #000000;
            font-family: 'Georgia', serif;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.6);
            border-radius: 10px;
            text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);
            margin: 0;
            line-height: 1.2;
        }
        .content-area {
            padding: 0;
            background-color: transparent;
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 20px;
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }
        .content-section {
            background-color: #ffffffee;
            padding: 2.5rem 4rem;
            border-radius: 20px;
        }
        .personal-details-header, .job-profile-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 0;
            margin-bottom: 1rem;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 0.5rem;
        }
        .personal-details-header h2, .job-profile-header h2 {
            margin: 0;
            color: #722F37;
            font-weight: 700;
            font-size: 2rem;
        }
        .personal-details-header img, .job-profile-header img {
            max-width: 140px;
            height: auto;
            border-radius: 8px;
            margin-left: 15px;
            object-fit: contain;
        }
        div.stButton > button {
            background: linear-gradient(to right, #FF0800, #E00700);
            border: 2px solid #CC0700;
            padding: 1.2rem 2.5rem;
            border-radius: 15px;
            font-size: 1.3rem;
            color: white;
            font-weight: bold;
            box-shadow: 0 6px 10px rgba(0,0,0,0.4);
            transition: all 0.2s ease-in-out;
            margin-top: 2rem;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        div.stButton > button:hover {
            transform: translateY(-2px) scale(1.05);
            box-shadow: 0 10px 20px rgba(0,0,0,0.5);
            cursor: pointer;
        }
        h2.section-title {
            font-size: 2rem;
            color: #722F37;
            font-weight: 700;
            margin-top: 2.5rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 0.5rem;
        }
        .prediction-summary {
            text-align: center;
            font-size: 1.2rem;
            color: #Ff0000;
            font-weight: 500;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        .warning-note {
            text-align: center;
            font-size: 1rem;
            color: #Ff0000;
            margin-top: 2rem;
            font-weight: 500;
        }

        label[data-testid="stWidgetLabel"] p {
            font-size: 1.15rem;
            font-weight: 600;
            color: #333333;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.markdown("""
    <div class='header-area'>
        <div class='big-title'>💼 Employee Salary Prediction</div>
    </div>
    <div class='content-area'>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='content-section'>
        <div class='personal-details-header'>
            <h2>📄 Personal Details</h2>
            <img src='https://cdn-icons-png.flaticon.com/512/2922/2922510.png'>
        </div>
""", unsafe_allow_html=True)

with st.form("prediction_form", clear_on_submit=False):
    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("🎂 Age", 18, 65, 30)
        gender = st.selectbox("👤 Gender", ["Male", "Female", "Other"])

    with col2:
        experience = st.slider("💼 Years of Experience", 0, 40, 5)
        education = st.selectbox("🎓 Education Level", ["Bachelor's", "Master's", "PhD"])

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='content-section'>
        <div class='job-profile-header'>
            <h2>💼 Job Profile</h2>
            <img src='https://cdn-icons-png.flaticon.com/512/1946/1946429.png'>
        </div>
    """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        job_title = st.selectbox("💻 Job Title", [
            "Software Engineer", "Data Scientist", "Product Manager", "Designer",
            "Sales Associate", "HR Specialist"])
        industry = st.selectbox("🏢 Industry", [
            "Technology", "Healthcare", "Finance", "Education", "Manufacturing", "Retail"])
    with col4:
        country = st.selectbox("🌍 Country", ["India", "USA", "UK", "Canada", "Germany", "Australia"])
        city_tier = st.selectbox("🏙️ City Tier", ["Tier 1", "Tier 2", "Tier 3"])
        remote_work = st.selectbox("🏠 Remote Work", ["Yes", "No"])

    submit_button = st.form_submit_button("🚀 Estimate Salary")

if submit_button:
    if experience > age:
        st.error("❌ Years of experience cannot be greater than age.")
    elif experience > 40:
        st.warning("⚠️ Experience seems too high (over 40 years). Please verify input.")
    elif age - experience < 15:
        st.warning("⚠️ Please verify age and experience. Too early experience?")
    else:
        input_df = pd.DataFrame({
            "Age": [age],
            "Years of Experience": [experience],
            "Gender": [gender],
            "Education Level": [education],
            "Job Title": [job_title],
            "Country": [country],
            "City Tier": [city_tier],
            "Remote Work": [remote_work],
            "Industry": [industry]
        })

        try:
            monthly_inr = model.predict(input_df)[0]
            annual_inr = monthly_inr * 12
            monthly_usd = monthly_inr / 83.0
            annual_usd = annual_inr / 83.0

            st.success("💰 **Estimated Salary**")
            st.success(f"📅 **Annual:** ₹{annual_inr:.2f} / ${annual_usd:.2f} USD")
            st.success(f"🗓️ **Monthly:** ₹{monthly_inr:.2f} / ${monthly_usd:.2f} USD")

        except Exception as e:
            st.error(f"⚠️ Error making prediction: {e}")
            st.info("Please ensure your 'best_regression_model.pkl' can process the given input features and their formats.")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<p class='prediction-summary'>
    *Estimate the expected annual salary in INR & USD based on employee background.*
</p>
<p class='warning-note'>
    *Note: Predictions are based on a specific dataset and may not generalize to all real-world cases.*
</p>
</div>
</div>
""", unsafe_allow_html=True)