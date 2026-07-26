# Detailed API Rules: Backend (Alice)

This document describes the detailed backend implementation rules for API endpoints. The global overview is documented in [api_design.md](file:///d:/Desktop/Demo/my-project/docs/api_design.md).

## 1. Database Query Safety
- **No raw string formatting for parameters**: Always use SQL parameterization (i.e. `?` placeholders in SQLite) to block SQL injection risks.
- **Connection management**: Always open a connection inside route handlers using `get_db_connection()`, query what is needed, and close it immediately in a `try...finally` or `with` block to prevent SQLite database lockouts.

## 2. Input Parameter Validations
For any creation (`POST`) or modification (`PUT`), the fields must satisfy:
- **`title`**: Non-empty string. Whitespace must be trimmed before saving. Length must not exceed 100 characters.
- **`status`**: Must be strictly one of `To Do`, `In Progress`, or `Done`.
- **`priority`**: Must be strictly one of `Low`, `Medium`, or `High`.

## 3. Standard HTTP Status Responses
- `200 OK`: Successful retrieval, update, or deletion.
- `201 Created`: Successful creation of a new task.
- `400 Bad Request`: Input validation failed (missing title, invalid status/priority).
- `404 Not Found`: Task with the specified ID does not exist.
- `500 Internal Server Error`: SQLite error or python exception. Response payload must be `{"error": "description"}`.
