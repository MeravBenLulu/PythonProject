import pytest
from starlette.testclient import TestClient

from app.models.income import Income
from main import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_get_all_incomes(client):
    response = client.get("/income/all")
    assert response.status_code == 200


def test_get_income(client):
    response = client.get("/income/get_income?name=test_inc")
    assert response.status_code == 400
    response2 = client.get("/income/get_income?name=test_income")
    assert response2.status_code == 200


def test_add_income(client):
    income_data = {
        "_id": "1",
        "name": "איפור לרותי",
        "amount":150
    }
    income = Income(**income_data)
    response = client.post("/income/add_income", json=income.dict())
    assert response.status_code == 200
    assert response.json()["id"] == income_data["id"]
    assert response.json()["name"] == income_data["name"]
    assert response.json()["amount"] == income_data["amount"]
    income_data2 = {
        "_id": "1",
        "name": "עבודה בחנות",
        "amount":200
    }
    income2 = Income(**income_data2)
    print(income2)
    response2 = client.post("/income/add_income", json=income2.dict())
    assert response2.status_code == 400


def test_update_income(client):
    # Prepare test data
    test_income_data = {
        "_id": "1",
        "name": "test_income",
        "amount":8
    }
    new_data = {
        "_id": "1",
        "name": "test2",
        "amount":2
    }
    # Call the update_income function
    updated_income = client.put(f"/income/update?name={test_income_data['name']}",
                              json=new_data)
    # Assert that the income has been updated correctly
    print(updated_income)
    assert updated_income.status_code == 200

def test_delete_income(client):
    response = client.delete("/income/delete_income?name=test_inc")
    assert response.status_code == 400
    response2 = client.delete("/income/delete_income?name=test_income")
    assert response2.status_code == 200