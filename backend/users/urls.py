from django.urls import path
from .views import UserRegisterAPIView, UserRetrieveAPIView


urlpatterns = [
    path('users/account/register/', UserRegisterAPIView.as_view(), name="ep-register-user"),
    path('users/account/retrieve/<uuid:user_id>/', UserRetrieveAPIView.as_view(), name="ep-retrieve-user")
]
