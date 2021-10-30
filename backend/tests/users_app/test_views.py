import pytest
from django.urls import reverse_lazy, reverse

pytestmark = pytest.mark.django_db
class TestUserRegisterAPIView:

    def test_views__user_register_api_view_valid(self, api_client, validated_user_data):
        url = reverse("ep-register-user")
        response = api_client.post(url, validated_user_data, format='json')

        assert response.status_code == 201
        assert response.data["email"] == validated_user_data["email"]
        assert response.data["user_id"]

    def test_views__user_register_api_view_no_password(self, api_client, invalid_user_data_no_password):
        url = reverse("ep-register-user")
        response = api_client.post(url, invalid_user_data_no_password, format='json')

        assert response.status_code == 400

    def test_views__user_register_api_view_no_email(self, api_client, invalid_user_data_no_email):
        url = reverse("ep-register-user")
        response = api_client.post(url, invalid_user_data_no_email, format='json')

        assert response.status_code == 400


class TestUserUpdateAPIView:
    
    def test_user_update_valid(self, api_client, validated_user_data, validated_data):
        create_user_url = reverse("ep-register-user")
        response1 = api_client.post(
            create_user_url, 
            validated_user_data,
            format="json"
        )
        update_user_url = reverse(
            "ep-update-user", 
            kwargs={"user_id":response1.data["user_id"]}
        )

        obtain_token_url = reverse(
            "ep-token-obtain-pair",
        )
        response2 = api_client.post(
            obtain_token_url,
            validated_user_data,
            format="json"
        )
        
        access_token = response2.data["access"]
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        response3 = api_client.put(
            update_user_url,
            validated_data,
            format="json"
        )

        assert response3.status_code == 200
        assert response3.data["full_name"]

    def test_user_update_invalid(self, api_client, validated_user_data, invalid_data):
        create_user_url = reverse("ep-register-user")
        response1 = api_client.post(
            create_user_url, 
            validated_user_data,
            format="json"
        )
        update_user_url = reverse(
            "ep-update-user", 
            kwargs={"user_id":response1.data["user_id"]}
        )


        obtain_token_url = reverse(
            "ep-token-obtain-pair",
        )
        response2 = api_client.post(
            obtain_token_url,
            validated_user_data,
            format="json"
        )
        
        access_token = response2.data["access"]
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        response3 = api_client.put(
            update_user_url,
            invalid_data,
            format="json"
        )

        assert response3.status_code == 400

class TestUserRetrieveAPIView:

    def test_user_retrieve(self, api_client, validated_user_data):
        create_user_url = reverse("ep-register-user")
        response1 = api_client.post(
            create_user_url, 
            validated_user_data,
            format="json"
        )
        retrieve_user_url = reverse(
            "ep-retrieve-user",
            kwargs={"user_id": response1.data["user_id"]}
        )

        obtain_token_url = reverse(
            "ep-token-obtain-pair",
        )
        response2 = api_client.post(
            obtain_token_url,
            validated_user_data,
            format="json"
        )

        access_token = response2.data["access"]
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        response3 = api_client.get(retrieve_user_url)

        assert response3.status_code == 200
        assert response3.data["email"]