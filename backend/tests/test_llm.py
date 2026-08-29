from backend.services.llm_service import generate_explanation

patient = {
    "age": 55,
    "gender": "Male",
    "bmi": 31.4,
    "HbA1c_level": 7.1,
    "blood_glucose_level": 182,
    "hypertension": 1,
    "heart_disease": 0
}

prediction = {
    "final_decision": "High Diabetes Risk",
    "probability": 0.96,
    "reasons": [
        "BMI ≥ 30",
        "HbA1c ≥ 6.5",
        "Blood glucose ≥ 126"
    ]
}

print(generate_explanation(patient, prediction))