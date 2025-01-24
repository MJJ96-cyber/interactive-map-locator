from flask import Flask, render_template, jsonify, request
import os
import requests
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()

GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

@app.route('/')
def home():
    return render_template('index.html')

# Serve the API key securely to the frontend
@app.route('/get-api-key')
def get_api_key():
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    return jsonify({"apiKey": api_key})

@app.route('/api/maps_key', methods=['GET'])
def get_maps_key():
    return jsonify({"key": GOOGLE_MAPS_API_KEY})

@app.route('/api/nearby_places', methods=['POST'])
def get_nearby_places():
    data = request.json
    lat = data.get('lat')
    lng = data.get('lng')
    radius = data.get('radius', 1000)  # Default to 1000 meters
    category = data.get('category', '')

    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={category}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch nearby places"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
