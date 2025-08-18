import uuid
import datetime
from models import storage

"""Module contains the base model that defines all commmon attributes"""


class BaseModel:
    """Basemodel defines all common attributees/methods for other
    classes"""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize instances attributes from kwargs or defaults."""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('updated_at', 'created_at'):
                        value = datetime.datetime.fromisoformat(value)
                        setattr(self, key, value)
        if not hasattr(self, "id"):
            self.id = str(uuid.uuid4())
        if not hasattr(self, 'created_at'):
            self.created_at = datetime.datetime.now()
        if not hasattr(self, "updated_at"):
            self.updated_at = self.created_at
        storage.new(self)

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self) -> None:
        """Updates updated_at with the current time"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """Returns a dictionary of instances attributes, wISO format"""

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
