import pytest
from django.urls import reverse_lazy, reverse


@pytest.mark.django_db
def test_views__user_register_api_view_valid(api_client, validated_user_data):
    url = reverse("ep-register-user")
    response = api_client.post(url, validated_user_data, format='json')

    assert response.status_code == 201
    assert response.data["email"] == validated_user_data["email"]

@pytest.mark.django_db
def test_views__user_register_api_view_no_password(api_client, invalid_user_data_no_password):
    url = reverse("ep-register-user")
    response = api_client.post(url, invalid_user_data_no_password, format='json')

    assert response.status_code == 400

@pytest.mark.django_db
def test_views__user_register_api_view_no_email(api_client, invalid_user_data_no_email):
    url = reverse("ep-register-user")
    response = api_client.post(url, invalid_user_data_no_email, format='json')

    assert response.status_code == 400
