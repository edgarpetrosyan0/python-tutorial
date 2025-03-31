from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,get_user


def registrationPage(request):
    return render(request, 'registration.html',{})

   

def loginPage(request):
    return render(request, 'login.html',{})
