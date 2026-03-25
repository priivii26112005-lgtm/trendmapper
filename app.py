from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # allow frontend (Netlify) to connect

# 🔥 MongoDB Connection
# For local testing it will use localhost
# For live (Render) you will later replace with MongoDB Atlas URL
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")

client = MongoClient(MONGO_URI)
db = client["trendmapper"]
collection = db["events"]

# 🟢 HOME ROUTE
@app.route("/")
def home():
    return jsonify({"message": "TrendMapper AI Backend Running 🚀"})

# 🟢 TRACK EVENT
@app.route("/track", methods=["POST"])
def track():
    data = request.json

    event = {
        "user_id": data.get("user_id"),
        "event_type": data.get("event_type"),
        "product_id": data.get("product_id"),
        "timestamp": datetime.utcnow()
    }

    collection.insert_one(event)

    return jsonify({"message": "Event stored successfully"})

# 🟢 GET EVENTS
@app.route("/events", methods=["GET"])
def get_events():
    events = []

    for e in collection.find({}, {"_id": 0}):
        events.append(e)

    return jsonify(events)

# 🚀 RUN APP (LOCAL ONLY)
if __name__ == "__main__":
    app.run(debug=True)