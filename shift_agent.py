import pandas as pd

df = pd.read_csv("../datasets/shift_records.csv")

print("\n========== SHIFT INTELLIGENCE ==========\n")

for _, row in df.iterrows():

    risk = 0

    if row["Hours_Worked"] > 10:
        risk += 30

    if row["Helmet"] == "No":
        risk += 40

    if row["Machine_Status"] == "Failure":
        risk += 30

    if risk >= 80:

        print("🚨 HIGH RISK")

    elif risk >= 40:

        print("⚠ MEDIUM RISK")

    else:

        print("✅ SAFE")

    print(f"Worker : {row['Worker']}")
    print(f"Shift  : {row['Shift']}")
    print(f"Hours  : {row['Hours_Worked']}")
    print(f"Risk   : {risk}")
    print("--------------------------")