from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from backend.database import get_rest_in_range


app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/api/sendDetails", methods=['POST'])
def handleRequest():
    user_data = request.get_json()
    #if user_data['keywords'] and user_data['range'] and user_data['position']:
    keywords = user_data['keywords']
    range = int(user_data['range'])
    position = user_data['position']
    r = get_rest_in_range(float(position['lat']), float(position['long']), range)
    print(r)
    #r = get_rest_in_range()
    #print(r)
    data = { "hi": 4 }
    return jsonify(data)