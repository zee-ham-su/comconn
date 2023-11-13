#!/usr/bin/python3
from flask import Blueprint, jsonify
from models.storage.db_storage import DBStorage
from models.user import User
user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users')
def get_users():
    users = DBStorage.get_all(User)
    user_data = [{'id': user.id, 'username': user.username,
                  'email': user.email} for user in users]
    return jsonify({'users': user_data})
