from backend.services.hybrid_engine import hybrid_prediction

patient = {
    "gender": 0,
    "age": 60,
    "hypertension": 1,
    "heart_disease": 0,
    "smoking_history": 2,
    "bmi": 33,
    "HbA1c_level": 7.1,
    "blood_glucose_level": 180
}

result = hybrid_prediction(patient)

print(result)