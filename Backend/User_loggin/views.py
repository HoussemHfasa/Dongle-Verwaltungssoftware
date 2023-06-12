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

# Passwort generieren
import string
import secrets
#Passwortzurücksetzung
from django.core.exceptions import ObjectDoesNotExist


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

    def generate_strong_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(characters) for _ in range(length))

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        name = request.data.get("name")
        password_length = secrets.randbelow(4) + 12
        password = self.generate_strong_password(password_length)
        role = request.data.get("role")
        firm_code = request.data.get("firm_code")

        if not email or not name or not role:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        

        try:
            user = User.objects.create_user(is_superuser=False, email=email, name=name, role=role, password=password,
                                            firm_code=firm_code)
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
             # Senden Sie eine E-Mail an den neu erstellten Benutzer
            user = User.objects.get(email=email)
            subject = 'Passwort erfolgreich geändert!'
            body = f"Lieber {user.name},\n\nIhr Passwort wurde erfolgreich geändert. Wenn Sie diese Änderung nicht veranlasst haben, versuchen Sie, Ihr Passwort auf der Anmeldeseite über die Option 'Passwort vergessen' zurückzusetzen. Andernfalls setzen Sie sich bitte umgehend mit unserem Support in Verbindung.\n\nMit freundlichen Grüßen,\nDas Our GFal-Team"
            email = EmailMessage(subject, body, to=[email])
            email.send()

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



#Passwortzurücksetzung

class GetUserPasswordView(APIView):
    def generate_strong_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(characters) for _ in range(length))

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")

        if not email:
            return Response({"error": "Email field is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            password_length = secrets.randbelow(4) + 12
            password = self.generate_strong_password(password_length)
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()
            subject = 'Passwortzurücksetzung für Ihr GFal-Konto'
            body = f"Lieber {user.name},\n\nSie haben Ihr Passwort vergessen und eine Passwortzurücksetzung angefordert. Hier sind Ihre aktualisierten Anmeldeinformationen:\n\nE-Mail: {email}\nNeues Passwort: {password}\n\nBitte bewahren Sie Ihre Anmeldeinformationen sicher auf und ändern Sie Ihr Passwort, sobald Sie sich das nächste Mal anmelden.\n\nMit freundlichen Grüßen,\nDas Our GFal-Team"
            email = EmailMessage(subject, body, to=[email])
            email.send()

            return Response({"password": password}, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)