from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load your trained Random Forest model
model = pickle.load(open("teja.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Only integers accepted
    study = int(request.form["study"])
    social = int(request.form["social"])
    attendance = int(request.form["attendance"])
    sleep = int(request.form["sleep"])

    # Prediction
    prediction = model.predict([[study, social, attendance, sleep]])

    # Round to 2 decimals
    return render_template("index.html", result=round(prediction[0], 2))

if _name_ == "_main_":
    app.run(debug=True)