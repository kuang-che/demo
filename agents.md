# AI Agent Project Guidelines

This document outlines standard guidelines and workflows for AI agents collaborating on the **Collaborative Demo Project**.

## Core Engineering Principles

- **Separation of Concerns**: Keep the Flask API and the vanilla JavaScript application modular and distinct by using the restructured subfolders.
- **RESTful Design**: Ensure all API routes are RESTful and return JSON payloads.
- **Database Safety**: Write robust SQL queries using parameterized inputs in Python to prevent SQL injection.
- **Visual Design**: The UI must maintain premium styling (dark mode, clean typography, soft borders, and fluid transitions).

## Collaborative Permissions & Detailed API Rules

To support multi-developer workflows, development access and technical guidelines are separated. AI agents MUST cross-reference a user's role permission file AND their specific API implementation rules before executing edits.

### 1. Permission Access Levels
Agents must evaluate file write actions against the user's permission file, categorizing access into one of the following levels:
- **Free-Write (可自由寫)**: The agent has permission to modify files/directories in this scope freely to complete tasks.
- **Write with Consent (可寫但須取得同意)**: The agent may modify files/directories in this scope, but MUST explicitly explain the change to the user and obtain approval before editing.
- **Read-Only (只讀)**: The agent can read files in this scope for reference but is STRICTLY FORBIDDEN from making any code changes.
- **No Access (不可讀寫)**: The agent is forbidden from both reading and writing files/directories in this scope (used for sensitive configurations like API keys).

> [!IMPORTANT]
> **Default Permissions Rule**: Any files or directories not explicitly listed in a user's permission profile matrix default to **Read-Only (只讀)**.
> **API Keys & Credentials Rule**: Local `.env` files or credentials files storing API keys and secret tokens are strictly **No Access (不可讀寫)** for all developers to prevent security exposure.

### 2. Permission Access Matrices
Refer to the individual markdown policies to determine the active developer's permission levels:
- **Backend Lead**: [Alice Chen](file:///d:/Desktop/Demo/my-project/permissions/alice.md) (Free-Write in `backend/` and `database/`; Read-Only in `frontend/`).
- **Frontend Lead**: [Bob Smith](file:///d:/Desktop/Demo/my-project/permissions/bob.md) (Free-Write in `frontend/`; Read-Only in `backend/` and `database/`).
- **QA Lead**: [Charlie Davis](file:///d:/Desktop/Demo/my-project/permissions/charlie.md) (Free-Write in `tests/`; Read-Only in others).

### 3. Role-Specific Detailed API Rules
- **Backend API Rules**: [Alice's API Rules](file:///d:/Desktop/Demo/my-project/docs/api/alice.md) (database safety, query formats, parameter checks).
- **Frontend API Rules**: [Bob's API Rules](file:///d:/Desktop/Demo/my-project/docs/api/bob.md) (network configurations, DOM insertion, XSS prevention).
- **QA & Testing Rules**: [Charlie's API Rules](file:///d:/Desktop/Demo/my-project/docs/api/charlie.md) (test isolation, DB teardowns, schema validation assertions).

For global API contracts, refer to the high-level summary [api_design.md](file:///d:/Desktop/Demo/my-project/docs/api_design.md), which should not be modified frequently.

## Restructured Development Flow

1. **Database Setup**: Use `database/schema.sql` to initialize `database/tasks.db`.
2. **Backend**: Split into modular directories:
   - Run from: `backend/server.py`
   - API Blueprint routes: `backend/api/routes.py`
   - Database connection: `backend/db/connection.py`
3. **Frontend**: Assets are split into separate resource folders:
   - Viewport: `frontend/index.html`
   - Stylesheets: `frontend/styles/style.css`
   - JavaScript application: `frontend/scripts/app.js`
