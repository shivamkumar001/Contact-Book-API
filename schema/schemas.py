def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "email": todo["email"],
        "PhoneNo": todo["PhoneNo"],
        "password": todo["password"],
        "Relation": todo["Relation"]
    }

def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]