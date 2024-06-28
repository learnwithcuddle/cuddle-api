import os 
import numpy as numpy
import tensorflow as tf 

from flask import Flask, flash, request, make_response, render_template

app = Flask(__name__)

@app.route("/test", methods=['GET', 'POST'])
def test():
    return "TESTINGGGGG"  

@app.route("/", methods=['GET', 'POST'])
def index():
    return "INDEXXXXXXXXXX"

if __name__ == "__main__":
    app.run(debug=True)