# Permission Policy: Charlie

- **Name**: Charlie Davis
- **Role**: QA Automation Engineer

## Directory Access Rules

| Directory / File | Permission Level | Notes |
|------------------|------------------|-------|
| `backend/`       | **Read-Only**    | Read-only access for debugging. |
| `database/`      | **Read-Only**    | Read-only access. |
| `frontend/`      | **Read-Only**    | Read-only access. |
| `tests/`         | **Free-Write**   | Owner of unit and integration test codebases. |
| `config/`        | **Read-Only**    | Configuration templates. |
| `docs/`          | **Write with Consent** | Shared project documentation. |
| `docs/api/charlie.md` | **Free-Write**   | Personal QA & testing API rules. |
| `.env`           | **No Access**    | Contains private API keys and tokens. |
| Shared Root files (README, agents.md, .gitignore) | **Write with Consent** | Requires coordination with the team. |
| **All other files (Unlisted)** | **Read-Only** | Default fallback policy. |
