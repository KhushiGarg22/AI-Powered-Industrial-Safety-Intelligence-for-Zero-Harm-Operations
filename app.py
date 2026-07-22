from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from camera import generate_frames
import random

app = Flask(__name__)
CORS(app)


# ----------------------------------------------------
# Compound Risk Engine
# ----------------------------------------------------

def calculate_risk(helmet, machine, fire, permit, shift):

    score = 0
    reasons = []

    if helmet == 0:
        score += 30
        reasons.append("Helmet Missing")

    if machine == 1:
        score += 25
        reasons.append("Machine Failure")

    if fire == 1:
        score += 30
        reasons.append("Fire Detected")

    if permit == "HIGH":
        score += 10
        reasons.append("Unsafe Permit")

    if shift == "HIGH":
        score += 5
        reasons.append("Worker Fatigue Risk")

    # Compound Risk
    if helmet == 0 and machine == 1:
        score += 15
        reasons.append("Worker Near Unsafe Machine")

    if fire == 1 and permit == "HIGH":
        score += 20
        reasons.append("Hot Work During Fire Risk")

    if score < 30:
        level = "SAFE"

    elif score < 60:
        level = "MEDIUM"

    elif score < 90:
        level = "HIGH"

    else:
        level = "CRITICAL"

    return score, level, reasons


# ----------------------------------------------------
# Emergency Orchestrator
# ----------------------------------------------------

def emergency_action(level):

    if level == "CRITICAL":

        return {

            "notify": True,

            "evacuate": True,

            "message": "🚨 Immediate Plant Evacuation Required"

        }

    elif level == "HIGH":

        return {

            "notify": True,

            "evacuate": False,

            "message": "⚠ Notify Safety Supervisor"

        }

    return {

        "notify": False,

        "evacuate": False,

        "message": "Plant Safe"

    }


# ----------------------------------------------------
# Home
# ----------------------------------------------------

@app.route("/")
def home():

    return jsonify({

        "message": "Industrial Safety AI Running"

    })


# ----------------------------------------------------
# Demo
# ----------------------------------------------------

@app.route("/demo")
def demo():

    helmet = random.randint(0, 1)

    machine = random.randint(0, 1)

    fire = random.randint(0, 1)

    permit = random.choice([

        "SAFE",

        "HIGH"

    ])

    shift = random.choice([

        "LOW",

        "MEDIUM",

        "HIGH"

    ])

    score, level, reasons = calculate_risk(

        helmet,

        machine,

        fire,

        permit,

        shift

    )

    emergency = emergency_action(level)

    return jsonify({

        "helmet": helmet,

        "machine_failure": machine,

        "fire": fire,

        "permit": permit,

        "shift": shift,

        "risk_score": score,

        "risk_level": level,

        "reasons": reasons,

        "emergency": emergency,

        "workers": 26,

        "machines": 15,

        "incidents": random.randint(1,5),

        "safety_score": max(100-score,0)

    })


# ----------------------------------------------------
# Predict
# ----------------------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    score, level, reasons = calculate_risk(

        data["helmet"],

        data["machine_failure"],

        data["fire"],

        data["permit"],

        data["shift"]

    )

    emergency = emergency_action(level)

    return jsonify({

        "risk_score": score,

        "risk_level": level,

        "reasons": reasons,

        "emergency": emergency

    })


# ----------------------------------------------------
# AI Assistant
# ----------------------------------------------------

@app.route("/ask_ai", methods=["POST"])
def ask_ai():

    data = request.get_json()

    question = data.get("question","").lower()

    if "risk" in question:

        answer = """
Current Risk Analysis

Reason
• Helmet Missing
• Fire Risk
• Unsafe Permit

Recommendation
• Stop Work
• Evacuate Area
• Notify Supervisor
"""

    elif "helmet" in question:

        answer = """
Helmet Compliance

Helmet violation detected.

Recommendation

Worker should wear PPE immediately.
"""

    elif "fire" in question:

        answer = """
Fire Risk

Smoke sensor active.

Recommendation

Activate fire suppression system.
"""

    elif "machine" in question:

        answer = """
Machine Health

High vibration detected.

Recommendation

Stop machine for inspection.
"""

    else:

        answer = """
Industrial Safety Assistant

System operating normally.

Continue monitoring all safety parameters.
"""

    return jsonify({

        "answer": answer

    })


# ----------------------------------------------------
# Camera
# ----------------------------------------------------

@app.route("/video_feed")
def video_feed():

    return Response(

        generate_frames(),

        mimetype="multipart/x-mixed-replace; boundary=frame"

    )


# ----------------------------------------------------
# Run
# ----------------------------------------------------

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=False,

        use_reloader=False,

        threaded=True

    )