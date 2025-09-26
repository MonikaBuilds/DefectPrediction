from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load model
with open(r"../model/defect_model.pkl", "rb") as f:
    model = pickle.load(f)

scaler = StandardScaler()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Convert inputs to floats
        features = [float(x) for x in request.form.values()]
    except ValueError:
        return render_template("index.html", prediction_text="Error: Please enter all numeric values.")

    # Scale features and predict
    features_scaled = scaler.fit_transform([features])
    prediction = model.predict(features_scaled)
    result = "Defective" if prediction[0] == 1 else "Clean"
    return render_template("index.html", prediction_text=f"Module is {result}")


if __name__ == "__main__":
    app.run(debug=True)
