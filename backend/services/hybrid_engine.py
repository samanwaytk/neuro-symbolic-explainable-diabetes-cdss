
import pandas as pd

from backend.services.rule_engine import evaluate_rules


from backend.core.model_loader import load_model

model = load_model()


def hybrid_prediction(patient_data):
    """
    Combines Machine Learning prediction
    with Symbolic Rule Engine.
    """

    # -------------------------
    # ML Prediction
    # -------------------------

    # Remove fields that are not model features
    model_input = patient_data.copy()
    model_input.pop("patient_name", None)

    df = pd.DataFrame([model_input])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    # -------------------------
    # Rule Engine
    # -------------------------

    rule_risk, reasons = evaluate_rules(
        age=patient_data["age"],
        bmi=patient_data["bmi"],
        glucose=patient_data["blood_glucose_level"],
        hba1c=patient_data["HbA1c_level"]
    )

    # -------------------------
    # Hybrid Decision
    # -------------------------

    if prediction == 1 and rule_risk == "High":
        final_decision = "High Diabetes Risk"

    elif prediction == 1:
        final_decision = "Moderate Diabetes Risk"

    elif rule_risk == "High":
        final_decision = "Needs Clinical Review"

    else:
        final_decision = "Low Diabetes Risk"

    return {
    "patient_data": patient_data,

    "ml_prediction": int(prediction),
    "probability": round(float(probability), 3),

    "rule_risk": rule_risk,
    "final_decision": final_decision,

    "reasons": reasons
}