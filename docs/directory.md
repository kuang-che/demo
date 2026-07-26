# Project Directory Layout

This file maps out the directory layout and the purpose of each component.

```text
my-project/
├── .gitignore             # Standard git exclusions for Python, SQLite, environment, etc.
├── agents.md              # Project guidelines and conventions for collaborative AI agents.
├── README.md              # Installation instructions, running guidelines, and quick startup.
│
├── permissions/           # Role-based workspace permissions policies.
│   ├── alice.md           # Backend Lead's permission matrix.
│   ├── bob.md             # Frontend Lead's permission matrix.
│   └── charlie.md         # QA Lead's permission matrix.
│
├── docs/                  # Documentation for the project architecture, design, and scope.
│   ├── directory.md       # (This file) Describes the project layout.
│   ├── problem_statement.md # Background, scope, and use cases for the demo.
│   ├── architecture.md    # Frontend-backend-database structure and flow.
│   ├── api_design.md      # Global API specification (endpoints, methods, payloads).
│   └── api/               # Role-specific detailed API rules.
│       ├── alice.md       # Backend database safety, validations, and responses.
│       ├── bob.md         # Frontend connections, state management, and XSS safeguards.
│       └── charlie.md     # QA database isolation, setup/teardowns, and assertion checks.
│
├── frontend/              # Presentation layer (divided into subfolders).
│   ├── index.html         # Application viewport structure.
│   ├── styles/
│   │   └── style.css      # Premium glassmorphic styling and layout.
│   └── scripts/
│       └── app.js         # Logic for UI events and communication with Flask server.
│
├── backend/               # Server-side API application (divided into subfolders).
│   ├── server.py          # Flask service launcher.
│   ├── requirements.txt   # Third-party Python dependencies (Flask, Flask-CORS).
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py      # API routing Blueprint logic.
│   └── db/
│       ├── __init__.py
│       └── connection.py  # SQLite connection utility methods.
│
├── database/              # Storage layer.
│   └── schema.sql         # SQL schema definitions for tables.
│
├── config/                # Environment config folder.
│   └── .env.example       # Template for local environment properties.
│
└── tests/                 # QA layer.
    └── test_api.py        # Python unittest suite targeting server API endpoints.
```
