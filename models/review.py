#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class of BaseModel that contains thes attrs:
    place_id, user_id, & text"""
    place_id = ''
    user_id = ''
    text = ''
