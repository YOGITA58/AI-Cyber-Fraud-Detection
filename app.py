from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
with open("model/phishing_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = ""
    confidence = ""

    if request.method == "POST":

        url_length = int(request.form["url_length"])
        ip_address = int(request.form["ip_address"])
        ssl_state = int(request.form["ssl_state"])
        age_domain = int(request.form["age_domain"])
        google_index = int(request.form["google_index"])

        features = [[
            ip_address,
            url_length,
            0, 0, 0, 0, 0,
            ssl_state,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            age_domain,
            0, 0, 0,
            google_index,
            0, 0
        ]]

        result = model.predict(features)

        confidence = round(
            max(model.predict_proba(features)[0]) * 100,
            2
        )

        if result[0] == -1:
            prediction = "<span style='color:red;'>🚨 Phishing Website</span>"
        else:
            prediction = "<span style='color:lime;'>✅ Legitimate Website</span>"

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run(debug=True)