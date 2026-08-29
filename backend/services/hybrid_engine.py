
import pandas as pd

from backend.services.rule_engine import evaluate_rules
from backend.services.llm_service import generate_explanation
from backend.explainability.shap_explainer import generate_shap_explanation


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

    shap_explanation = generate_shap_explanation(
        model,
        df
    )

    prediction = int(model.predict(df)[0])

    probability = float(model.predict_proba(df)[0][1])

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


    prediction_result = {
    "final_decision": final_decision,
    "probability": probability,
    "reasons": reasons
    }

    llm_explanation = generate_explanation(
    patient_data,
    prediction_result
    )
    print(shap_explanation)
   
    return {
    "patient_data": patient_data,
    "ml_prediction": prediction,
    "probability": probability,
    "rule_risk": rule_risk,
    "final_decision": final_decision,
    "reasons": reasons,
    "llm_explanation": llm_explanation,
    "shap_explanation": shap_explanation
}
    