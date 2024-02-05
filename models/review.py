#!/usr/bin/python3
""" Define review subclass that inherits from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Define review subclass that inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""
