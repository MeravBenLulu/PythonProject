import pytest
from starlette.testclient import TestClient

from app.models.user import User
from main import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_get_all_users(client):
    response = client.get("/user/all")
    assert response.status_code == 200


def test_sign_in(client):
    response = client.get("/user/sign_in?name=test_use&password=test_password")
    assert response.status_code == 400
    response2 = client.get("/user/sign_in?name=test_user&password=test_password")
    assert response2.status_code == 200


def test_sign_up(client):
    user_data = {
        "_id": "1",
        "name": "shimoni",
        "password": "123456",
        "age": 25,
        "city": "bne- brak"
    }
    user = User(**user_data)
    response = client.post("/user/sign_up", json=user.dict())
    assert response.status_code == 200
    assert response.json()["name"] == user_data["name"]
    assert response.json()["age"] == user_data["age"]
    assert response.json()["city"] == user_data["city"]
    user_data2 = {
        "_id": "1",
        "name": "test",
        "password": "test",
        "age": 25,
        "city": "Wonderland"
    }
    user2 = User(**user_data2)
    print(user2)
    response2 = client.post("/user/sign_up", json=user2.dict())
    assert response2.status_code == 400


def test_update_user(client):
    # Prepare test data
    test_user_data = {
        "_id": "1",
        "name": "test_user",
        "password": "test_password",
        "age": 30,
        "city": "TestCity"
    }
    new_data = {
        "_id": "1",
        "name": "test2",
        "password": "test2psw",
        "age": 30,
        "city": "TestCity"
    }
    # Call the update_user function
    updated_user = client.put(f"/user/update?name={test_user_data['name']}&password={test_user_data['password']}",
                              json=new_data)
    # Assert that the user has been updated correctly
    print(updated_user)
    assert updated_user.status_code == 200
def test_update_user(client):
    user_credentials = {
        "name": "a",
        "password": "a"
    }
    updated_user_data = {
        "name": "updated_name",
        "password": "updated_password",
        "age": 30,
        "city": "updated_city"
    }
    response = client.put("/user/update_user/a/a", json=updated_user_data)
    assert response.status_code == 200