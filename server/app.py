existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']
from flask import Flask, jsonify

app = Flask(__name__)

existing_models = ["sedan", "suv", "sports"]

# Default route
@app.route('/')
def home():
    return "Welcome to Flatiron Cars"

# Model-specific route
@app.route('/<model>')
def car_model(model):
    if model.lower() in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog", 404

if __name__ == '__main__':
    app.run(debug=True)