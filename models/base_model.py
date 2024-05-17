#!/usr/bin/python3

import cmd
from datetime import datetime
import uuid

"""Base model in which all other classes inherits from"""

class BaseModel(cmd.Cmd):
    """Initializes all the argyments"""
    def __init__(self):
        """ Initializes the public instance attributes
        Args:
            line (str): The additional arguments passed to the command line
            id: Assign a unique id when an instance is created
            created_at: Assigns the current datetime when an instance is created
            updated_at: Assigns the current dattime and updates every time an object is changed
            """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = selfcreated_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id} {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all kys/valued of __dic__ of the instance"""
        return (self.__dict__.copy())

