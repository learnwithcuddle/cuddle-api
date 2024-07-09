#from flask import Flask, request, jsonify
#from app.services.verify_sign import predict

#app = Flask(__name__)

#@app.route('/verify_sign', methods=['POST'])
#def process_image():
#    result = 1
#    #result = predict()
#    return result

#@app.route("/")
#def index():
#    return "FLASK APP IS WORKING YIPEEEEEEEE :333333"

#if __name__ == "__main__":
#    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "The flask app running on Heroku!"

if __name__ == '__main__':
    app.run()
