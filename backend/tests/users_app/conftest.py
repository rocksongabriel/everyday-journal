from pytest_factoryboy import register
import pytest

from .factories import UserFactory

register(UserFactory)


# Fixtures

@pytest.fixture
def validated_user_data():
    return {
        "email": "testmail@gmail.com",
        "password": "testpass1234"
    }

@pytest.fixture
def validated_data():
    return {
        "full_name": "Test User",
        "age": 19,
        "bio": "Very powerful journaler"
    }

@pytest.fixture
def invalid_user_data_no_password():
    return {
        "email": "testmail@gmail.com"
    }

@pytest.fixture
def invalid_user_data_no_email():
    return {
        "password": "testpass1234"
    }

