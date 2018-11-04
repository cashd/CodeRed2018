from flask import Flask, render_template, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/api/sendDetails", methods=['POST'])
def handleRequest():
    print(request.json)
    data = { "hi": 4 }
    return jsonify(data)