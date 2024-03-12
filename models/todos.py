from pydantic import BaseModel # data validation and manipulation
from typing import Optional   # Importing Optional from typing for optional fields


# Define the User class which inherits from BaseModel for data validation
class User(BaseModel):
    username: str
    password: str

# Define the Contact class which inherits from BaseModel for data validation
class Contact(BaseModel):   
    ContactId: str
    name: Optional[str]
    MOB: str
    username: str
    Group: Optional[str]
    email: Optional[str]