import unittest
import os
import json
import sys

# Ensure backend folder is in path for imports
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend"))
if backend_dir not in sys.path:
    sys.path.append(backend_dir)

import server
from db import connection

class TaskApiTestCase(unittest.TestCase):
    def setUp(self):
        """Configure test environments and initialize temporary database."""
        server.app.config['TESTING'] = True
        
        # Route DB path to a dedicated testing file to avoid corrupting dev database
        self.test_db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "test_tasks.db"))
        connection.DB_PATH = self.test_db_path
        
        # Remove any existing test database file
        if os.path.exists(self.test_db_path):
            try:
                os.remove(self.test_db_path)
            except OSError:
                pass
                
        # Initialize the database structure and seeds
        connection.init_db()
        
        self.app = server.app.test_client()

    def tearDown(self):
        """Cleanup test database file."""
        if os.path.exists(self.test_db_path):
            try:
                os.remove(self.test_db_path)
            except OSError:
                pass

    def test_get_tasks(self):
        """Test retrieving all tasks."""
        response = self.app.get('/api/tasks')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(isinstance(data, list))
        # The schema.sql seeds 3 items
        self.assertEqual(len(data), 3)

    def test_create_task(self):
        """Test successful task creation."""
        payload = {
            "title": "Write more unit tests",
            "description": "Expand tests suite to cover validations",
            "status": "To Do",
            "priority": "Medium"
        }
        response = self.app.post(
            '/api/tasks',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn("id", data)
        self.assertEqual(data["title"], "Write more unit tests")
        self.assertEqual(data["status"], "To Do")
        self.assertEqual(data["priority"], "Medium")

    def test_create_task_missing_title(self):
        """Test validation error when creating a task with missing title."""
        payload = {
            "description": "Missing title",
            "status": "In Progress"
        }
        response = self.app.post(
            '/api/tasks',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn("error", data)

    def test_update_task(self):
        """Test updating a task's status and priority."""
        # Using ID 1 since schema seeds insert 3 rows starting with ID 1
        payload = {
            "status": "In Progress",
            "priority": "High"
        }
        response = self.app.put(
            '/api/tasks/1',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["status"], "In Progress")
        self.assertEqual(data["priority"], "High")

    def test_delete_task(self):
        """Test deleting an existing task."""
        # Delete task with ID 2
        response = self.app.delete('/api/tasks/2')
        self.assertEqual(response.status_code, 200)
        
        # Verify it has been removed by querying list again
        get_resp = self.app.get('/api/tasks')
        data = json.loads(get_resp.data)
        self.assertEqual(len(data), 2) # Should now have only 2 elements
        
        # Verify attempting to delete again returns 404
        response_repeat = self.app.delete('/api/tasks/2')
        self.assertEqual(response_repeat.status_code, 404)

if __name__ == '__main__':
    unittest.main()
