from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is Running"

@app.route("/api")
def api():
    return jsonify({
        "message": "Hello from Backend Version 8!",
        "status": "success"
    })

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
