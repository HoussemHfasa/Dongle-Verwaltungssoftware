# User_loggin/urls.py
# URLs importieren 
from django.urls import path

# Eigene Views importieren 
from .views import (UserLoginAPIView, ObtainAdminAccessToken,CreateUserView,Passwordchangeview,ObtainAccessToken,GetUserPasswordView)

urlpatterns = [
    # Login URL hinzufügen
    path('login/', UserLoginAPIView.as_view(), name='user-login'),  
    #path('users/', UserListView.as_view(), name='user-list'),
    #path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    #path('admin/', AdminListView.as_view(), name='admin-list'),
    #path('verwalter/', VerwalterListView.as_view(), name='verwalter-list'),
    #path('kunde/', KundeListView.as_view(), name='kunde-list'),
    #path('admin-access-token/', AdminAccessTokenView.as_view(), name='admin-access-token'),
    path('admin-access-token/', ObtainAdminAccessToken.as_view(), name='admin-access-token'),
    path('user-access-token/', ObtainAccessToken.as_view(), name='user-access-token'),
    path('users/', CreateUserView.as_view(), name='create-user'),
    path('passwortverwalten/', Passwordchangeview.as_view(), name='passwort-verwalten'),
    path('Passwortzuruecksetzung/', GetUserPasswordView.as_view(), name='Passwortzurücksetzung'),
    
    
]