from fastapi import APIRouter, HTTPException, status, Depends

from models.todos import Contact, User
from config.db import collection_name, authentication_DB
from schema.schemas import list_serial, user_serial
from bson import ObjectId
# from .auth import get_current_user
from .auth import authenticate_user, oauth2_scheme
from passlib.context import CryptContext

router = APIRouter()

# @router.get("/protected")
# async def read_protected_route(token: str = Depends(oauth2_scheme)):
#     return {"message": "This is a protected route"}

# Store user name and password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/add/user")
async def Add_User(usr: User):
    hashed_password = pwd_context.hash(usr.password)
    new_user = User(username=usr.username, password=hashed_password)
    authentication_DB.insert_one(dict(new_user))
    return {"message": "User Added successfully"}

@router.post("/store-data")
async def store_data(contact: Contact, current_user: User = Depends(authenticate_user)):
    # Only authenticated users can access this endpoint
    # Store data in collection_name

    collection_name.insert_one({"username": current_user.username, "data": dict(contact)})
    return {"message": "Data stored successfully"}

# Get User request
@router.get('/')
async def find_all_users(token: str = Depends(authenticate_user)):
    todos = list_serial(collection_name.find()) # find everything in the collection and return it
    return todos

# POST request method Write in DB
@router.post("/")
@router.post("/")
async def Post_User(todo: Contact, current_user: User = Depends(authenticate_user)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Invalid token")
    collection_name.insert_one(dict(todo))
    return {"message": "User created successfully"}

# Put request  method Update in DB
@router.put("/{id}")
async def update_user(id: str, todo: Contact, token: str = Depends(authenticate_user)):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    return {"message": "User updated successfully"}

# Delete request method
@router.delete("/{id}")
async def delete_User(id: str, token: str = Depends(authenticate_user)):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "User deleted successfully"}

# Basic search based on name 
@router.get("/search/name/{name}")
async def search_user_by_name(name: str, token: str = Depends(authenticate_user)):
    #name = name.strip().lower()
    users = list_serial(collection_name.find({"name":name}))
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    return users

# Show User on the basis of Group 
@router.get("/search/relation/{relation}")
async def search_user_by_relationship(relation: str, token: str = Depends(authenticate_user)):
    users = list_serial(collection_name.find({"Relation":relation}))
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    return users