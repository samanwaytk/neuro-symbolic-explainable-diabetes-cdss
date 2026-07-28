import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/raw/diabetes_prediction_dataset.csv")

print("Original Shape:", df.shape)

# Create encoders
gender_encoder = LabelEncoder()
smoking_encoder = LabelEncoder()

# Encode categorical columns
df["gender"] = gender_encoder.fit_transform(df["gender"])
df["smoking_history"] = smoking_encoder.fit_transform(df["smoking_history"])

print("\nEncoding Complete!")
print(df.head())

# Save processed dataset
df.to_csv("data/processed/diabetes_processed.csv", index=False)

# Save encoders
joblib.dump(gender_encoder, "models/gender_encoder.pkl")
joblib.dump(smoking_encoder, "models/smoking_encoder.pkl")

print("\nProcessed dataset saved successfully!")
print("Gender encoder saved successfully!")
print("Smoking encoder saved successfully!")