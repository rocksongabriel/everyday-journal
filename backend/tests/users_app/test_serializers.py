import pytest

from users.api.serializers import User, UserProfileSerializer, UserRegisterSerializer, UserUpdateSerializer

pytestmark = pytest.mark.django_db


# Tests

class TestUserRegisterSerializer:

    def test_serialization(self, user_factory):
        user = user_factory()
        serializer = UserRegisterSerializer(user)

        assert serializer.data

    def test_deserialization(self,validated_user_data):
        serializer = UserRegisterSerializer(data=validated_user_data)

        if serializer.is_valid():
            user = serializer.save()
        assert user.email == serializer.validated_data["email"]
    

class TestUserUpdateSerializer:

    def test_serilization(self, user_factory):
        user = user_factory()
        serializer = UserUpdateSerializer(user)

        assert serializer.data

    def test_deserialization(self, user_factory, validated_data):
        user = user_factory()
        serializer = UserUpdateSerializer(user, data=validated_data)

        if serializer.is_valid():
            serializer.save()
        
        assert serializer.data.get("full_name")
        assert serializer.data["age"]
        assert serializer.data["bio"]


class TestUserRetrieveSerializer:

    def test_serialization(self):
        user = User.objects.create(
            email="testemail.com",
            password="testpass1234",
            full_name="Test User",
            bio="Let's do this",
            age=29,
        )

        serializer = UserProfileSerializer(user)
        assert serializer.data