import os 
import numpy as numpy
from PIL import Image
import tensorflow as tf 

from resizeimage import resizeimage 
from werkzeug import secure_filename
from keras_preprocessing import image 
from flask import Flask, flash, request, make_response, render_template

app = Flask(__name__)

@app.route("/test", methods=['GET', 'POST'])
def index():
    return {"test" : "success :p"}

if __name__ == "__main__":
    app.run()