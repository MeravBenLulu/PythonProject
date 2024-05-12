import unittest
from PythonProject.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_register_user(self):
        response = self.app.post('/register', json={'username': 'test_user'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
