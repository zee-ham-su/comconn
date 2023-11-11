#!/usr/bin/python3
"""
Flask app
"""
from routes.review_route import review_bp
from routes.resource_route import resource_bp
from routes.user_route import user_bp
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import storage

app = Flask(__name__)

# Update the database URI with your MySQL credentials and database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress a warning

# Initialize the SQLAlchemy instance with the Flask app
db = SQLAlchemy(app)


# Create tables based on the defined models
db.create_all()

# Import blueprints from routes

# Register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(resource_bp)
app.register_blueprint(review_bp)

# Teardown context


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()

# 404 Error handler


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
        404:
            description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    app.run(debug=True)
