from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate
from users.serializers import RegistrationSerializer
from django.contrib.auth.models import User



def registrationPage(request):
    return render(request, 'registration.html',{})
   

def loginPage(request):
    return render(request, 'login.html',{})


class UserRegistrationView(APIView):
   def post(self,request):
     serializer = RegistrationSerializer(data=request.data)
     
     if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=serializer.data['email'])
        user.set_password(serializer.data['password'])
        serializer.save()
        token = Token.objects.create(user=user)
        
        return Response({'token':token.key, "user":serializer.data},status=status.HTTP_201_CREATED)
     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
class UserLoginView(APIView):
   def post(self,request):
      pass
