from fastapi import APIRouter, HTTPException, Depends
from models.todos import Contact, User
from config.db import collection_name, authentication_DB
from schema.schemas import list_serial, user_serial
from bson import ObjectId
from .auth import authenticate_user, oauth2_scheme
from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Store user name and password
@router.post("/add/user")
async def Add_User(usr: User):
    try:
        hashed_password = pwd_context.hash(usr.password)
        new_user = User(username=usr.username, password=hashed_password)
        authentication_DB.insert_one(dict(new_user))
        return {"message": "User Added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get User request
@router.get('/find/contacts')
async def find_all_contact_of_current_user(current_user: User = Depends(authenticate_user)):
    try:
        if not current_user:
            raise HTTPException(status_code=401, detail="Invalid token, Please come with correct credentials.")
        todos = list_serial(collection_name.find({"username":current_user.username}))
        return todos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# post request method for writing contacts of current user in the db.
@router.post("/create/contacts")
async def Post_contact_of_current_user(todo: Contact, current_user: User = Depends(authenticate_user)):
    try:
        if not current_user:
            raise HTTPException(status_code=401, detail="Invalid token, Please come with correct credentials.")
        collection_name.insert_one(dict(todo))
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Put request method Update in DB
@router.put("/{id}")
async def update_user(id: str, todo: Contact, current_user: User = Depends(authenticate_user)):
    try:
        if not current_user:
            raise HTTPException(status_code=401, detail="Invalid token, Please come with correct credentials.")
        user_data = collection_name.find_one(ObjectId(id))
        if (user_data["username"] != current_user.username):
            raise HTTPException(status_code=401, detail="Contact not present for the current user")
        collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
        return {"message": "User updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Delete request method
@router.delete("/{id}")
async def delete_User(id: str, current_user: User = Depends(authenticate_user)):
    try:
        if not current_user:
            raise HTTPException(status_code=401, detail="Invalid token, Please come with correct credentials.")
        user_data = collection_name.find_one(ObjectId(id))
        if (user_data["username"] != current_user.username):
            raise HTTPException(status_code=401, detail="Contact not present for the current user")
        collection_name.find_one_and_delete({"_id": ObjectId(id)})
        return {"message": "Contact deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/search/relation/{relation}")
async def search_user_by_relationship(relation: str, current_user: User = Depends(authenticate_user)):
    try:
        if not current_user:
            raise HTTPException(status_code=401, detail="Invalid token, Please come with correct credentials.")
        users = list_serial(collection_name.find({"Group":relation, "username":current_user.username}))
        if not users:
            raise HTTPException(status_code=404, detail="Contacts not found")
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
