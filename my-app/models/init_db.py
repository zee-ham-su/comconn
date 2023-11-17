#!/usr/bin/python3
"""
Initialize the database for the Flask app.

This script creates the necessary tables in the database using direct SQL queries.
"""

from models.storage.db_storage import DBStorage
from backend.v1.app import create_app
from sqlalchemy import create_engine, Table, DateTime, Column, Integer, String, MetaData, ForeignKeyConstraint
import sys
from datetime import datetime

sys.path.append("/root/commcon/my-app")


def init_db():
    """
    Initialize the database tables using direct SQL queries.

    This function executes the SQL queries to create the required tables in the database.

    Usage:
        Run this script to set up the database tables.

    Note:
        Make sure the database and user have the necessary privileges.

    Raises:
        RuntimeError: If the SQL queries encounter an error.

    """
    
    db_storage = DBStorage()
    engine = db_storage.engine

    app = create_app()
    metadata = MetaData()

    resources = Table(
        'resources', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String(255), nullable=False),
        Column('description', String(255), nullable=False),
        Column('created_at', DateTime, default=datetime.utcnow,
               nullable=False),
        Column('updated_at', DateTime, default=datetime.utcnow,
               onupdate=datetime.utcnow, nullable=False)
    )

    reviews = Table(
        'reviews', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('user_id', Integer),
        Column('resource_id', Integer),
        Column('rating', Integer),
        Column('comment', String(255)),
        Column('created_at', DateTime, default=datetime.utcnow,
               nullable=False),
        Column('updated_at', DateTime, default=datetime.utcnow,
               onupdate=datetime.utcnow, nullable=False),
        ForeignKeyConstraint(['user_id'], ['users.id']),
        ForeignKeyConstraint(['resource_id'], ['resources.id'])
    )

    users = Table(
        'users', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('username', String(255), unique=True),
        Column('email', String(255), unique=True),
        Column('password', String(255)),
        Column('created_at', DateTime, default=datetime.utcnow,
               nullable=False),
        Column('updated_at', DateTime, default=datetime.utcnow,
               onupdate=datetime.utcnow, nullable=False)
    )

    try:
        metadata.create_all(engine)
        print("Tables created successfully!")
    except Exception as e:
        print(f"Error creating tables: {e}")


if __name__ == "__main__":
    init_db()
