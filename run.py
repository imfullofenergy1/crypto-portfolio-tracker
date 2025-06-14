from app.main import app

if __name__ == "__main__":
    print("🔥 Starting Flask app...")
    app.run(host="0.0.0.0", port=10000, debug=True)
