from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():

    hour = datetime.now().hour

    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    return jsonify({
        "fulfillmentText":
        f"{greeting}! I am Yong Kang, a member of 24 Festive Drums. What is your name?"
    })

@app.route("/")
def home():
    return "Webhook is running!"