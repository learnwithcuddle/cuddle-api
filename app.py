from flask import Flask

app = Flask(__name__)

@app.route("/test", methods=['GET', 'POST'])
def test():
    return jsonify({{hey: "please work"}})

@app.route("/")
def index():
    return "FLASK APP IS WORKING YIPEEEEEEEE :333333"

if __name__ == "__main__":
    app.run()
