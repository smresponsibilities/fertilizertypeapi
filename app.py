import pickle
from flask import Flask, request
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app) 


fertname_dict = {0: '10-26-26', 1: '14-35-14', 2: '17-17-17', 3: '20-20', 4: '28-28', 5: 'DAP', 6: 'Urea'}

with open("xgb_pipeline.pkl", "rb") as f:
    xgb_pipeline = pickle.load(f)


@app.route('/')
def home():
    return "This is a Fertilizer Recommendation API!"

# {
#   "temperature": 0.0,
#   "humidity": 0.0,
#   "moisture": 0.0,
#   "soilType": 0,
#   "cropType": 0,
#   "nitrogen": 0,
#   "potassium": 0,
#   "phosphorous": 0
# }

@app.route('/fertilizername', methods=['POST'])
def get_fertilizer():
    try:
        numbers1 = request.json
        
        numbers=[ numbers1["temperature"],
            numbers1["humidity"],
            numbers1["moisture"],
            numbers1["soilType"],
            numbers1["cropType"],
            numbers1["nitrogen"],
            numbers1["potassium"],
            numbers1["phosphorous"]]
        
        numbers_array = np.array(numbers).reshape(1, -1)
        prediction = xgb_pipeline.predict(numbers_array)[0]
        
        if prediction in fertname_dict:
            return {
                "Fertilizername": fertname_dict[prediction]
            }
        else:
            return {
                "error": "Invalid prediction"
            }
    except KeyError:
        return {
            "error": "Invalid input data"
        }
    except Exception as e:
        return {
            "error": str(e)
        }

if __name__ == '__main__':
    app.run(debug=True)