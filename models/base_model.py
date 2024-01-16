#!/usr/bin/pyhon3

"""BaseMode1 module"""

import uuid
from datetime import datetime


class BaseMode1:
    """BaseMode1 class"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseMode1"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """String representation of BaseMode1"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update Updated_at with the current datetime"""
        self.updated_at = datetime.now()
        

    def to_dict(self):
        """Convert instance to dictionary"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dictecho "help" | ./console.py

    def from_dict(self, dict_data):
        """Create instance from dictionary data"""
        pass
