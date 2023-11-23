#!/usr/bin/env python3

from flask import Blueprint, jsonify, request, abort
from models.storage.db_storage import DBStorage
from models.user import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from flask import render_template


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


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        storage = get_storage()
        user = storage.get_user_by_username(data.get('username'))

        entered_password = data.get(
            'password').strip() if data.get('password') else None
        stored_hashed_password = user.password_hash.strip(
        ) if user and user.password_hash else None

        print(f'Entered Password: "{entered_password}"')
        print(f'Stored Hashed Password: "{stored_hashed_password}"')

        if user:
            print(f'User ID: {user.id}')
            print(f'Username: {user.username}')
            print(f'Email: {user.email}')
            
        if user and check_password_hash(stored_hashed_password, entered_password):
            login_user(user)
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Invalid username or password'}), 401
    else:
        # Render the login form for GET requests
        return render_template('login.html')



@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200


@user_bp.route('/current_user')
@login_required
def get_current_user():
    return jsonify(current_user.to_dict())


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    storage = get_storage()

    # Check if the username or email is already in use
    existing_user = storage.get_user_by_username(data.get('username'))
    if existing_user:
        return jsonify({'message': 'Username is already taken'}), 400

    existing_email = storage.get_user_by_email(data.get('email'))
    if existing_email:
        return jsonify({'message': 'Email is already registered'}), 400

    # Create a new user and save it to the database
    new_user = User(**data)
    storage.new(new_user)
    storage.save()

    return jsonify({'message': 'Registration successful'}), 201


@user_bp.route('/update_profile', methods=['GET', 'PUT'])
@login_required
def update_profile():
    if request.method == 'GET':
        data = request.get_json()
        user = current_user
        return render_template('update_profile.html')
    elif request.method == 'PUT':
        data = request.get_json()
        user = current_user

    # Update user profile fields based on the received data
    for key, value in data.items():
        setattr(user, key, value)

    get_storage().save()

    return jsonify({'message': 'Profile updated successfully'}), 200
