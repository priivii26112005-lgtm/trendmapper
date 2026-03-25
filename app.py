from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# =========================
# 👉 Serve Frontend (IMPORTANT)
# =========================
@app.route('/')
def home():
    return send_from_directory('frontend', 'index.html')


# =========================
# 👉 Dummy Event Data API
# =========================
@app.route('/events', methods=['GET'])
def get_events():
    data = [
        {"event_type": "view", "product_id": 101},
        {"event_type": "add_to_cart", "product_id": 101},
        {"event_type": "view", "product_id": 102},
        {"event_type": "add_to_cart", "product_id": 101},
        {"event_type": "view", "product_id": 103},
        {"event_type": "add_to_cart", "product_id": 102},
        {"event_type": "view", "product_id": 101},
        {"event_type": "add_to_cart", "product_id": 103},
    ]
    return jsonify(data)


# =========================
# 👉 Top Products API
# =========================
@app.route('/top-products', methods=['GET'])
def top_products():
    products = {
        101: 5,
        102: 2,
        103: 1
    }

    sorted_products = sorted(products.items(), key=lambda x: x[1], reverse=True)

    result = []
    for p in sorted_products:
        result.append({
            "product_id": p[0],
            "count": p[1]
        })

    return jsonify(result)


# =========================
# 👉 AI Insights (Dummy)
# =========================
@app.route('/ai-insights', methods=['GET'])
def ai_insights():
    insights = [
        "📈 Product 101 is trending!",
        "🛒 Add-to-cart rate is increasing",
        "⚡ Users are more active in evening",
        "🔥 Product 102 needs promotion"
    ]
    return jsonify({"insight": random.choice(insights)})


# =========================
# 👉 Login API (Simple)
# =========================
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # simple login (demo)
    if username == "admin" and password == "1234":
        return jsonify({"status": "success", "user": username})
    else:
        return jsonify({"status": "fail"}), 401


# =========================
# 👉 Run App (Render Ready)
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)