#!/usr/bin/env python3

from datetime import datetime
import hashlib
from flask import Blueprint, jsonify, request, abort
from models.storage.db_storage import DBStorage
from models.user import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from flask import render_template, redirect, url_for


user_bp = Blueprint('user_bp', __name__)


def get_storage():
    """
    Get an instance of the storage system.

    Returns:
        DBStorage: An instance of the database storage system.
    """
    return DBStorage()


@user_bp.route('/users', methods=['GET'])
def get_users():
    """
    Retrieve a list of all users.

    Returns:
        Response: JSON response with a list of users.
    """
    storage = get_storage()
    users = storage.get_all(User)
    user_data = [{'id': user.id, 'username': user.username,
                  'email': user.email} for user in users]
    return jsonify({'users': user_data})


@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Retrieve a list of all users.

    Returns:
        Response: JSON response with a list of users.
    """
    storage = get_storage()
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@user_bp.route('/users', methods=['POST'])
def create_user():
    """
    create a list of all users.

    Returns:
        Response: JSON response with a list of users.
    """
    storage = get_storage()
    data = request.get_json()
    new_user = User(**data)
    storage.new(new_user)
    storage.save()
    return jsonify(new_user.to_dict()), 201


@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    update a list of all users.

    Returns:
        Response: JSON response with a list of users.
    """
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
    """
    delete a list of all users.

    Returns:
        Response: JSON response with a list of users.
    """
    storage = get_storage()
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 204


@user_bp.route('/logout',  methods=['DELETE'])
def logout():
    """
    Logout the current user.

    Returns:
        Response: JSON response indicating a successful logout.
    """
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200


@user_bp.route('/current_user')
@login_required
def get_current_user():
    """
    Get information about the current authenticated user.

    Returns:
        Response: JSON response with information about the current user.
    """
    return jsonify(current_user.to_dict())


@user_bp.route('/register', methods=['POST'])
def register():
    """
    Register a new user.

    Returns:
        Response: JSON response indicating the success of the registration.
    """
    data = request.get_json()
    print("Received data:", data)
    storage = get_storage()

    # Check if the username or email is already in use
    existing_user = storage.get_user_by_username(data.get('username'))
    if existing_user:
        return jsonify({'message': 'Username is already taken'}), 400

    existing_email = storage.get_user_by_email(data.get('email'))
    if existing_email:
        return jsonify({'message': 'Email is already registered'}), 400

    # Generate a unique salt for the user
    unique_salt = datetime.utcnow().isoformat()

    # Check if the 'password' field is present in the JSON data
    if 'password' not in data or data['password'] is None:
        return jsonify({'message': 'Password is required'}), 400

    # Hash the password using the unique salt
    hashed_password = hashlib.sha256(
        (unique_salt + data['password']).encode()).hexdigest()

    # Add this line for debugging
    print(f'Hashed Password: "{hashed_password}"')

    # Create a new user and save it to the database
    new_user = User(
        username=data['username'], email=data['email'], password_hash=hashed_password,  unique_salt=unique_salt)
    new_user.password_hash = hashed_password
    storage.new(new_user)
    storage.save()

    return jsonify({'message': 'Registration successful'}), 201


@user_bp.route('/login', methods=['POST'])
def login():
    """
    Login a user.

    Returns:
        Response: JSON response indicating the success or failure of the login attempt.
    """
    data = request.get_json()
    storage = get_storage()
    user = storage.get_user_by_username(data.get('username'))

    if user:
        # Generate the unique salt for the user stored in the database
        some_instance = DBStorage()
        unique_salt = some_instance.get_unique_salt_from_database(user_id=user.id)

        entered_password = data.get('password').strip() if data.get('password') else None
        stored_hashed_password = hashlib.sha256(unique_salt.encode()).hexdigest()

        print(f'Entered Password: "{entered_password}"')
        print(f'Stored Hashed Password: "{stored_hashed_password}"')

        # Check if the password matches
        if hashlib.sha256((unique_salt + entered_password).encode()).hexdigest() == user.password_hash:
            
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Invalid username or password'}), 401


@user_bp.route('/dashboard', methods=['GET', 'OPTIONS'])
@login_required
def dashboard():
    """
    Display the user dashboard.

    Returns:
        Response: Rendered HTML template for the user dashboard.
    """
    # Check if the user is authenticated
    if not current_user.is_authenticated:
        # Redirect to the login page
        return redirect(url_for('user_bp.login'))

    return render_template('dashboard.html')


@user_bp.route('/update_profile', methods=['GET', 'PUT'])
@login_required
def update_profile():
    """
    Update the user profile.

    Returns:
        Response: JSON response indicating the success of the profile update.
    """
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
