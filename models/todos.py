from pydantic import BaseModel # data validation and manipulation
from typing import Optional
# from enum import Enum

class User(BaseModel):
    username: str
    password: str

class Contact(BaseModel):
    ContactId: str
    name: Optional[str]
    MOB: str
    username: str
    Group: Optional[str]
    email: Optional[str]