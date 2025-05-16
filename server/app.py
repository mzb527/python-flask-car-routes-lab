existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']
from flask import Flask, jsonify

app = Flask(__name__)

# Car models you care about
car_models = {
    "beedle": {"brand": "Beedle Motors", "year": 2024, "type": "Compact"},
    "crossroads": {"brand": "Crossroads Automotive", "year": 2023, "type": "SUV"},
    "m2": {"brand": "M Series", "year": 2025, "type": "Sports"},
    "panique": {"brand": "Panique Cars", "year": 2024, "type": "Luxury"}
}

# Default route introducing the company
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Car Company Database! Use /<model> to get details on Beedle, Crossroads, M2, or Panique."})

# Model-specific route for requesting information
@app.route("/<model>")
def get_car_model(model):
    if not model.isalpha() and model != "m2":  # Allow 'm2' as a valid model
        return jsonify({"error": "Invalid model name format"}), 400

    car_info = car_models.get(model.lower())
    if car_info:
        return jsonify(car_info)

    return jsonify({"error": "Model not found"}), 404

# Global error handlers
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Route not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)