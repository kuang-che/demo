import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Import connection utilities and API routes from our packages
from db.connection import init_db
from api.routes import tasks_bp

load_dotenv()

app = Flask(__name__)
# Enable CORS so frontend files can connect
CORS(app)

# Register the routes blueprint with prefix /api
app.register_blueprint(tasks_bp, url_prefix="/api")

if __name__ == "__main__":
    # Initialize SQLite database using connection package
    init_db()
    # Run server locally on port 5000
    app.run(host="127.0.0.1", port=5000, debug=True)
