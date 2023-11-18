#!/usr/bin/env python3

from flask import Blueprint, jsonify, request, abort
from models.storage.db_storage import DBStorage
from models.user import User
from models.review import Review
from models.resource_1 import Resource


user_bp = Blueprint('user_bp', __name__)


def get_storage():
    return DBStorage()


@user_bp.route('/users', methods=['GET'])
def get_users():
    storage = get_storage()
    users = storage.get_all(User)
    user_data = [{'id': user.id, 'username': user.username,
                  'email': user.email} for user in users]
    return jsonify({'users': user_data})


@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    storage = get_storage()
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@user_bp.route('/users', methods=['POST'])
def create_user():
    storage = get_storage()
    data = request.get_json()
    new_user = User(**data)
    storage.new(new_user)
    storage.save()
    return jsonify(new_user.to_dict()), 201


@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    storage = get_storage()
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    data = request.get_json()
    for key, value in data.items():
        setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict())


@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    storage = get_storage()
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 204
