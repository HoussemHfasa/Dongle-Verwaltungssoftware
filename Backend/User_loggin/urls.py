# User_loggin/urls.py
# URLs importieren 
from django.urls import path
from django.urls import reverse

# Eigene Views importieren 
from .views import (UserLoginAPIView, ObtainAdminAccessToken,CreateUserView,Passwordchangeview,ObtainAccessToken,GetUserPasswordView)

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='user-login'),  
    path('admin-access-token/', ObtainAdminAccessToken.as_view(), name='admin-access-token'),
    path('user-access-token/', ObtainAccessToken.as_view(), name='user-access-token'),
    path('users/', CreateUserView.as_view(), name='create-user'),
    path('passwortverwalten/', Passwordchangeview.as_view(), name='passwort-verwalten'),
    path('Passwortzuruecksetzung/', GetUserPasswordView.as_view(), name='Passwortzurücksetzung'),
    
    
]