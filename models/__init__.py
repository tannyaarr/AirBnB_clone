#!/usr/bin/python3
"""Initialization of the 'models' module"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
