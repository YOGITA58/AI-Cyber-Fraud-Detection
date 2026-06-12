print("Step 1")

import pickle
print("Step 2")

with open("model/phishing_model.pkl", "rb") as file:
    print("Step 3")
    model = pickle.load(file)

print("Step 4 - Model loaded successfully!")