-- Drop table if exists to allow clean re-initialization
DROP TABLE IF EXISTS tasks;

-- Create tasks table
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL CHECK(status IN ('To Do', 'In Progress', 'Done')) DEFAULT 'To Do',
    priority TEXT NOT NULL CHECK(priority IN ('Low', 'Medium', 'High')) DEFAULT 'Medium',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Seed tasks for demonstration
INSERT INTO tasks (title, description, status, priority) VALUES 
('Setup Demo Architecture', 'Configure project folders, write documentations, and design schema.', 'Done', 'High'),
('Build Frontend Interface', 'Develop the glassmorphic dark-theme UI with CSS and JavaScript.', 'In Progress', 'Medium'),
('Implement REST API Server', 'Write Flask code to fetch, update, and persist tasks in SQLite.', 'To Do', 'High');
