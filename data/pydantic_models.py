from pydantic import BaseModel
from data.model_enums import Catagory

class Message(BaseModel):
    name: str
    message: str
    datetime: str
    email: str
    catagory: Catagory