import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt
import os

# Create output folder
os.makedirs("outputs/shap", exist_ok=True)

# Load trained model
model = joblib.load("models/diabetes_model.pkl")

# Load processed data
df = pd.read_csv("data/processed/diabetes_processed.csv")

# Features only
X = df.drop("diabetes", axis=1)

# Create SHAP explainer
explainer = shap.Explainer(model)

# Explain first patient
shap_values = explainer(X.iloc[[0]])

# Waterfall plot for Diabetes class (class 1)
shap.plots.waterfall(shap_values[0, :, 1], show=False)

plt.tight_layout()
plt.savefig("outputs/shap/waterfall_plot.png", dpi=300)
plt.close()

print("Waterfall plot saved successfully!")