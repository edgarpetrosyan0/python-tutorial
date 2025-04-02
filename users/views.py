from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate
from users.serializers import RegistrationSerializer


def registrationPage(request):
    return render(request, 'registration.html',{})
   

def loginPage(request):
    return render(request, 'login.html',{})

class UserRegistrationView(APIView):
   def post(self,request):
     print(request.data)
     serializer = RegistrationSerializer(data=request.data)
     
     if serializer.is_valid():
       # Creating the user model
        user = serializer.save()

        user.set_password(serializer.validated_data['password'])
        user.save()

        refreshToken = RefreshToken.for_user(user)  # Creating a JWT Token
        print(serializer.data)

        return Response({
                'refresh': str(refreshToken),
                'access': str(refreshToken.access_token),
                'user': serializer.data,
                'redirect_url': '/login/'
            }, status=status.HTTP_201_CREATED)
     
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            refreshToken = RefreshToken.for_user(user)  #Creating a JWT Token

            return Response({
                'refresh': str(refreshToken),
                'access': str(refreshToken.access_token),
                'redirect_url': '/' 
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

