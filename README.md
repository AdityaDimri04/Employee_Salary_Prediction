
# 💼 Employee Salary Prediction

A **Streamlit-powered web app** that predicts an employee’s **annual and monthly salary** (in both INR and USD) based on personal and professional attributes like age, gender, education, experience, job title, location, industry, and remote work status.

---

## 🔗 Live Demo

👉 [Launch the App]
   (https://employeesalaryprediction-zjvtbazkxuuchugssy4sdj.streamlit.app/)

---

## 📋 Features

- Predicts salary in **INR & USD**
- Supports **annual** and **monthly** estimates
- Smart **error handling** (e.g. experience > age, invalid ranges)
- **Responsive, modern UI** with color themes and 3D-style visuals
- **RandomForest-based ML model** trained with structured preprocessing

---

## 📂 Project Structure

```
Employee-Salary-Prediction/
├── app.py                     # Streamlit application
├── Employee_Salary_Prediction.ipynb  # Jupyter notebook for model training
├── SalaryData.csv             # Dataset
├── best_regression_model.pkl  # Trained pipeline (with preprocessing)
├── requirements.txt           # Project dependencies
├── LICENSE                    # MIT License
└── README.md                  # Project overview (this file)
```

---

## 🚀 Getting Started (Run Locally)

1. **Clone the repository**
   ```bash
   git clone https://github.com/AdityaDimri04/Employee_Salary_Prediction.git
   cd Employee_Salary_Prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 🧠 Model Overview

- **Preprocessing:**
  - StandardScaler for numerical features (`Age`, `Years of Experience`)
  - OneHotEncoder for categorical features (e.g. `Gender`, `Job Title`, `City Tier`)
- **Model:**
  - RandomForestRegressor (selected based on R², MAE, RMSE)
- **Saved With:**
  - `joblib.dump()` — includes both preprocessing and model pipeline

---

## 🎯 How to Use

1. Enter employee details in the sidebar (age, gender, job, experience, etc.)
2. Click **"🚀 Estimate Salary"**
3. View estimated **Annual and Monthly Salary** in **INR & USD**

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## ⚠️ Disclaimer

This model is trained on a specific dataset. Predictions are approximate and may not reflect real-world salary distributions across industries or locations.
