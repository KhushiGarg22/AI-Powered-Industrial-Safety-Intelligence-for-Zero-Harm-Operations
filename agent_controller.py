import random

class HelmetAgent:
    def analyze(self):
        return {
            "helmet": random.choice([0, 1])
        }


class FireAgent:
    def analyze(self):
        return {
            "fire": random.choice([0, 1])
        }


class MachineAgent:
    def analyze(self):
        return {
            "machine_failure": random.choice([0, 1])
        }


class PermitAgent:
    def analyze(self):
        return {
            "permit_risk": random.choice(["SAFE", "HIGH"])
        }


class ShiftAgent:
    def analyze(self):
        return {
            "shift_risk": random.choice(["SAFE", "HIGH"])
        }


class RiskCoordinator:

    def __init__(self):

        self.helmet = HelmetAgent()

        self.fire = FireAgent()

        self.machine = MachineAgent()

        self.permit = PermitAgent()

        self.shift = ShiftAgent()

    def analyze(self):

        result = {}

        result.update(self.helmet.analyze())
        result.update(self.fire.analyze())
        result.update(self.machine.analyze())
        result.update(self.permit.analyze())
        result.update(self.shift.analyze())

        risk = 0

        if result["helmet"] == 0:
            risk += 20

        if result["fire"] == 1:
            risk += 30

        if result["machine_failure"] == 1:
            risk += 30

        if result["permit_risk"] == "HIGH":
            risk += 10

        if result["shift_risk"] == "HIGH":
            risk += 10

        result["overall_risk"] = risk

        if risk >= 80:
            result["status"] = "🔴 CRITICAL"

        elif risk >= 50:
            result["status"] = "🟠 HIGH"

        elif risk >= 20:
            result["status"] = "🟡 MEDIUM"

        else:
            result["status"] = "🟢 SAFE"

        return result


coordinator = RiskCoordinator()

report = coordinator.analyze()

print("\n========== MULTI AGENT REPORT ==========\n")

for key, value in report.items():
    print(f"{key} : {value}")