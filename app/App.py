# App
from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load("C:\\Users\\Abhimantr Singh\\Downloads\\codecplus\\predictive-maintenance-system\\models\\rf_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            # Extract float values from form
            input_data = [float(x) for x in request.form.values()]
            pred = model.predict([input_data])[0]
            prediction = "Failure" if pred == 1 else "No Failure"
        except:
            prediction = "Invalid input. Please enter numeric values only."
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
