from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.api.serializers import UserRegisterSerializer


class UserRegisterAPIView(APIView):
    
    def post(self, request, **extra):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"email": user.email}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)