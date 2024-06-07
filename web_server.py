# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is a simple Flask app by Mudassir."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4512)
