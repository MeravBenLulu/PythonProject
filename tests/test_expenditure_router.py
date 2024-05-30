import pytest
from starlette.testclient import TestClient

from app.models.expenditure import Expenditure
from main import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_get_all_expenses(client):
    response = client.get("/expenditure/all")
    assert response.status_code == 200


def test_get_expenses(client):
    response = client.get("/expenditure/get_expenditure?name=test_ex")
    assert response.status_code == 400
    response2 = client.get("/expenditure/get_expenditure?name=test_expenditure")
    assert response2.status_code == 200


def test_add_expenditure(client):
    expenditure_data = {
        "_id": "1",
        "name": "קניות",
        "amount":150
    }
    expenditure = Expenditure(**expenditure_data)
    response = client.post("/expenditure/add_expenditure", json=expenditure.dict())
    assert response.status_code == 200
    assert response.json()["id"] == expenditure_data["id"]
    assert response.json()["name"] == expenditure_data["name"]
    assert response.json()["amount"] == expenditure_data["amount"]
    expenditure_data2 = {
        "_id": "1",
        "name": "אבידה",
        "amount":200
    }
    expenditure2 = Expenditure(**expenditure_data2)
    print(expenditure2)
    response2 = client.post("/expenditure/add_expenditure", json=expenditure2.dict())
    assert response2.status_code == 400


def test_update_expenditure(client):
    # Prepare test data
    test_expenditure_data = {
        "_id": "1",
        "name": "test_expenditure",
        "amount":8
    }
    new_data = {
        "_id": "1",
        "name": "test2",
        "amount":2
    }
    # Call the update_income function
    updated_expenditure = client.put(f"/expenditure/update?name={test_expenditure_data['name']}",
                              json=new_data)
    # Assert that the expenditure has been updated correctly
    print(updated_expenditure)
    assert updated_expenditure.status_code == 200

def test_delete_expenditure(client):
    response = client.delete("/expenditure/delete_expenditure?name=test_ex")
    assert response.status_code == 400
    response2 = client.delete("/expenditure/delete_expenditure?name=test_expenditure")
    assert response2.status_code == 200