import http

from app.models.user import User
from app.db_management.config_db import users


async def get_all_users():
    """
    Retrieves all users from the database.

    Returns:
        list: A list of User instances representing all users in the system.
    """
    users.find()
    return [User(**user) for user in users.find()]


async def get_user(name: str, password: str):
    """
    Retrieves a user from the database by name and password.

    Args:
        name (str): The name of the user.
        password (str): The password of the user.

    Returns:
        dict: Information about the user if found.

    Raises:
        Exception: If the user does not exist, raises an Exception with status code 400.
    """
    query = {"name": name, "password": password}
    projection = {"_id": 0, "name": 1, "password": 1, "age": 1, "city": 1}
    response = users.find_one(query, projection)
    if response is None:
        raise Exception("user not exists")
    return response


async def add_user(user: User):
    """
    Adds a new user to the database.

    Args:
        user (User): An instance of User representing the user to be added.

    Returns:
        dict: Information about the user that was added.

    Raises:
        Exception: If the user already exists, raises an Exception with status code 400.
    """
    user_dict = dict(user)
    print("User to be inserted:", user_dict)
    find_user = users.find_one({"name": user_dict.get("name"), "password": user_dict.get("password")})
    if find_user is not None:
        raise Exception("user already exists")
    inserted_user = users.insert_one(user_dict)
    return {
        "_id": str(inserted_user.inserted_id),
        "name": user_dict["name"],
        "age": user_dict["age"],
        "city": user_dict["city"]
    }

async def update_user(name: str, password: str, updated_user: User):
    user_dict = dict(updated_user)

    query = {"name": name, "password": password}
    find_user = users.find_one(query)
    if find_user is None:
        raise Exception("User does not exist")

    update_data = {"$set": user_dict}
    users.update_one(query, update_data)