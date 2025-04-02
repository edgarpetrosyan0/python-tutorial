from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', "username", "password"]

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    #When working with passwords, it is better to use write_only=True so that it
    #is not displayed in the data returned by the serializer.
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
       #Check that the user is logged in.
        user = authenticate(email=data.get('email'), password=data.get('password'))
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return user


