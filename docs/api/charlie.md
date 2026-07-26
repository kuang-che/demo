# Detailed API Rules: QA & Testing (Charlie)

This document describes QA automated testing regulations for the API endpoints.

## 1. Test Isolation Guidelines
- **Dedicated Database File**: Tests must never be run on the developer database (`database/tasks.db`). Override `server.DB_PATH` in `setUp()` to use a dedicated test file (e.g. `tests/test_tasks.db`).
- **Clean State**: Always drop and re-initialize the test database in `setUp()` using `server.init_db()` to ensure assertions run from a consistent, known state.
- **Teardown**: Delete the test database file in `tearDown()` to leave no leftover artifacts in the repository.

## 2. API Schema Validation Points
Verify response states on every test:
- **Keys**: Confirm that tasks returned by endpoints contain `id`, `title`, `description`, `status`, `priority`, and `created_at`.
- **Status code assertions**:
  - GET requests: expect `200`.
  - POST requests: expect `201` for creation, `400` for invalid payloads.
  - PUT requests: expect `200` for updates, `404` for non-existent IDs.
  - DELETE requests: expect `200` for deletes, `404` for repeating deletes.
