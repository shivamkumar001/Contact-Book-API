from fastapi import APIRouter, HTTPException

from models.todos import User#,RelationEnum
from config.db import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

# Get User request
@router.get('/')
async def find_all_users():
    todos = list_serial(collection_name.find()) # find everything in the collection and return it
    return todos

# POST request method Write in DB
@router.post("/")
async def Post_User(todo: User):
    collection_name.insert_one(dict(todo))
    return {"message": "User created successfully"}

# Put request  method Update in DB
@router.put("/{id}")
async def update_user(id: str, todo: User):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    return {"message": "User updated successfully"}

# Delete request method
@router.delete("/{id}")
async def delete_User(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "User deleted successfully"}

# Basic search based on name 
@router.get("/search/name/{name}")
async def search_user_by_name(name: str):
    #name = name.strip().lower()
    users = list_serial(collection_name.find({"name":name}))
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    return users

# Show User on the basis of Group 
@router.get("/search/relation/{relation}")
async def search_user_by_relationship(relation: str):
    users = list_serial(collection_name.find({"Relation":relation}))
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    return users