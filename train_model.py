import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv(r"C:\Users\kanna\OneDrive\Desktop\Health Prediction Application\diabetes_prediction_dataset.csv")  # your file name

print("Columns:", df.columns)

# -------------------------
# FIX CATEGORICAL DATA
# -------------------------

df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})

le = LabelEncoder()
df['smoking_history'] = le.fit_transform(df['smoking_history'])

# -------------------------
# SPLIT DATA
# -------------------------

target_col = 'diabetes'   # from your dataset

X = df.drop(target_col, axis=1)
y = df[target_col]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained successfully!")