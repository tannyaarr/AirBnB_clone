#!/usr/bin/python3
"""Defines the review model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
