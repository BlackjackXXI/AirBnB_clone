#!/usr/bin/python3
""" Define user subclass that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Define user subclass that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
