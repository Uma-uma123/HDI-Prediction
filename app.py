from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model/model.pkl")
encoder = joblib.load("model/label_encoder.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    life = float(request.form["life"])
    expected = float(request.form["expected"])
    mean = float(request.form["mean"])
    income = float(request.form["income"])

    features = np.array([[life, expected, mean, income]])

    prediction = model.predict(features)

    result = encoder.inverse_transform(prediction)

    return render_template("result.html", prediction=result[0])

if __name__ == "__main__":
    app.run(debug=True)