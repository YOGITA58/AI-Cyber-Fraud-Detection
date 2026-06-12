import pandas as pd

df = pd.read_csv("phishingData.csv")

print("First 5 Rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nDataset Info:")
print(df.info())
print("\nResult Distribution:")
print(df["Result"].value_counts())
