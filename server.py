from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from backend.database import get_response


app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/api/sendDetails", methods=['POST'])
def handleRequest():
    user_data = request.get_json()
    if user_data['keywords'] is not None and user_data['range'] is not None and user_data['position'] is not None:
        keywords = user_data['keywords']
        range = int(user_data['range'])
        position = user_data['position']
        r = get_response(float(position['lat']), float(position['long']), range, keywords)
        if r is not None and len(r) != 0:
            # Sort based off of closest
            data = { "restaurants": r }
            return jsonify(data)
        else:
            data = { "Error": "No restaraunts in the given radius" }
            return jsonify(data)
    else:
        data = { "Error": "Not all parameters given" }
        return jsonify(data)