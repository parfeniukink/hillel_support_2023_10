import requests


def test_user_create():
    url = "http://localhost:8000/users"

    payload = {
        "username": "test",
        "password": "test",
        "email": "john@email.com",
        "first_name": "John",
        "last_name": "Doe",
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201
