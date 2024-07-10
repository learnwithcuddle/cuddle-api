import sys
from flask import Flask, request, jsonify
from verify_sign import *

app = Flask(__name__)

@app.route('/verify', methods=['POST'])
def process_image():
    result = predict()
    return result

@app.route('/')
def index():
    return "FLASK APP IS WORKING YIPEEEEEEEE :333333"

if __name__ == "__main__":
    app.run(debug=True)
