from rest_framework import serializers
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validators
from django.core import exceptions

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["email", "password"]

    def validate(self, data):
        user = User(**data)
        password = data["password"]
        
        errors = dict() 
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=user)

         # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
             errors['password'] = list(e.messages)

        if errors:
             raise serializers.ValidationError(errors)

        return super(UserRegisterSerializer, self).validate(data)

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