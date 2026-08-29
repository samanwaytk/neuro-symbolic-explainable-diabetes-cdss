import shap
import pandas as pd


def generate_shap_explanation(model, patient_df):

    explainer = shap.Explainer(model)

    shap_values = explainer(patient_df)


    values = shap_values.values[0]


    # For binary classification
    if len(values.shape) == 2:
        values = values[:, 1]


    explanation = {}


    for feature, value in zip(
        patient_df.columns,
        values
    ):

        explanation[feature] = {
            "impact": float(value),

            "direction":
                "Increased Diabetes Risk"
                if value > 0
                else "Reduced Diabetes Risk"
        }


    return explanation