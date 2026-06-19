from feature_extractor import extract_features
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
with open("model/phishing_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def home():
    

    analysis = {}
    prediction = ""
    confidence = ""

    if request.method == "POST":

        url = request.form["url"]

        features, analysis = extract_features(url)

        features = [features]

        result = model.predict(features)

        confidence = round(
            max(model.predict_proba(features)[0]) * 100,
            2
        )

        if result[0] == -1:
            prediction = "🚨 Phishing Website"
        else:
            prediction = "✅ Legitimate Website"

    return render_template(
    "index.html",
    prediction=prediction,
    confidence=confidence,
    analysis=analysis
)
if __name__ == "__main__":
    app.run(debug=True)