from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["email", "password"]

    def validate_password(self, password):
        password_validation.validate_password(password)
        return password

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["full_name", "bio", "age", "avatar"]

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.bio = validated_data.get("bio", instance.bio)
        instance.age = validated_data.get("age", instance.age)
        instance.avatar = validated_data.get("avatar", instance.avatar)
        instance.save()
        return instance
 

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["email", "full_name", "bio", "age", "avatar"]