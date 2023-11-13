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
    MYAPP_DB_USER = 'com_connect'
    MYAPP_DB_PWD = 'com_connect_pwd'
    MYAPP_DB_HOST = 'localhost'
    MYAPP_DB_NAME = 'com_connect_db'
    MYAPP_ENV = getenv('MYAPP_ENV')
