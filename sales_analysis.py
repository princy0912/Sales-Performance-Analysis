import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("sales_data.csv")

print("First 5 rows:")
print(df.head())

print("\nColumns in dataset:")
print(df.columns)

print("\nDataset shape (rows, columns):")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())