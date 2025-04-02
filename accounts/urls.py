from django.urls import path
from accounts.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    #For HTML page
    path('login/', loginPage, name='login'), 
    path('registration/', registrationPage, name='registration'),

    # # Registration and Login API, exclude_from_schema=True will not be visible in Swagger
    # path('api/register/', UserRegistrationView.as_view(), name='register', exclude_from_schema=True),
    # path('api/login/', UserLoginView.as_view(), name='login_api', exclude_from_schema=True),

    # Getting and refreshing a JWT token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 ]

