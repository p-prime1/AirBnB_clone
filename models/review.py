from .base_model import BaseModel
"""Module contains the Review class"""


class Review(BaseModel):
    place_id:str = ""
    user_id:str = ""
    text:str = ""
