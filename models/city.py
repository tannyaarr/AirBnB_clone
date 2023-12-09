#!/usr/bin/python3
"""Defines the City module"""

from models.base_model import BaseModel


class City(BaseModel):
    """city class that inherits from baseModel"""
    state_id = ""
    name = ""
