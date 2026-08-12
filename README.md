# 🏭 AI-Powered Industrial Safety Intelligence for Zero-Harm Operations

> **An AI-driven industrial safety intelligence system for proactive hazard detection, predictive risk analysis, and emergency response.**

This project combines **Computer Vision, Machine Learning, IoT sensor analytics, Digital Permit Intelligence, Worker Shift Analysis, and Multi-Agent Risk Coordination** to create a unified industrial safety monitoring system.

The objective is to move from **reactive safety management** to **proactive risk detection** by identifying multiple safety hazards and combining them into a single overall risk assessment.

---

## 🎯 Problem Statement

Industrial environments involve multiple sources of risk, including:

* Workers not wearing required PPE
* Machine failures
* Fire and smoke hazards
* Unsafe work permits
* Excessive working hours and fatigue
* Multiple hazards occurring simultaneously

Traditional safety systems often monitor these factors separately.

This project addresses the problem by bringing multiple safety intelligence modules together and generating a **compound risk score** with corresponding safety recommendations.

---

## 💡 Solution

The system collects safety information from different sources and processes them through specialized AI/ML modules.

```text
                INDUSTRIAL ENVIRONMENT
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
       CCTV          Machine Data     IoT Sensors
        │                │                │
        ▼                ▼                ▼
 Helmet Detection   Machine Failure   Fire Detection
    YOLO11n         Random Forest     Random Forest
        │                │                │
        └────────────────┼────────────────┘
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
       Permit Intelligence    Shift Intelligence
              │                     │
              └──────────┬──────────┘
                         ▼
                 Risk Coordinator
                         │
                         ▼
                 Compound Risk Engine
                         │
                         ▼
                 Overall Risk Score
                         │
            ┌────────────┼────────────┐
            ▼            ▼            ▼
          SAFE         HIGH       CRITICAL
                         │
                         ▼
                  Emergency Action
```

---

## ✨ Key Features

### 🪖 1. AI-Based Helmet Detection

Uses a trained **YOLO11n object-detection model** to analyze camera/webcam frames and identify:

* Person
* Helmet
* Head

The system can count detected persons, helmets, and heads and provide annotated video output.

The helmet model is trained using a hard-hat detection dataset.

---

### 🔥 2. Fire Detection

A **Random Forest Classifier** is trained using IoT smoke/fire sensor data.

The model analyzes environmental parameters such as:

* Temperature
* Humidity
* TVOC
* eCO2
* Gas-related sensor readings
* Pressure
* PM1.0
* PM2.5
* Particle counts

The output determines whether a potential fire condition has been detected.

```text
Sensor Data
     ↓
Machine Learning Model
     ↓
Fire Prediction
   /       \
 FIRE     SAFE
```

---

### ⚙️ 3. Predictive Machine Failure Detection

A Random Forest model is trained using machine operating parameters such as:

* Machine Type
* Air Temperature
* Process Temperature
* Rotational Speed
* Torque
* Tool Wear

The model predicts whether a machine failure is likely.

```text
Machine Parameters
        ↓
Random Forest
        ↓
Failure Prediction
     /          \
Failure       Safe
```

This module supports **predictive maintenance** by identifying potential machine problems before they become larger safety risks.

---

### 📋 4. Digital Permit Intelligence

The Permit Intelligence module analyzes active work permits and environmental gas levels.

Risk levels are evaluated based on gas concentration:

```text
Gas Level < 60
      ↓
    SAFE

Gas Level 60–79
      ↓
  HIGH RISK
      ↓
Safety Officer Approval

Gas Level ≥ 80
      ↓
CRITICAL ALERT
      ↓
Stop Work Immediately
```

The module considers:

* Worker
* Work area
* Work type
* Permit status
* Gas level

---

### 👷 5. Worker Shift Intelligence

The Shift Intelligence module evaluates worker-related safety conditions.

The current risk calculation considers:

* Hours worked
* Helmet compliance
* Machine status

This helps identify situations where long working hours, PPE violations, or unsafe machine conditions may increase worker risk.

---

### 🤖 6. Multi-Agent Risk Coordination

The project includes separate safety agents for:

```text
Helmet Agent
Fire Agent
Machine Agent
Permit Agent
Shift Agent
```

