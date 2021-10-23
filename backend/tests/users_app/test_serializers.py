import pytest

from users.api.serializers import UserRegisterSerializer

pytestmark = pytest.mark.django_db

# Fixtures

@pytest.fixture
def validated_user_data():
    return {
        "email": "testmail@gmail.com",
        "password": "testpass1234"
    }


# Tests

class TestUserRegisterSerializer:

    def test_user_serializer__serialization(self, user_factory):
        user = user_factory()
        serializer = UserRegisterSerializer(user)

        assert serializer.data

    def test_user_serializer__deserialization(self,validated_user_data):
        serializer = UserRegisterSerializer(data=validated_user_data)

        if serializer.is_valid():
            user = serializer.save()
        assert user.email == serializer.validated_data["email"]
    