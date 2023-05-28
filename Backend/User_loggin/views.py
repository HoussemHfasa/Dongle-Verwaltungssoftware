# Nutzermodell importieren
from django.contrib.auth import get_user_model  

# Views importieren 
from django.shortcuts import render
from rest_framework import generics

# JWT Token Response importieren
from rest_framework_simplejwt.views import TokenObtainPairView  

# Eigene Serializers und Models importieren
from . import models
from . import serializers  

# Authentifizierung importieren
from django.contrib.auth import authenticate

# APIView, Response und Statuscodes importieren
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST  

# Nutzermodell definieren 
User = get_user_model()

# Login View
class UserLoginAPIView(TokenObtainPairView): 
    # Login Serializer verwenden 
    serializer_class = serializers.UserLoginSerializer

# Nutzerliste 
class UserListView(generics.ListCreateAPIView):
    # Alle Nutzer anzeigen
    queryset = User.objects.all()  
    # Nutzer Serializer verwenden 
    serializer_class = serializers.UserSerializer

# Detailansicht eines Nutzers 
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    # Alle Nutzer anzeigen
    queryset = User.objects.all()  
    # Nutzer Serializer verwenden
    serializer_class = serializers.UserSerializer  

# Administratorenliste  
class AdminListView(generics.ListCreateAPIView):
    # Nur Administratoren anzeigen
    queryset = User.objects.filter(role='Admin')  
    # Nutzer Serializer verwenden
    serializer_class = serializers.UserSerializer   

# Detailansicht eines Administrators
class AdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    # Nur Administratoren anzeigen 
    queryset = User.objects.filter(role='Admin')   
    # Nutzer Serializer verwenden  
    serializer_class = serializers.UserSerializer   

# Verwalterliste
class VerwalterListView(generics.ListCreateAPIView):
    # Nur Verwalter anzeigen
    queryset = User.objects.filter(role='Verwalter')  
    # Nutzer Serializer verwenden
    serializer_class = serializers.UserSerializer

# Detailansicht eines Verwalters
class VerwalterDetailView(generics.RetrieveUpdateDestroyAPIView):
    # Nur Verwalter anzeigen
    queryset = User.objects.filter(role='Verwalter')  
    # Nutzer Serializer verwenden
    serializer_class = serializers.UserSerializer

# Kundenliste 
class KundeListView(generics.ListCreateAPIView):
    # Nur Kunden anzeigen
    queryset = User.objects.filter(role='Kunde') 
    # Nutzer Serializer verwenden 
    serializer_class = serializers.UserSerializer

# Detailansicht eines Kunden
class KundeDetailView(generics.RetrieveUpdateDestroyAPIView):
    # Nur Kunden anzeigen
    queryset = User.objects.filter(role='Kunde')  
    # Nutzer Serializer verwenden
    serializer_class = serializers.UserSerializer