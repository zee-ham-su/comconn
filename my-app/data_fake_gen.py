#!/usr/bin/env python3
"""
Populate the database with fake data for testing or development.

This script generates and inserts fake data into the database tables.

Usage:
    Run this script to populate the database with fake data.

Note:
    Make sure the database is set up and the necessary tables are created.

Raises:
    RuntimeError: If there is an issue inserting fake data into the database.
"""

from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.sql import func
from os import getenv

# Set up database connection
MYAPP_DB_USER = 'com_connect'
MYAPP_DB_PWD = 'com_connect_pwd'
MYAPP_DB_HOST = 'localhost'
MYAPP_DB_NAME = 'com_connect_db'
MYAPP_ENV = getenv('MYAPP_ENV')

db_url = f"mysql+mysqldb://{MYAPP_DB_USER}:{MYAPP_DB_PWD}@{MYAPP_DB_HOST}/{MYAPP_DB_NAME}"
engine = create_engine(db_url)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now())
    reviews = relationship('Review', back_populates='user')


class Resource(Base):
    __tablename__ = 'resources'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    description = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now())
    reviews = relationship('Review', back_populates='resource')


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    resource_id = Column(Integer, ForeignKey('resources.id'))
    rating = Column(Integer)
    comment = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now())
    user = relationship('User', back_populates='reviews')
    resource = relationship('Resource', back_populates='reviews')


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def generate_fake_data(model, num_records=10):
    fake = Faker()
    for _ in range(num_records):
        record = model(
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
        )
        session.add(record)

    session.commit()


# Generate fake data for each model
generate_fake_data(User)

# Generate fake data for Resource and Review models
fake = Faker()
resources = []
for _ in range(10):
    resource = Resource(
        name=fake.word(),
        description=fake.sentence(),
        created_at=fake.date_time_this_decade(),
        updated_at=fake.date_time_this_decade(),
    )
    resources.append(resource)

session.add_all(resources)
session.commit()

reviews = []
for resource in resources:
    for _ in range(fake.random_int(min=1, max=5)):
        review = Review(
            user_id=fake.random_int(min=1, max=10),
            resource_id=resource.id,
            rating=fake.random_int(min=1, max=5),
            comment=fake.text(),
            created_at=fake.date_time_this_decade(),
            updated_at=fake.date_time_this_decade(),
        )
        reviews.append(review)

session.add_all(reviews)
session.commit()

session.close()
