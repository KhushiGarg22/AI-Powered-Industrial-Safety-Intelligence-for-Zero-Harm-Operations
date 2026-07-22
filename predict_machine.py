import joblib
import pandas as pd

# Load trained model
model = joblib.load("../models/machine_model.pkl")
encoder = joblib.load("../models/type_encoder.pkl")

print("========== Machine Failure Prediction ==========\n")

machine_type = input("Machine Type (L/M/H): ").upper()

air_temp = float(input("Air Temperature (K): "))
process_temp = float(input("Process Temperature (K): "))
rpm = float(input("Rotational Speed (rpm): "))
torque = float(input("Torque (Nm): "))
tool_wear = float(input("Tool Wear (min): "))

# Encode machine type
machine_type = encoder.transform([machine_type])[0]

sample = pd.DataFrame({
    "Type": [machine_type],
    "Air temperature [K]": [air_temp],
    "Process temperature [K]": [process_temp],
    "Rotational speed [rpm]": [rpm],
    "Torque [Nm]": [torque],
    "Tool wear [min]": [tool_wear]
})

prediction = model.predict(sample)[0]

print("\n=================================")

if prediction == 1:
    print("⚠️ ALERT : Machine Failure Predicted")
else:
    print("✅ Machine is Safe")

print("=================================")