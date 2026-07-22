import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ----------------------------
# Load Dataset
# ----------------------------
df = pd.read_csv("../datasets/ai4i2020.csv")

print("Dataset Loaded Successfully")
print(df.head())

# ----------------------------
# Encode Type Column
# ----------------------------
encoder = LabelEncoder()
df["Type"] = encoder.fit_transform(df["Type"])

# ----------------------------
# Features
# ----------------------------
X = df[
    [
        "Type",
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]",
    ]
]

# Target
y = df["Machine failure"]

# ----------------------------
# Split Dataset
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ----------------------------
# Train Model
# ----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ----------------------------
# Prediction
# ----------------------------
pred = model.predict(X_test)

# ----------------------------
# Accuracy
# ----------------------------
print("\nAccuracy :", accuracy_score(y_test, pred))

print("\nClassification Report\n")
print(classification_report(y_test, pred))

print("\nConfusion Matrix\n")
print(confusion_matrix(y_test, pred))

# ----------------------------
# Save Model
# ----------------------------
joblib.dump(model, "../models/machine_model.pkl")
joblib.dump(encoder, "../models/type_encoder.pkl")

print("\nMachine Failure Model Saved Successfully!")