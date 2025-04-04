# views.py
from django.http import HttpRequest
from django.shortcuts import render

def home(request: HttpRequest):
    print(request.user.username)
    return render(request, 'main/index.html',{'username': request.user.username})
