#!/usr/bin/python3

import cmd
from datetime import datetime
import uuid

"""Base model in which all other classes inherits from"""


class BaseModel:
    """Initializes all the argyments"""
    def __init__(self, *args, **kwargs):
        """ Initializes the public instance attributes
        Args:
            line (str): The additional arguments passed to the command line
            id: Assign a unique id
            created_at: Assigns the current datetime
            updated_at: Assigns the current dattime
            """
        if (kwargs):
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns an official string rep of the class"""

        return f"[{self.__class__.__name__}] ({self.id} {self.__dict__}"

    def save(self):
        """Updates the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary"""
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return (dict_copy)
