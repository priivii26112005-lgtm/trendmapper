from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="frontend")
CORS(app)

# =========================
# Serve Frontend
# =========================
@app.route('/')
def home():
    return send_from_directory('frontend', 'index.html')

# =========================
# API: Events
# =========================
events = []

@app.route('/track', methods=['POST'])
def track():
    data = request.json
    events.append(data)
    return jsonify({"message": "Event stored"})

@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(events)

# =========================
# Run
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
