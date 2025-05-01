from flask import Blueprint, request, jsonify
import joblib
import os
from app.models import train_model

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route('/train', methods=['POST'])
def train():
    try:
        data_path = request.json.get("data_path")
        model_save_path = request.json.get("model_save_path")

        if not (data_path and model_save_path):
            return jsonify({"error": "data_path and model_save_path are required"}), 400

        result = train_model(data_path, model_save_path)
        return jsonify({"message": "Model trained successfully", "result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_blueprint.route('/predict', methods=['POST'])
def predict():
    try:
        model_path = request.json.get("model_path")
        features = request.json.get("features")

        if not (model_path and features):
            return jsonify({"error": "model_path and features are required"}), 400

        model = joblib.load(model_path)
        prediction = model.predict([features])
        result_label = "Absent" if prediction[0] == 0 else "Present"
        return jsonify({"prediction": prediction.tolist(), "result_label": result_label}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500