from django.urls import path
from .views import UserRegisterAPIView, UserRetrieveAPIView, UserUpdateAPIView


urlpatterns = [
    path('users/account/register/', UserRegisterAPIView.as_view(), name="ep-register-user"),
    path('users/account/retrieve/<uuid:user_id>/', UserRetrieveAPIView.as_view(), name="ep-retrieve-user"),
    path('users/account/update/<uuid:user_id>/', UserUpdateAPIView.as_view(), name="ep-update-user"),
]
