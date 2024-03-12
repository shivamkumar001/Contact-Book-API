def individual_user(usr) -> dict:
    return {
        "user_id": str(usr["_user_id"]),
        "username": usr["username"],
        "password": usr["password"]
    }

def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "ContactId": todo["ContactId"],
        "name"  : todo["name"],
        "MOB": todo["MOB"],
        "username": todo["username"],
        "Group": todo["Group"],
        "email": todo["email"]
    }

def user_serial(users) -> list:
    return [individual_user(usr) for usr in users]

def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]

