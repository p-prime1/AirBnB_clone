import json
"""Module contains a class that serializes and desirializes"""


class FileStorage:
    """Class serializes desirializes instance to and from a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        return self.__objects


    def new(self, obj) -> None:
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj


    def save(self) -> None:
        with open(self.__file_path, "w") as f:
            obj_dict = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(obj_dict, f)


    def reload(self) -> None:
        try:
            from models.base_model import BaseModel
            classes = {"BaseModel": BaseModel}

            with open(self.__file_path, "r") as f:
                content = json.load(f)
                if not content:
                    return
            for key, value in content.items():
                cls_name = value["__class__"]
                cls = classes.get(cls_name)
                self.__objects[key] = cls(**value)

        except (FileNotFoundError, json.JSONDecodeError):
            pass
