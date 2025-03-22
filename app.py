from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Define feature names (must match training features)
expected_columns = [
    "MedInc", "HouseAge", "AveRooms", "AveBedrms", 
    "Population", "AveOccup", "Latitude", "Longitude"
]

# Initialize Flask app
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        
        # Ensure data is a pandas DataFrame with correct column names
        features = pd.DataFrame([data["features"]], columns=expected_columns)
        
        # Predict
        prediction = model.predict(features)[0]
        return jsonify({"predicted_price": prediction})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

