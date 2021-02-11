from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/api/', methods=["POST"])
def main_interface():
    response = request.get_json()
    print(response)
    print(type(response))
    response["send"] = "AJAX sent from Flask server..."
    return jsonify(response)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response
