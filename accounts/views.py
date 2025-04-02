# views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegistrationSerializer, LoginSerializer


def registrationPage(request):
    User = get_user_model() 

    if request.user.is_authenticated:
        return render(request=request, template_name="/")

    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = User.objects.create_user(
            username = username,
            email = email,
            password = password)
        
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
        return redirect("/")
    
    return render(request=request, template_name="registration.html", context={})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return HttpResponse("fail")

    return render(request=request, template_name="login.html", context={})


# API Views for JWT Authentication
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh), 
                'access': str(refresh.access_token)},
                 status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
