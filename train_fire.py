import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("../datasets/smoke_detection_iot.csv")

print("Dataset Loaded Successfully")

# Remove unnecessary columns
drop_cols = ["Unnamed: 0", "UTC"]

for col in drop_cols:
    if col in df.columns:
        df.drop(columns=col, inplace=True)

# Features
X = df.drop("Fire Alarm", axis=1)

# Target
y = df["Fire Alarm"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

print("\nAccuracy :", accuracy_score(y_test, pred))
print("\nClassification Report\n")
print(classification_report(y_test, pred))

# Save Model
joblib.dump(model, "../models/fire_model.pkl")

print("\nFire Prediction Model Saved Successfully!")