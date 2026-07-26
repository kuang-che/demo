# Collaborative Task Dashboard Demo

A modern, full-stack, single-page application demonstrating a collaborative task management workflow. It is built with a fast Flask API backend, a premium glassmorphic vanilla JavaScript frontend, and a local SQLite database.

## Features

- **Kanban-Style Dashboard**: Clean columns representing task progression (To Do, In Progress, Done).
- **Interactive UI**: Fluid transitions, hover indicators, responsive design, and status cards.
- **REST API**: Backend endpoints for task retrieval, creation, updates, and deletion.
- **Persistent Storage**: Real-time updates backed by SQLite.

## Project Structure

```text
Demo/
│
├── .gitignore
├── agents.md
├── README.md
│
├── docs/
│   ├── directory.md
│   ├── problem_statement.md
│   ├── architecture.md
│   ├── api_design.md
│   └── api/
│
├── frontend/
│   ├── index.html
│   ├── styles/style.css
│   └── scripts/app.js
│
├── backend/
│   ├── server.py
│   ├── requirements.txt
│   ├── db/
│   └── api/
│
├── database/
│   └── schema.sql
│
├── config/
│   └── .env.example
│
├── permissions/
└── tests/
    └── test_api.py
```

## Quick Start

### 1. Database Setup
Initialize the database from the root of the project:
```bash
sqlite3 database/tasks.db < database/schema.sql
```
*(Note: The backend server will automatically initialize the database structure if the file does not exist, so this step is optional.)*

### 2. Backend Setup & Run
Navigate to the `backend/` directory, set up your virtual environment, install dependencies, and run:
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run server
python server.py
```
The server will run on `http://127.0.0.1:5000`.

### 3. Frontend Execution
Since the frontend consists of static HTML, CSS, and JS:
- Simply open `frontend/index.html` in a web browser, or
- Serve it using any local HTTP utility (e.g., Python's `python -m http.server 8000` from the `frontend` folder).

### 4. Running Tests
You can verify the backend API is working correctly by running unit tests:
```bash
python -m unittest tests/test_api.py
```
