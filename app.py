from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data
        age = int(request.form["age"])
        cholesterol = int(request.form["cholesterol"])
        bp = int(request.form["bp"])

        # Prepare data for prediction
        input_data = np.array([[age, cholesterol, bp]])
        prediction = model.predict(input_data)[0]

        # Convert prediction to meaningful output
        result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
