#!/usr/bin/python3
"""
Flask app
"""

from models.found_model import db
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append("/root/commcon/my-app")

# backend/v1/app.py
from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from routes.review_route import review_bp
from routes.resource_route import resource_bp
from routes.user_route import user_bp
from models.storage.db_storage import DBStorage
from models.storage.config import AppConfig  # Import AppConfig from config.py


# Initialize the SQLAlchemy instance with the Flask app
db = SQLAlchemy()

db_storage = DBStorage()

#models import

def create_app():
    app = Flask(__name__)
    # Update the database URI with your MySQL credentials and database name
    db_uri = f"mysql://{AppConfig.MYAPP_DB_USER}:{AppConfig.MYAPP_DB_PWD}@{AppConfig.MYAPP_DB_HOST}/{AppConfig.MYAPP_DB_NAME}"
    print(f"Database URI: {db_uri}")
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    # To suppress a warning
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    
    # Initialize the SQLAlchemy instance with the Flask app
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(resource_bp)
    app.register_blueprint(review_bp)

    # Teardown context
    @app.teardown_appcontext
    def close_db(error):
        """ Close Storage """
        db_storage.close()

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

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        # Create tables based on the defined models
        db.create_all()
    app.run(debug=True)
