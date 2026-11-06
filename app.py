from flask import Flask, jsonify, request
from datetime import datetime
from zoneinfo import ZoneInfo
//good morning
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():

    hour = datetime.now(ZoneInfo("Asia/Kuala_Lumpur")).hour

    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    return jsonify({
        "fulfillmentText":
        f"{greeting}! I'm Yong Kang, your 24 Festive Drums learning assistant. What is your name?"
    })
