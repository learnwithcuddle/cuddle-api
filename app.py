from flask import Flask
from app.services.verify_sign import predict

app = Flask(__name__)

@app.route("/verify", methods=['POST'])
def process_image():
    result = predict()
    return result

@app.route("/")
def index():
    return "FLASK APP IS WORKING YIPEEEEEEEE :333333"

if __name__ == "__main__":
    app.run()
