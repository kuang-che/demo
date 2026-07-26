# Permission Policy: Alice

- **Name**: Alice Chen
- **Role**: Backend Lead Engineer

## Directory Access Rules

| Directory / File | Permission Level | Notes |
|------------------|------------------|-------|
| `backend/`       | **Free-Write**   | Owner of Flask API codebase. |
| `database/`      | **Free-Write**   | Owner of SQLite schemas and db files. |
| `frontend/`      | **Read-Only**    | Read-only access for cross-referencing. |
| `tests/`         | **Free-Write**   | Allowed to write API tests. |
| `config/`        | **Write with Consent** | Configuration templates. |
| `docs/`          | **Free-Write**   | Owner of backend architecture docs. |
| `.env`           | **No Access**    | Contains private API keys and tokens. |
| Shared Root files (README, agents.md, .gitignore) | **Write with Consent** | Requires coordination with the team. |
| **All other files (Unlisted)** | **Read-Only** | Default fallback policy. |
