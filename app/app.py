import os 
import numpy as numpy
import tensorflow as tf 

from flask import Flask, flash, request, make_response, render_template

port = int(os.environ.get("PORT", 5000))
app = Flask(__name__)

@app.route("/test", methods=['GET', 'POST'])
def test():
    return jsonify({{hey: "please work"}})

@app.route("/", methods=['GET', 'POST'])
def index():
    return jsonify({{hey: "please work"}})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
