import os
from functools import wraps
from flask import request, jsonify
import base64

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'message': 'Authorization header is missing'}), 401

        try:
            auth_type, credentials = auth_header.split()
            if auth_type.lower() != 'basic':
                return jsonify({'message': 'Unsupported authentication type'}), 401
            
            decoded_credentials = base64.b64decode(credentials).decode('utf-8')
            username, password = decoded_credentials.split(':')

            admin_user = os.getenv('ADMIN_USERNAME')
            admin_pass = os.getenv('ADMIN_PASSWORD')

            if username == admin_user and password == admin_pass:
                return f(*args, **kwargs)
            else:
                return jsonify({'message': 'Invalid credentials'}), 401

        except Exception as e:
            return jsonify({'message': 'Invalid authorization header', 'error': str(e)}), 401

    return decorated_function
