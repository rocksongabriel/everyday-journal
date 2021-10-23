import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Factory for a user model"""
    email = "testuser@gmail.com"
    password = factory.PostGenerationMethodCall(
        "set_password", "testpass1234"
    )

    class Meta:
        model = "users.User"