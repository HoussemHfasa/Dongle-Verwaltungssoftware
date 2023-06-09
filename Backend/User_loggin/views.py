# User_loggin/views.py
# Nutzermodell importieren
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
# Views importieren
from rest_framework import generics
from rest_framework import status
# testcreateuser
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# APIView, Response und Statuscodes importieren
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
# JWT Token Response importieren
from rest_framework_simplejwt.views import TokenObtainPairView

# Eigene Serializers und Models importieren
from . import serializers
from .permissions import IsAdminOrReadOnly
# testcreat account
from .serializers import CustomTokenObtainPairSerializer

# Authentifizierung importieren


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

#in frontend benutzt
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
        firm_code = request.data.get("firm_code")

        if not email or not name or not role or not password:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(is_superuser=False, email=email, name=name, role=role, password=password,
                                            firm_code=firm_code)
            # Serialize the created user object, if needed
            # user_data = UserSerializer(user).data
            # Senden Sie eine E-Mail an den neu erstellten Benutzer
            subject = 'Willkommen bei GFal!'
            body = f"Lieber {name},\n\nIhnen wurde von einem Administrator ein Konto in unserer App erstellt! Hier sind Ihre Anmeldeinformationen:\n\nE-Mail: {email}\nPasswort: {password}\n\nBitte bewahren Sie Ihre Anmeldeinformationen sicher auf.\n\nMit freundlichen Grüßen,\nDas Our GFal-Team"
            email = EmailMessage(subject, body, to=[email])
            email.send()
            return Response({"success": "User created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)




class Passwordchangeview(APIView):

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        old_password = request.data.get("oldPassword")
        new_password = request.data.get("newPassword") 

        if not email or not old_password or not new_password:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)

            # Check if the old password is correct
            if not user.check_password(old_password):
                return Response({"error": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)

            # Set the new password
            user.set_password(new_password)
            user.save()

            return Response({"success": "Password changed successfully"}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class ObtainAccessToken(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            token = str(CustomTokenObtainPairSerializer.get_token(user).access_token)
            return Response({"access_token": token})
        else:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

