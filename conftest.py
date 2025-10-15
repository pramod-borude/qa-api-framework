import pytest
from api import users_api

@pytest.fixture(autouse=True)
def clear_users():
    """
    Reset USERS before each test
    """
    users_api.reset_users()
    yield
    users_api.reset_users()
