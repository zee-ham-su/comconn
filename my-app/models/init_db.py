#!/usr/bin/python3
"""
Initialize the database for the Flask app.

This script creates the necessary tables in the database.
"""

from backend.v1.app import create_app, db



def init_db():
    """
    Initialize the database tables.

    This function creates the required tables in the database by
    utilizing the Flask application context.

    Usage:
        Run this script to set up the database tables.

    Note:
        Make sure the Flask app configuration and database models
        are defined in the 'app.py' file.

    Raises:
        RuntimeError: If the Flask app context cannot be established.

    """
    app = create_app()

    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    init_db()