import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt
import os

# Create output folder if it doesn't exist
os.makedirs("outputs/shap", exist_ok=True)

# Load model
model = joblib.load("models/diabetes_model.pkl")

# Load processed dataset
df = pd.read_csv("data/processed/diabetes_processed.csv")

X = df.drop("diabetes", axis=1)

# Create explainer
explainer = shap.Explainer(model)

# Explain first 100 patients (faster than all 100,000)
shap_values = explainer(X.iloc[:100])

# -------------------------
# Summary Plot
# -------------------------
shap.plots.beeswarm(shap_values[:, :, 1], show=False)

plt.tight_layout()
plt.savefig("outputs/shap/summary_plot.png")
plt.close()

print("Summary plot saved!")