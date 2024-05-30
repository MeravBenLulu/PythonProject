import http

from app.models.income import Income
from app.db_management.config_db import incomes


async def get_all_incomes():
    """
    Retrieves all incomes from the database.

    Returns:
        list: A list of Income instances representing all incomes in the system.
    """
    incomes.find()
    return [Income(**income) for income in incomes.find()]


async def get_income(name:str):
    """
    Retrieves a income from the database by name and password.

    Args:
        name (str): The name of the income.
    Returns:
        dict: Information about the income if found.

    Raises:
        Exception: If the income does not exist, raises an Exception with status code 400.
    """
    query = {"name": name}
    projection = {"_id": 0, "name": 1, "amount":1}
    response = incomes.find_one(query, projection)
    if response is None:
        raise Exception("income not exists")
    return response


async def add_incom(income: Income):
    """
    Adds a new income to the database.

    Args:
        income (Incom): An instance of Incom representing the income to be added.

    Returns:
        dict: Information about the income that was added.

    Raises:
        Exception: If the income already exists, raises an Exception with status code 400.
    """
    income_dict = dict(income)
    print("Income to be inserted:", income_dict)
    find_incom = incomes.find_one({"name": income_dict.get("name")})
    if find_incom is not None:
        raise Exception("income already exists")
    inserted_income = incomes.insert_one(income_dict)
    return {
        "_id": str(inserted_income.inserted_id),
        "name": income_dict["name"],
        "amount": income_dict["amount"],
    }

async def update_incom(name: str, updated_income: Income):
    income_dict = dict(updated_income)

    query = {"name": name}
    find_income = incomes.find_one(query)
    if find_income is None:
        raise Exception("Income does not exist")

    update_data = {"$set": income_dict}
    incomes.update_one(query, update_data)

async def delete_income(name:str):
    """
    delete a income from the database by name and password.

    Args:
        name (str): The name of the income.
    Returns:
        dict: Information about the income if found.

    Raises:
        Exception: If the income does not exist, raises an Exception with status code 400.
    """
    query = {"name": name}
    response = incomes.delete_one(query)
    if response is None:
        raise Exception("income not exists")
    return response