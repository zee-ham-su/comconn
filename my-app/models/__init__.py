#!/usr/bin/python3
"""
Initialization module for the models package.

This module handles the initialization of the storage based on the value of TYPE_STORAGE environment variable.
"""
from os import getenv

TYPE_STORAGE = getenv("TYPE_STORAGE")

if TYPE_STORAGE == "db":
    from models.storage.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
