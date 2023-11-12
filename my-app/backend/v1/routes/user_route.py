#!/usr/bin/python3
import sys
sys.path.append('/root/commcon/my-app/backend/v1/models')
from flask import Blueprint, jsonify
from storage import storage
from user import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users')
def get_users():
    users = storage.get_all(User)
    user_data = [{'id': user.id, 'username': user.username,
                  'email': user.email} for user in users]
    return jsonify({'users': user_data})
