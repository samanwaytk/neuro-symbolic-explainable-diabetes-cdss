import joblib
import pandas as pd
import shap

# Load trained model
model = joblib.load("models/diabetes_model.pkl")

# Load processed dataset
df = pd.read_csv("data/processed/diabetes_processed.csv")

# Separate features
X = df.drop("diabetes", axis=1)

# Create SHAP Explainer
explainer = shap.Explainer(model)

# Explain first patient
shap_values = explainer(X.iloc[[0]])

print("=" * 60)
print("PATIENT EXPLANATION")
print("=" * 60)

prediction = model.predict(X.iloc[[0]])[0]

print(f"\nPrediction: {prediction}")

# SHAP values for diabetes class (class 1)
values = shap_values.values[0, :, 1]

print("\nFeature Contributions\n")

for feature, value in zip(X.columns, values):

    direction = (
        "Increased Diabetes Risk"
        if value > 0
        else "Reduced Diabetes Risk"
    )

    print(f"{feature:22} {value:10.4f}   {direction}")