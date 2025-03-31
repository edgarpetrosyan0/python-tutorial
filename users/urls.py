from django.shortcuts import render
from django.urls import path
from users.views import (
    registrationPage,
    loginPage
)

urlpatterns = [
    path('login/', loginPage, name='login'), 
    path('registration/', registrationPage, name='registration'),
 ]

