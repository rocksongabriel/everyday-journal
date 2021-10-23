from django.urls import path
from .views import UserRegisterAPIView


urlpatterns = [
    path('users/account/register/', UserRegisterAPIView.as_view(), name="ep-register-user")
]
