import http

from app.models.expenditure import Expenditure
from app.db_management.config_db import expenses


async def get_all_expenses():
    """
    Retrieves all expenses from the database.

    Returns:
        list: A list of Expenditure instances representing all expenses in the system.
    """
    expenses.find()
    return [Expenditure(**expenditure) for expenditure in expenses.find()]


async def get_expenditure(name:str):
    """
    Retrieves a expenditure from the database by name and password.

    Args:
        name (str): The name of the expenditure.
    Returns:
        dict: Information about the expenditure if found.

    Raises:
        Exception: If the expenditure does not exist, raises an Exception with status code 400.
    """
    query = {"name": name}
    projection = {"_id": 0, "name": 1, "amount":1}
    response = expenses.find_one(query, projection)
    if response is None:
        raise Exception("expenditure not exists")
    return response


async def add_expenditure(expenditure: Expenditure):
    """
    Adds a new expenditure to the database.

    Args:
        expenditure (expenditure): An instance of expenditure representing the expenditure to be added.

    Returns:
        dict: Information about the expenditure that was added.

    Raises:
        Exception: If the expenditure already exists, raises an Exception with status code 400.
    """
    expenditure_dict = dict(expenditure)
    print("Expenditure to be inserted:", expenditure_dict)
    find_expenditure = expenses.find_one({"name": expenditure_dict.get("name")})
    if find_expenditure is not None:
        raise Exception("expenditure already exists")
    inserted_expenditure = expenses.insert_one(expenditure_dict)
    return {
        "_id": str(inserted_expenditure.inserted_id),
        "name": expenditure_dict["name"],
        "amount": expenditure_dict["amount"],
    }

async def update_expenditure(name: str, updated_expenditure: Expenditure):
    expenditure_dict = dict(updated_expenditure)

    query = {"name": name}
    find_expenditure = expenses.find_one(query)
    if find_expenditure is None:
        raise Exception("Expenditure does not exist")

    update_data = {"$set": expenditure_dict}
    expenses.update_one(query, update_data)

async def delete_expenditure(name:str):
    """
    delete a expenditure from the database by name and password.

    Args:
        name (str): The name of the expenditure.
    Returns:
        dict: Information about the expenditure if found.

    Raises:
        Exception: If the expenditure does not exist, raises an Exception with status code 400.
    """
    query = {"name": name}
    response = expenses.delete_one(query)
    if response is None:
        raise Exception("expenditure not exists")
    return response