A **Risk Coordinator** collects the outputs from these agents and combines them into a unified safety assessment.

```text
Helmet Agent ─────┐
Fire Agent ───────┤
Machine Agent ────┤
Permit Agent ─────┼──► Risk Coordinator
Shift Agent ──────┘
                         │
                         ▼
                  Overall Risk Score
```

This architecture makes it possible to extend the system with additional specialized safety agents in the future.

---

## 🧮 Compound Risk Engine

The system does not only evaluate individual hazards.

It also considers **combined hazards**.

For example:

```text
Missing Helmet + Machine Failure
            ↓
      Additional Risk
```

and:

```text
Fire + Unsafe Permit
            ↓
      Additional Risk
```

The current backend combines the following factors:

* Helmet compliance
* Machine failure
* Fire detection
* Permit risk
* Worker shift risk

The result is converted into a safety level:

```text
SAFE
  ↓
MEDIUM
  ↓
HIGH
  ↓
CRITICAL
```

---

## 🚨 Emergency Response

After calculating the overall risk level, the system generates a recommended response.

### 🔴 CRITICAL

**Immediate Plant Evacuation Required**

### 🟠 HIGH

**Notify Safety Supervisor**

### 🟢 SAFE

**Continue Normal Monitoring**

This creates a simple decision pipeline:

```text
Hazard Detection
       ↓
Risk Calculation
       ↓
Risk Classification
       ↓
Recommended Action
```

---

## 🌐 Backend & API

The backend is implemented using **Flask**.

Important API endpoints include:

```text
GET /
```

Checks whether the Industrial Safety AI backend is running.

```text
GET /demo
```

Generates a demonstration safety scenario and returns the calculated risk information.

```text
POST /predict
```

Accepts safety parameters and calculates the overall risk score and risk level.

```text
POST /ask_ai
```

Provides safety-oriented responses for questions related to risk, helmets, fire, and machine health.

```text
GET /video_feed
```

Streams the processed camera feed with object-detection results.

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │   Data Sources      │
                    └──────────┬──────────┘
                               │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
            ▼                  ▼                  ▼
        CCTV Data         Machine Data       IoT Sensor Data
            │                  │                  │
            ▼                  ▼                  ▼
        YOLO Model       ML Prediction       Fire Model
            │                  │                  │
            └──────────────────┼──────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │ Safety Intelligence │
                    │       Agents        │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │  Risk Coordinator   │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │ Compound Risk Engine│
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │ Overall Risk Score  │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                ▼              ▼              ▼
              SAFE           HIGH          CRITICAL
                │              │              │
                ▼              ▼              ▼
            Monitor        Notify        Emergency
                          Supervisor       Action
```

---

## 🛠️ Technology Stack

### Artificial Intelligence & Machine Learning

* Python
* YOLO11
* Computer Vision
* Random Forest
* Scikit-learn
* Pandas
* Joblib

### Computer Vision

* OpenCV
* Ultralytics YOLO
* Real-time webcam processing

### Backend

* Flask
* Flask-CORS
* REST API

### Frontend

* React
* Vite
* JavaScript

### Data & Analytics

* Pandas
* CSV datasets
* IoT sensor data
* Predictive maintenance data

---

## 📂 Project Structure

```text
AI-Powered-Industrial-Safety-Intelligence-for-Zero-Harm-Operations/
│
├── agent.py
├── agent_controller.py
├── app.py
├── camera.py
├── webcam.py
│
├── train.py
├── train_machine.py
├── predict_machine.py
├── train_fire.py
├── predict_fire.py
│
├── permit_check.py
├── shift_agent.py
│
├── check_dataset.py
├── detect.py
│
├── machine_model.pkl
├── fire_model.pkl
├── type_encoder.pkl
│
├── yolo11n.pt
│
├── package.json
├── package-lock.json
├── vite.config.js
├── index.html
│
└── README.md
```

---

## 🔄 End-to-End Workflow

```text
1. Collect Safety Data
          ↓
2. Process CCTV / Machine / IoT / Permit / Shift Data
          ↓
3. Run Specialized AI/ML Modules
          ↓
4. Generate Individual Risk Indicators
          ↓
5. Combine Results Through Risk Coordinator
          ↓
