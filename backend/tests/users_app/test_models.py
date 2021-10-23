import pytest
from django.contrib.auth import get_user_model
from users.models import CustomUserManager

User = get_user_model()

pytestmark = pytest.mark.django_db

class TestCustomUser:


    def test_user__create_user(self, user_factory):
        user = user_factory()
        assert user.email == "testuser@gmail.com"
        assert user.check_password("testpass1234")
        assert User.objects.count() == 1

    def test_custom_user_manager__raises_value_error(self):
        with pytest.raises(ValueError):
            user = User.objects.create_user(email=None,password="testpass1234")

    def test_custom_user_manager__create_user(self):
        user = User.objects.create_user("testmail@gmail.com", "testpass1234")
        assert user.email == "testmail@gmail.com"
        assert isinstance(user, User)

    def test_custom_user_manager__create_superuser(self):
        user = User.objects.create_superuser("admin@gmail.com", "testpass1234")
        assert user.email == "admin@gmail.com"
        assert isinstance(user, User)
