from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.api.serializers import UserProfileSerializer, UserRegisterSerializer, UserUpdateSerializer

User = get_user_model()


class UserRegisterAPIView(APIView):
    
    def post(self, request, **extra):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response = {
                "email": user.email, "user_id": user.user_id
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, user_id):
        user = User.objects.get(user_id=user_id)
        serializer = UserUpdateSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRetrieveAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = User.objects.get(user_id=user_id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
