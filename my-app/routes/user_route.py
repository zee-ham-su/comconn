#!/usr/bin/python3
import sys
sys.path.append("/root/commcon/my-app")

from flask import Blueprint, jsonify
from models.storage.db_storage import DBStorage
from models.user import User
user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users')
def get_users():
    # Create an instance of DBStorage
    storage = DBStorage()
    users = storage.get_all(User)  # Use the instance to call get_all method
    user_data = [{'id': user.id, 'username': user.username,
                  'email': user.email} for user in users]
    return jsonify({'users': user_data})
