import pytest
import allure
from api_common import users_api
from common.assertions import assert_status_code
from faker import Faker

faker = Faker()

def random_username():
    return faker.user_name() + faker.pystr(min_chars=3, max_chars=5)

def random_email():
    return faker.email()

@allure.title("Create normal user")
def test_create_user_normal():
    payload = {"username": random_username(), "email": random_email(), "password": "123456"}
    resp = users_api.create_user(payload)
    assert_status_code(resp, 200)

@allure.title("Create user with invalid email")
def test_create_user_invalid_email():
    payload = {"username": random_username(), "email": "bad-email", "password": "123456"}
    resp = users_api.create_user(payload)
    assert_status_code(resp, 400)

@allure.title("Create user missing username")
def test_create_user_missing_username():
    payload = {"email": random_email(), "password": "123456"}
    resp = users_api.create_user(payload)
    assert_status_code(resp, 400)

@allure.title("Create duplicate user")
def test_create_user_duplicate():
    username = random_username()
    email = random_email()
    payload = {"username": username, "email": email, "password": "123456"}
    users_api.create_user(payload)
    resp = users_api.create_user(payload)
    assert_status_code(resp, 400)

@allure.title("Get user normal")
def test_get_user_normal():
    payload = {"username": random_username(), "email": random_email(), "password": "123456"}
    user = users_api.create_user(payload).json()["data"]
    resp = users_api.get_user(user["id"])
    assert_status_code(resp, 200)

@allure.title("Get user not found")
def test_get_user_not_found():
    resp = users_api.get_user(99999)
    assert_status_code(resp, 404)

@allure.title("Update user email normal")
def test_update_user_email_normal():
    payload = {"username": random_username(), "email": random_email(), "password": "123456"}
    user = users_api.create_user(payload).json()["data"]
    resp = users_api.update_user(user["id"], {"email": random_email()})
    assert_status_code(resp, 200)

@allure.title("Update user with invalid email")
def test_update_user_invalid_email():
    payload = {"username": random_username(), "email": random_email(), "password": "123456"}
    user = users_api.create_user(payload).json()["data"]
    resp = users_api.update_user(user["id"], {"email": "bad-email"})
    assert_status_code(resp, 400)

@allure.title("Delete user normal")
def test_delete_user_normal():
    payload = {"username": random_username(), "email": random_email(), "password": "123456"}
    user = users_api.create_user(payload).json()["data"]
    resp = users_api.delete_user(user["id"])
    assert_status_code(resp, 200)

@allure.title("Delete non-existent user")
def test_delete_nonexistent_user():
    resp = users_api.delete_user(999999)
    assert_status_code(resp, 404)

@allure.title("List users pagination")
def test_list_users_pagination():
    # Auto-generate 15 users
    for _ in range(15):
        payload = {"username": random_username(), "email": random_email(), "password": "123456"}
        resp = users_api.create_user(payload)
        assert_status_code(resp, 200)

    # Page 1
    resp = users_api.list_users(page=1, size=10)
    assert_status_code(resp, 200)
    data = resp.json()["data"]
    assert len(data["list"]) == 10
    assert data["total"] == 15

@allure.title("List users with keyword search")
def test_list_users_with_keyword():
    created_users = []
    for _ in range(10):
        payload = {"username": random_username(), "email": random_email(), "password": "123456"}
        resp = users_api.create_user(payload)
        assert_status_code(resp, 200)
        created_users.append(resp.json()["data"]["username"])

    username = created_users[0]
    resp = users_api.list_users(page=1, size=10, keyword=username[:4])
    assert_status_code(resp, 200)
    data = resp.json()["data"]
    assert any(username == u["username"] for u in data["list"])
