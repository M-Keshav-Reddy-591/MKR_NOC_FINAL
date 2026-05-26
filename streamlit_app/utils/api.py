import requests

BASE_URL = "http://127.0.0.1:8000/api/v1"


def login_user(emp_id, password, role):

    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "emp_id": emp_id,
            "password": password,
            "role": role
        }
    )

    return response