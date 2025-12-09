from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World from Jenkins CI/CD Pipeline!"

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)