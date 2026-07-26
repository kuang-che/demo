import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

# Import connection utilities and API routes from our packages
from db.connection import init_db
from api.routes import tasks_bp

load_dotenv()

# Resolve absolute path to frontend asset directory
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")
# Enable CORS so frontend files can connect from any origin
CORS(app)

# Register the routes blueprint with prefix /api
app.register_blueprint(tasks_bp, url_prefix="/api")

@app.route("/")
def serve_index():
    """Serve the main frontend application at root URL."""
    return send_from_directory(FRONTEND_DIR, "index.html")

if __name__ == "__main__":
    # Initialize SQLite database using connection package
    init_db()
    print(f"🚀 SyncBoard Server running on http://127.0.0.1:5000")
    # Run server locally on port 5000
    app.run(host="127.0.0.1", port=5000, debug=True)
