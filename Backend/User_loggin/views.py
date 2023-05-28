from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from . import models
from . import serializers
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

User = get_user_model()

class UserLoginAPIView(TokenObtainPairView):
    serializer_class = serializers.UserLoginSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class AdminListView(generics.ListCreateAPIView):
    queryset = User.objects.filter(role='Admin')
    serializer_class = serializers.UserSerializer

class AdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(role='Admin')
    serializer_class = serializers.UserSerializer

class VerwalterListView(generics.ListCreateAPIView):
    queryset = User.objects.filter(role='Verwalter')
    serializer_class = serializers.UserSerializer

class VerwalterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(role='Verwalter')
    serializer_class = serializers.UserSerializer

class KundeListView(generics.ListCreateAPIView):
    queryset = User.objects.filter(role='Kunde')
    serializer_class = serializers.UserSerializer

class KundeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(role='Kunde')
    serializer_class = serializers.UserSerializer