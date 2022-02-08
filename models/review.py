#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """the review class contains a place, user and text"""
    place_id = ''
    user_id = ''
    text = ''
