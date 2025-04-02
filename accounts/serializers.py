from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # Hash password
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    #When working with passwords, it is better to use write_only=True so that it
    #is not displayed in the data returned by the serializer.
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return user