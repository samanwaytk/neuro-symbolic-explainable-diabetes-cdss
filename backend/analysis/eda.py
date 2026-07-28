import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/diabetes_prediction_dataset.csv")

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

# First 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns.tolist())

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics
print("\nSummary Statistics:")
print(df.describe())

# Target distribution
print("\nDiabetes Distribution:")
print(df["diabetes"].value_counts())