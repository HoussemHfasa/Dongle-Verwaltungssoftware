# User_loggin/views.py
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
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST  


#testcreateuser
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly


#testcreat account
from .serializers import CustomTokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model



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


    
class AdminAccessTokenView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.role != 'Admin':
            return Response({'error': 'Only admin users can obtain admin access token'}, status=HTTP_400_BAD_REQUEST)

        token = str(CustomTokenObtainPairSerializer.get_token(request.user).access_token)
        return Response({'access_token': token})
    
class ObtainAdminAccessToken(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            if user.role == "Admin":
                token = str(CustomTokenObtainPairSerializer.get_token(user).access_token)
                return Response({"access_token": token})
            else:
                return Response({"error": "User is not an admin"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
        

class CreateUserView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        name = request.data.get("name")
        role = request.data.get("role")
        password = request.data.get("password")
        firm_code=request.data.get("firm_code")

        if not email or not name or not role or not password:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(is_superuser=False ,email=email, name=name, role=role, password=password,firm_code=firm_code)
            # Serialize the created user object, if needed
            # user_data = UserSerializer(user).data
            return Response({"success": "User created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        


