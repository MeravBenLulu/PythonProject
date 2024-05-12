from PythonProject.app import app
from flask import request, jsonify

from PythonProject.models.user import User

@app.route('/register', methods=['POST'])
def register_user():
    user_data = request.get_json()
    user_id = User.create_user(user_data)
    return jsonify({'message': 'User registered successfully', 'user_id': str(user_id)})

# Implement other routes for login, profile update, expenses, income, visualization, etc.
