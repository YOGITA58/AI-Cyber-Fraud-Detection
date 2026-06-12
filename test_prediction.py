import pickle
import pandas as pd

with open("model/phishing_model.pkl", "rb") as file:
    model = pickle.load(file)

df = pd.read_csv("PhishingData.csv")

df.columns = df.columns.str.strip()

df = df.drop("index", axis=1)

X = df.drop("Result", axis=1)

prediction = model.predict([X.iloc[0]])

print("Prediction:", prediction[0])
