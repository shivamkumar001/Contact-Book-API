from pymongo import MongoClient

client = MongoClient("mongodb+srv://shivam9399kumar:password1234@mongoshivam.9edgrg8.mongodb.net/?retryWrites=true&w=majority&appName=MongoShivam")

db = client.ContactBookDB

collection_name = db["todo_collection"]
authentication_DB = db["authenticateDB"]