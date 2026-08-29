import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"


def generate_explanation(patient_data, prediction_result):
    """
    Generate a natural language explanation using the local Phi-3 model.
    """

    prompt = f"""
You are an AI clinical assistant.

Patient Information:
- Age: {patient_data['age']}
- Gender: {patient_data['gender']}
- BMI: {patient_data['bmi']}
- HbA1c: {patient_data['HbA1c_level']}
- Blood Glucose: {patient_data['blood_glucose_level']}
- Hypertension: {patient_data['hypertension']}
- Heart Disease: {patient_data['heart_disease']}

Prediction:
{prediction_result['final_decision']}

Probability:
{prediction_result['probability']:.2f}

Rule-based Reasons:
{chr(10).join(prediction_result['reasons'])}

Provide:
1. A concise explanation.
2. Important contributing factors.
3. A general recommendation.
Do not provide a medical diagnosis.
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()

        return response.json()["response"]

    except Exception as e:
        return f"LLM Error: {str(e)}"