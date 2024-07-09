from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, this is your Flask app running on Heroku!"

if __name__ == '__main__':
    app.run()
