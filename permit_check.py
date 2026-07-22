import pandas as pd

# Load permit data
df = pd.read_csv("../datasets/permit_logs.csv")

print("\n========== DIGITAL PERMIT INTELLIGENCE ==========\n")

for _, row in df.iterrows():

    if row["Status"] != "Active":
        continue

    gas = row["Gas_Level"]

    work = row["Work_Type"]

    area = row["Area"]

    worker = row["Worker"]

    if gas >= 80:

        print("🚨 CRITICAL ALERT")
        print(f"Worker : {worker}")
        print(f"Area   : {area}")
        print(f"Permit : {work}")
        print(f"Gas    : {gas}")
        print("Recommendation : Stop Work Immediately\n")

    elif gas >= 60:

        print("⚠ HIGH RISK")

        print(f"Worker : {worker}")

        print(f"Area   : {area}")

        print(f"Permit : {work}")

        print(f"Gas    : {gas}")

        print("Recommendation : Safety Officer Approval Required\n")

    else:

        print(f"✅ {worker} ({work}) -> SAFE")