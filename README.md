" House Price Prediction API" 
This project provides an API to predict house prices based on input features.

 Features
- Predicts house prices using a trained machine learning model.
- Accepts input features via API requests.
- Returns predicted prices as output.
 Installation

1.Clone the repository:
git clone https://github.com/TEN3T-12/house-price-prediction-api.git
cd house-price-prediction-api

Install dependencies:
pip install -r requirements.txt


Run the API server:
python app.py

Make a request to the API: Use a tool like Postman or curl to send a POST request with house features.

curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"feature1": value, "feature2": value}'

{
  "predicted_price": 250000
}


License
This project is licensed under the MIT License.



