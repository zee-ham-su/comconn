#!/usr/bin/python3
"""
config.py

Configuration module for the MyApp project.

This module defines the AppConfig class, which contains configuration variables for the project.
"""

from os import getenv

class AppConfig:
    """
    AppConfig class containing configuration variables for the project.

    Attributes:
        MYAPP_DB_USER (str): Database user for MyApp.
        MYAPP_DB_PWD (str): Database password for MyApp.
        MYAPP_DB_HOST (str): Database host for MyApp.
        MYAPP_DB_NAME (str): Database name for MyApp.
        MYAPP_ENV (str): Environment variable for MyApp.

    Methods:
        (None)
    """
    MYAPP_DB_USER = getenv('MYAPP_DB_USER')
    MYAPP_DB_PWD = getenv('MYAPP_DB_PWD')
    MYAPP_DB_HOST = getenv('MYAPP_DB_HOST')
    MYAPP_DB_NAME = getenv('MYAPP_DB_NAME')
    MYAPP_ENV = getenv('MYAPP_ENV')
