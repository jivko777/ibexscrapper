from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/data")
def get_data():
    try:
        with open("ibex_data.json", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception:
        return jsonify({"error": "Данните не са налични"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
