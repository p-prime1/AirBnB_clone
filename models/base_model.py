from types import NoneType
import uuid
import datetime

"""Module contains the base model that defines all commmon attributes"""


class BaseModel:
    """Basemodel defines all common attributees/methods for other
    classes"""

    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self) -> None:
        """Updates updated_at with the current time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self) -> dict:
        """Returns a dictionary containing al key/values of __dict__
        includeing the class name,
        and with updated_at and created_at in ISO format"""

        new_dict = {}
        for key, value in self.__dict__.items():
            new_dict[key] = value

        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
