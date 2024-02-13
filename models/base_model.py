#!/usr/bin/python3
import uuid
from datetime import datetime
import models

""" modelBase """

class BaseModel:
    """ Defines shared attributes and methods for derived classes """

    def __init__(self, *args, **kwargs):
        """ Initialize an instance potentially with a dictionary argument """
        if kwargs:
            for attr, value in kwargs.items():
                if attr in ["created_at", "updated_at"]:
                    setattr(self, attr, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif attr != "__class__":
                    setattr(self, attr, value)
        if "id" not in kwargs:
            self.id = str(uuid.uuid4())
        if "created_at" not in kwargs:
            self.created_at = datetime.now()
        if "updated_at" not in kwargs:
            self.updated_at = datetime.now()
        if not kwargs or len(kwargs) ==  0:
            models.storage.new(self)

    def __str__(self):
        """ Override string special method """
        repr_str = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return repr_str

    def save(self):
        """ Update updated_at with current time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dict with keys and values of __dict__ of the instance """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        return new_dict
