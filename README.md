# 💼 SmartPayPredict

### A Machine Learning System for Employee Salary Forecasting

SmartPayPredict is an intelligent salary prediction web application built using Python, Streamlit, and Machine Learning. It predicts an employee's salary based on job role, education, experience, city tier, skills, certifications, and company size.

🔗 **Live Demo:** [https://smartpaypredict0.streamlit.app/](https://smartpaypredict0.streamlit.app/)



## 📌 Features

- Predict employee salary based on:
  - ✅ Experience
  - ✅ Education Level
  - ✅ Job Role
  - ✅ City Tier
  - ✅ Technical Skills
  - ✅ Certifications
  - ✅ Company Size
- Clean and responsive Streamlit UI
- Real-time salary prediction
- Pre-trained ML model with high accuracy
- Suitable for HR analytics, employee planning, and compensation benchmarking


## 🧠 Machine Learning Model

- **Algorithm Used:** Ridge Regression (can be extended to ensemble models like XGBoost or Random Forest)
- **Preprocessing:** One-hot encoding of categorical features
- **Pipeline:** Scikit-learn pipeline for preprocessing + regression
- **Trained model file:** `salary_predictor.pkl`

---

## 📂 Project Structure
```bash

SmartPayPredict/
│
├── app.py                  # Streamlit frontend
├── model.py                # Model training script
├── salary_predictor.pkl    # Pre-trained ML model
├── employee_data.csv       # Sample training dataset
├── requirements.txt        # Python dependencies
```
## 🚀 How to Run Locally

1. Clone the repo

```bash
git clone https://github.com/Pratikkamble123/SmartPayPredict.git
cd SmartPayPredict
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Train the model (optional if `salary_predictor.pkl` already exists)

```bash
python model.py
```

4. Launch the web app

```bash
streamlit run app.py
```

---

## 📊 Sample Input Fields

| Field           | Type         | Example              |
| --------------- | ------------ | -------------------- |
| Experience      | Numeric      | 3                    |
| Education Level | Dropdown     | Bachelors, Masters   |
| Role            | Dropdown     | Data Scientist       |
| City Tier       | Dropdown     | 1, 2, 3              |
| Skills          | Multi-select | Python, SQL          |
| Certifications  | Yes/No       | Yes                  |
| Company Size    | Dropdown     | Small, Medium, Large |

---

## 👨‍💻 Developed By

**Pratik Kamble**
🎓 IBM Internship Project
🌐 GitHub: [Pratikkamble123](https://github.com/Pratikkamble123)

---

## 📬 Feedback & Contributions

Feel free to open issues or contribute enhancements via pull requests.

---

⭐️ Don't forget to star this repository if you found it helpful!

```

