from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained ML model (make sure defect_model.pkl exists in the app folder)
model = pickle.load(open("defect_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        try:
            # Get values from form
            loc = int(request.form["loc"])
            complexity = int(request.form["complexity"])
            halstead = int(request.form["halstead"])

            # Convert to numpy array
            features = np.array([[loc, complexity, halstead]])

            # Predict
            prediction = model.predict(features)[0]
            result = "Defect Prone" if prediction == 1 else "Not Defect Prone"

            # Send back values + prediction
            return render_template(
                "index.html",
                prediction=result,
                loc=loc,
                complexity=complexity,
                halstead=halstead
            )

        except Exception as e:
            return render_template("index.html", prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
