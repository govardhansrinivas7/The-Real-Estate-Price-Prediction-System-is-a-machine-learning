from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import json
import numpy as np

app = Flask(__name__)
CORS(app)

# Load model
try:
    model = pickle.load(open("model/house_price_model.pkl", "rb"))
    with open("model/columns.json", "r") as f:
        data_columns = json.load(f)["data_columns"]
except FileNotFoundError:
    print("Warning: Model files not found. Please run train_model.py first.")
    model = None
    data_columns = []

@app.route("/")
def home():
    return "Real Estate Price Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.get_json()

    try:
        sqft = float(data["sqft"])
        bhk = int(data["bhk"])
        bath = int(data["bath"])
        location = data["location"].lower()

        x = np.zeros(len(data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk

        if location in data_columns:
            loc_index = data_columns.index(location)
            x[loc_index] = 1

        price = model.predict([x])[0]

        return jsonify({
            "predicted_price": round(price, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
