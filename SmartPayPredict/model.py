
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load data
df = pd.read_csv("employee_data.csv")

# Features and target
X = df.drop(columns=["Name", "Salary"])
y = df["Salary"]

# Preprocessing
categorical_features = ["Education", "Role", "City_Tier", "Skills", "Certifications", "Company_Size"]
preprocessor = ColumnTransformer(transformers=[
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
])

# Models
xgb_model = xgb.XGBRegressor()
rf_model = RandomForestRegressor()
ridge_model = Ridge()

# Pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", ridge_model)
])

# Train and save
model.fit(X, y)
joblib.dump(model, "salary_predictor.pkl")
