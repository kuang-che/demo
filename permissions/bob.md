# Permission Policy: Bob

- **Name**: Bob Smith
- **Role**: Lead Frontend Developer

## Directory Access Rules

| Directory / File | Permission Level | Notes |
|------------------|------------------|-------|
| `backend/`       | **Read-Only**    | Read-only access for API endpoint integrations. |
| `database/`      | **Read-Only**    | Read-only access to check schema.sql. |
| `frontend/`      | **Free-Write**   | Owner of presentation assets, layouts, and logic. |
| `tests/`         | **Read-Only**    | Read-only access for test coordination. |
| `config/`        | **Read-Only**    | Configuration templates. |
| `docs/`          | **Write with Consent** | Shared project documentation. |
| `docs/api/bob.md` | **Free-Write**   | Personal frontend API implementation rules. |
| `.env`           | **No Access**    | Contains private API keys and tokens. |
| Shared Root files (README, agents.md, .gitignore) | **Write with Consent** | Requires coordination with the team. |
| **All other files (Unlisted)** | **Read-Only** | Default fallback policy. |
