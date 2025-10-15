import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"

def create_user(payload):
    return requests.post(f"{BASE_URL}/users", json=payload)

def get_user(user_id):
    return requests.get(f"{BASE_URL}/users/{user_id}")

def update_user(user_id, payload):
    return requests.put(f"{BASE_URL}/users/{user_id}", json=payload)

def delete_user(user_id):
    return requests.delete(f"{BASE_URL}/users/{user_id}")

def list_users(page=1, size=10, keyword=""):
    return requests.get(f"{BASE_URL}/users", params={"page": page, "size": size, "keyword": keyword})

def reset_users():
    return requests.post(f"{BASE_URL}/reset")
