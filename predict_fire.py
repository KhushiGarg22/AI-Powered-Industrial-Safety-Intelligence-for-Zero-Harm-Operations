import joblib
import pandas as pd

model = joblib.load("../models/fire_model.pkl")

print("========== Fire Prediction ==========\n")

temperature = float(input("Temperature (C): "))
humidity = float(input("Humidity (%): "))
tvoc = float(input("TVOC (ppb): "))
eco2 = float(input("eCO2 (ppm): "))
raw_h2 = float(input("Raw H2: "))
raw_ethanol = float(input("Raw Ethanol: "))
pressure = float(input("Pressure (hPa): "))
pm1 = float(input("PM1.0: "))
pm25 = float(input("PM2.5: "))
nc05 = float(input("NC0.5: "))
nc10 = float(input("NC1.0: "))
nc25 = float(input("NC2.5: "))
cnt = float(input("CNT: "))

sample = pd.DataFrame({
    "Temperature[C]": [temperature],
    "Humidity[%]": [humidity],
    "TVOC[ppb]": [tvoc],
    "eCO2[ppm]": [eco2],
    "Raw H2": [raw_h2],
    "Raw Ethanol": [raw_ethanol],
    "Pressure[hPa]": [pressure],
    "PM1.0": [pm1],
    "PM2.5": [pm25],
    "NC0.5": [nc05],
    "NC1.0": [nc10],
    "NC2.5": [nc25],
    "CNT": [cnt]
})

prediction = model.predict(sample)[0]

print("\n==============================")

if prediction == 1:
    print("🔥 FIRE DETECTED")
else:
    print("✅ No Fire Detected")

print("==============================")