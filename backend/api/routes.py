from flask import Blueprint, request, jsonify
from db.connection import get_db_connection

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route("/tasks", methods=["GET"])
def get_tasks():
    """Get all tasks from the database."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC")
        rows = cursor.fetchall()
        conn.close()
        
        tasks = []
        for row in rows:
            tasks.append({
                "id": row["id"],
                "title": row["title"],
                "description": row["description"],
                "status": row["status"],
                "priority": row["priority"],
                "created_at": row["created_at"]
            })
        return jsonify(tasks), 200
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve tasks: {str(e)}"}), 500

@tasks_bp.route("/tasks", methods=["POST"])
def create_task():
    """Create a new task in the database."""
    data = request.get_json() or {}
    title = data.get("title")
    description = data.get("description", "")
    status = data.get("status", "To Do")
    priority = data.get("priority", "Medium")
    
    if not title or not title.strip():
        return jsonify({"error": "Task title is required"}), 400
        
    if status not in ("To Do", "In Progress", "Done"):
        return jsonify({"error": "Invalid status. Must be 'To Do', 'In Progress', or 'Done'"}), 400
        
    if priority not in ("Low", "Medium", "High"):
        return jsonify({"error": "Invalid priority. Must be 'Low', 'Medium', or 'High'"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, description, status, priority) VALUES (?, ?, ?, ?)",
            (title.strip(), description.strip(), status, priority)
        )
        conn.commit()
        task_id = cursor.lastrowid
        
        # Retrieve the newly created task
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = cursor.fetchone()
        conn.close()
        
        task = {
            "id": row["id"],
            "title": row["title"],
            "description": row["description"],
            "status": row["status"],
            "priority": row["priority"],
            "created_at": row["created_at"]
        }
        return jsonify(task), 201
    except Exception as e:
        return jsonify({"error": f"Failed to create task: {str(e)}"}), 500

@tasks_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """Update a task's fields dynamically."""
    data = request.get_json() or {}
    
    # Retrieve the task first
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    
    if not row:
        conn.close()
        return jsonify({"error": f"Task with ID {task_id} not found"}), 404
        
    # Read updated fields, fallback to current values
    title = data.get("title", row["title"])
    description = data.get("description", row["description"])
    status = data.get("status", row["status"])
    priority = data.get("priority", row["priority"])
    
    if not title or not title.strip():
        conn.close()
        return jsonify({"error": "Task title cannot be empty"}), 400
        
    if status not in ("To Do", "In Progress", "Done"):
        conn.close()
        return jsonify({"error": "Invalid status. Must be 'To Do', 'In Progress', or 'Done'"}), 400
        
    if priority not in ("Low", "Medium", "High"):
        conn.close()
        return jsonify({"error": "Invalid priority. Must be 'Low', 'Medium', or 'High'"}), 400

    try:
        cursor.execute(
            "UPDATE tasks SET title = ?, description = ?, status = ?, priority = ? WHERE id = ?",
            (title.strip(), description.strip(), status, priority, task_id)
        )
        conn.commit()
        
        # Retrieve the updated task
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        updated_row = cursor.fetchone()
        conn.close()
        
        task = {
            "id": updated_row["id"],
            "title": updated_row["title"],
            "description": updated_row["description"],
            "status": updated_row["status"],
            "priority": updated_row["priority"],
            "created_at": updated_row["created_at"]
        }
        return jsonify(task), 200
    except Exception as e:
        conn.close()
        return jsonify({"error": f"Failed to update task: {str(e)}"}), 500

@tasks_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Delete a task by ID."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = cursor.fetchone()
        
        if not row:
            conn.close()
            return jsonify({"error": f"Task with ID {task_id} not found"}), 404
            
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        
        return jsonify({"message": f"Task with ID {task_id} has been successfully deleted."}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to delete task: {str(e)}"}), 500
