# REST API Design

This document details the RESTful API contract implemented by the Flask backend server. All responses are returned as JSON.

## Base URL
Default: `http://127.0.0.1:5000`

---

## Endpoints

### 1. Get All Tasks
Retrieve a list of all current tasks in the database.

* **URL**: `/api/tasks`
* **Method**: `GET`
* **Response Code**: `200 OK`
* **Response Body**:
```json
[
  {
    "id": 1,
    "title": "Set up environment",
    "description": "Establish Python venv and install dependencies",
    "status": "Done",
    "priority": "High",
    "created_at": "2026-07-21 15:30:00"
  },
  {
    "id": 2,
    "title": "Design layout",
    "description": "Create glassmorphic UI dashboard",
    "status": "In Progress",
    "priority": "Medium",
    "created_at": "2026-07-21 16:15:00"
  }
]
```

---

### 2. Create Task
Create a new task.

* **URL**: `/api/tasks`
* **Method**: `POST`
* **Request Headers**: `Content-Type: application/json`
* **Request Body**:
```json
{
  "title": "Write unit tests",
  "description": "Ensure API endpoints are covered by tests",
  "status": "To Do",
  "priority": "Low"
}
```
* **Response Code**: `201 Created`
* **Response Body**:
```json
{
  "id": 3,
  "title": "Write unit tests",
  "description": "Ensure API endpoints are covered by tests",
  "status": "To Do",
  "priority": "Low",
  "created_at": "2026-07-21 17:00:00"
}
```

---

### 3. Update Task
Update the properties of an existing task (e.g., changing status or priority).

* **URL**: `/api/tasks/<id>`
* **Method**: `PUT`
* **Request Headers**: `Content-Type: application/json`
* **Request Body**:
```json
{
  "status": "In Progress"
}
```
* **Response Code**: `200 OK`
* **Response Body**:
```json
{
  "id": 3,
  "title": "Write unit tests",
  "description": "Ensure API endpoints are covered by tests",
  "status": "In Progress",
  "priority": "Low",
  "created_at": "2026-07-21 17:00:00"
}
```

---

### 4. Delete Task
Delete a task from the board.

* **URL**: `/api/tasks/<id>`
* **Method**: `DELETE`
* **Response Code**: `200 OK`
* **Response Body**:
```json
{
  "message": "Task with ID 3 has been successfully deleted."
}
```
