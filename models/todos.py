from pydantic import BaseModel # data validation and manipulation
# from enum import Enum

# class RelationEnum(Enum):
#     FRIEND = "FRIEND"
#     FAMILY = "FAMILY"
#     COLLEAGUE = "COLLEAGUE"
#     OTHERS = "OTHERS"
class User(BaseModel):
    name: str
    email: str
    PhoneNo: str
    password: str
    Relation: str

# def dict(self):
#     user_dict = {
#         'name': self.name,
#         'email': self.email,
#         'phone': self.phone,
#         'password': self.password,
#         'relation': self.relation.value
#     }
#     return user_dict