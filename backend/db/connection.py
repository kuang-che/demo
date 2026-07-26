import os
import sqlite3
from dotenv import load_dotenv

# Load configurations
load_dotenv()

# Resolve SQLite database path starting from this file's location (backend/db/connection.py)
DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "database", "tasks.db")
DB_PATH = os.path.abspath(os.getenv("DB_PATH", DEFAULT_DB_PATH))

def init_db():
    """Initializes the SQLite database using the schema.sql file if database does not exist."""
    db_dir = os.path.dirname(DB_PATH)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)

    if not os.path.exists(DB_PATH):
        print(f"Database file not found at {DB_PATH}. Initializing database...")
        schema_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "database", "schema.sql"))
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        if os.path.exists(schema_path):
            try:
                with open(schema_path, "r", encoding="utf-8") as f:
                    cursor.executescript(f.read())
                conn.commit()
                print("Database structure and seed data initialized successfully.")
            except Exception as e:
                print(f"Error executing schema script: {e}")
        else:
            print("Warning: schema.sql not found. Creating table using fallback query.")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT NOT NULL CHECK(status IN ('To Do', 'In Progress', 'Done')) DEFAULT 'To Do',
                    priority TEXT NOT NULL CHECK(priority IN ('Low', 'Medium', 'High')) DEFAULT 'Medium',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()
        conn.close()
    else:
        print(f"Database already exists at {DB_PATH}.")

def get_db_connection():
    """Establishes connection to the SQLite database and configures row factory."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
