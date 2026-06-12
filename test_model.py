import pickle

with open("model/phishing_model.pkl", "rb") as file:
    model = pickle.load(file)

print("Model loaded successfully!") 