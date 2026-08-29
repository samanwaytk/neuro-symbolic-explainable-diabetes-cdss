# Neuro-Symbolic XAI CDSS

An AI-based Clinical Decision Support System (CDSS) for diabetes risk assessment that combines Machine Learning, Symbolic Rule-Based Reasoning, SHAP Explainable AI, and an LLM-based clinical explanation layer.

## Overview

The system analyzes patient information and produces a diabetes risk assessment by combining:

- Machine Learning prediction
- Symbolic clinical rules
- Hybrid neuro-symbolic decision making
- SHAP-based explainability
- LLM-generated clinical explanation
- FastAPI backend
- React frontend

The goal is to provide not only a prediction, but also an understandable explanation of why the system reached that prediction.

## System Architecture

```text
Patient Information
        |
        v
   React Frontend
        |
        v
   FastAPI Backend
        |
        +-------------------+
        |                   |
        v                   v
   ML Prediction      Rule Engine
        |                   |
        +---------+---------+
                  |
                  v
          Hybrid Decision
                  |
          +-------+-------+
          |               |
          v               v
        SHAP             LLM
          |               |
          +-------+-------+
                  |
                  v
          Explainable Result
                  |
                  v
            React Frontend
            Main Components
1. Machine Learning

A trained diabetes classification model generates:

Diabetes prediction
Prediction probability
2. Symbolic Rule Engine

Clinical rules evaluate important patient measurements such as:

HbA1c
Blood glucose
BMI
Age

The rule engine provides explicit risk factors supporting the assessment.

3. Neuro-Symbolic Hybrid Engine

The system combines the ML prediction with symbolic reasoning.

The final decision considers both:

Statistical model prediction
Rule-based clinical risk

This makes the decision more interpretable than relying on the ML model alone.

4. SHAP Explainability

SHAP (SHapley Additive exPlanations) explains how individual patient features influenced the ML prediction.

The frontend displays:

Feature
SHAP contribution
Direction of influence

For example:

HbA1c        +0.837    Increased Diabetes Risk
Age          +0.017    Increased Diabetes Risk
BMI          +0.014    Increased Diabetes Risk
5. LLM Clinical Explanation

The LLM converts the prediction and identified risk factors into a human-readable clinical explanation.

The explanation is intended to make the system output easier to understand.

Technology Stack
Backend
Python
FastAPI
Pandas
Scikit-learn
SHAP
Joblib
Frontend
React
Vite
JavaScript
HTML
CSS
Axios
AI
Machine Learning
Symbolic Rule-Based Reasoning
SHAP Explainable AI
Large Language Model
Project Structure
neuro-symbolic-xai-cdss/
│
├── backend/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── explainability/
│   ├── preprocessing/
│   ├── schemas/
│   ├── services/
│   ├── tests/
│   └── main.py
│
├── data/
│
├── frontend/
│   ├── public/
│   └── src/
│       ├── components/
│       ├── assets/
│       ├── App.jsx
│       └── main.jsx
│
├── outputs/
│   └── shap/
│
├── models/
│   └── diabetes_model.pkl
│
├── requirements.txt
├── .gitignore
└── README.md
Running the Backend

Create and activate the Python virtual environment:

python -m venv venv
.\venv\Scripts\Activate.ps1

Install the dependencies:

pip install -r requirements.txt

Start FastAPI:

uvicorn backend.main:app --reload

The API will be available at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs
Running the Frontend

Open a second terminal and move into the frontend directory:

cd frontend

Install frontend dependencies:

npm install

Start the Vite development server:

npm run dev

The frontend will normally be available at:

http://localhost:5173
Example

Example patient:

Age:              55
BMI:               31.4
HbA1c:              7.2
Blood Glucose:    185
Hypertension:       Yes
Heart Disease:      No

Example system output:

Final Decision: High Diabetes Risk
ML Prediction: 1
Probability: ~98%
Rule Risk: High

The system additionally provides symbolic risk factors, SHAP feature contributions, and an LLM-generated explanation.

Model File

The trained model is intentionally excluded from Git because the model file is approximately 155 MB and exceeds GitHub's standard 100 MB per-file limit.

The expected model location is:

models/diabetes_model.pkl
Disclaimer

This project is an academic/research prototype and is not intended to replace professional medical diagnosis, treatment, or clinical judgment.

Clinical decisions should be made by qualified healthcare professionals using appropriate clinical information and current medical guidelines.

Author

Sam