6. Calculate Compound Risk Score
          ↓
7. Classify Safety Level
          ↓
8. Generate Recommended Emergency Action
```

---

## 🧪 Model Training

### Helmet Detection

The YOLO11n model is trained for object detection using the hard-hat dataset.

Training configuration includes:

```text
Model       : YOLO11n
Epochs      : 50
Image Size  : 640
Batch Size  : 8
```

### Machine Failure Model

A Random Forest Classifier is trained using machine operating parameters and evaluated using:

* Accuracy
* Classification Report
* Confusion Matrix

### Fire Detection Model

A Random Forest Classifier is trained using environmental and smoke-sensor features and evaluated using classification metrics.

---

## 📊 Risk Levels

The system converts the calculated risk score into four categories:

```text
🟢 SAFE
Low overall risk

🟡 MEDIUM
Potential safety concern requiring monitoring

🟠 HIGH
Immediate safety attention required

🔴 CRITICAL
Emergency action may be required
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/KhushiGarg22/AI-Powered-Industrial-Safety-Intelligence-for-Zero-Harm-Operations.git
cd AI-Powered-Industrial-Safety-Intelligence-for-Zero-Harm-Operations
```

### Install Python Dependencies

```bash
pip install flask flask-cors pandas numpy scikit-learn joblib opencv-python ultralytics
```

### Run the Flask Backend

```bash
python app.py
```

The backend runs on:

```text
http://127.0.0.1:5000
```

---

## 🧪 Running Individual Modules

### Train Machine Failure Model

```bash
python train_machine.py
```

### Predict Machine Failure

```bash
python predict_machine.py
```

### Train Fire Detection Model

```bash
python train_fire.py
```

### Predict Fire Risk

```bash
python predict_fire.py
```

### Run Permit Intelligence

```bash
python permit_check.py
```

### Run Shift Intelligence

```bash
python shift_agent.py
```

### Train Helmet Detection Model

```bash
python train.py
```

### Run Webcam Detection

```bash
python webcam.py
```

---

## 🎯 Use Cases

The system can be adapted for environments such as:

* Manufacturing plants
* Construction sites
* Chemical industries
* Warehouses
* Power plants
* Industrial maintenance environments
* High-risk work areas

---

## 🔮 Future Scope

The current project is a prototype that can be extended into a production-grade industrial safety platform.

Possible improvements include:

* Real-time IoT sensor integration
* Live SCADA integration
* GPS/GIS-based safety heatmaps
* Worker location tracking
* Real-time emergency notifications
* SMS/Email alerts
* Automated incident reports
* Database-backed historical analytics
* More advanced predictive-maintenance models
* LLM-based safety assistant
* RAG-based industrial safety knowledge system
* Role-based admin and safety dashboards
* Cloud deployment
* Edge AI deployment for low-latency detection

---

## 🌟 Key Highlights

* 🪖 Real-time PPE / Helmet Detection
* 🔥 IoT-Based Fire Prediction
* ⚙️ Predictive Machine Failure Detection
* 📋 Digital Permit Risk Analysis
* 👷 Worker Shift & Fatigue Risk Analysis
* 🤖 Multi-Agent Safety Coordination
* 🧮 Compound Risk Scoring
* 🚨 Emergency Response Recommendations
* 📹 Real-Time Camera Processing
* 🌐 Flask REST API
* ⚛️ React + Vite Frontend

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

* Computer Vision
* Object Detection using YOLO
* Machine Learning
* Predictive Maintenance
* IoT Sensor Data Analysis
* Risk Scoring
* Multi-Agent System Design
* Flask API Development
* React/Vite Application Development
* Real-Time Video Processing
* Data Preprocessing
* Model Training and Evaluation
* Integrating multiple AI modules into one application

---

## 📌 Project Status

**Current Status: Prototype / Proof of Concept**

The project demonstrates the architecture and working of an AI-powered industrial safety intelligence platform. Some components currently use simulated/demo inputs, while the individual ML and computer-vision modules demonstrate the intended detection and prediction workflow.

The architecture is designed to be extended with real industrial IoT, SCADA, geospatial, and notification integrations.

---

## 👩‍💻 Developed By

**Khushi Garg**

AI/ML • Computer Vision • Machine Learning • Full-Stack Development

