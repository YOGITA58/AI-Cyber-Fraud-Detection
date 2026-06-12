import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("PhishingData.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Remove index column
df = df.drop("index", axis=1)

# Features and labels
X = df.drop("Result", axis=1)
y = df["Result"]

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Save model
with open("model/phishing_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")