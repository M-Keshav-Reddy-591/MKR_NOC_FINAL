import requests

BASE_URL = "http://127.0.0.1:8000/api/v1"


def get_dashboard_stats():

    return requests.get(
        f"{BASE_URL}/dashboard/stats"
    )


def get_employees():

    return requests.get(
        f"{BASE_URL}/employees"
    )