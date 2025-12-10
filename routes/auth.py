from flask import Blueprint, request, jsonify
import os
import base64

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username and password are required'}), 400

    username = data['username']
    password = data['password']

    admin_user = os.getenv('ADMIN_USERNAME')
    admin_pass = os.getenv('ADMIN_PASSWORD')

    if username == admin_user and password == admin_pass:
        # In a real app, you would return a JWT or session cookie.
        # For this simple case, we'll just confirm the login is OK
        # and the frontend can construct the Basic Auth header.
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
