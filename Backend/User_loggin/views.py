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
from django.utils import timezone


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

# Klasse zum Abrufen des Zugriffstokens
class ObtainAccessToken(APIView):
    # POST-Methode zum Abrufen des Zugriffstokens
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, username=email, password=password)

        # Wenn der Benutzer authentifiziert ist, gib das Token zurück
        if user is not None:
            token = str(CustomTokenObtainPairSerializer.get_token(user).access_token)
            return Response({"access_token": token},status=status.HTTP_200_OK)
        else:
            return Response({"error": "Ungültige E-Mail oder Passwort"}, status=status.HTTP_401_UNAUTHORIZED)

# Login View
class UserLoginAPIView(TokenObtainPairView):
    # Login Serializer verwenden
    serializer_class = serializers.UserLoginSerializer
    http_method_names = ['post']


# Klasse zum Abrufen des Admin-Zugriffstokens
class AdminAccessTokenView(GenericAPIView):
    # Nur authentifizierte Benutzer können auf diese Ansicht zugreifen
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    # GET-Methode zum Abrufen des Admin-Zugriffstokens
    def get(self, request, *args, **kwargs):
        # Wenn der Benutzer keine Admin-Rolle hat, gib einen Fehler zurück
        if request.user.role != 'Admin':
            return Response({'error': 'Only admin users can obtain admin access token'}, status=HTTP_400_BAD_REQUEST)

        # Wenn der Benutzer ein Admin ist, gib das Token zurück
        token = str(CustomTokenObtainPairSerializer.get_token(request.user).access_token)
        return Response({'access_token': token})

# Klasse zum Abrufen des Admin-Zugriffstokens mit der POST-Methode
class ObtainAdminAccessToken(APIView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, username=email, password=password)

        # Wenn der Benutzer authentifiziert ist und Admin-Rolle hat, gib das Token zurück
        if user is not None:
            if user.role == "Admin":
                token = str(CustomTokenObtainPairSerializer.get_token(user).access_token)
                return Response({"access_token": token},status=status.HTTP_200_OK)
            else:
                return Response({"error": "User is not an admin"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

# Klasse zum Erstellen eines neuen Benutzers
class CreateUserView(APIView):
    # Nur Admins können neue Benutzer erstellen, andere Benutzer haben schreibgeschützten Zugriff
    permission_classes = [IsAdminOrReadOnly]

    # Funktion zum Generieren eines sicheren Passworts
    def generate_strong_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(characters) for _ in range(length))

    # POST-Methode zum Erstellen eines neuen Benutzers
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        name = request.data.get("name")
        password_length = secrets.randbelow(4) + 12
        password = self.generate_strong_password(password_length)
        role = request.data.get("role")
        firm_code = request.data.get("firm_code")

        # Überprüfe, ob alle erforderlichen Felder ausgefüllt sind
        if not email or not name or not role:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Erstelle einen neuen Benutzer und sende eine Willkommens-E-Mail
        try:
            user = User.objects.create_user(is_superuser=False, email=email, name=name, role=role, password=password,
                                            firm_code=firm_code)
            subject ='Willkommen bei GFal!'
            body = f"Lieber {name},\n\nIhnen wurde von einem Administrator ein Konto in unserer App erstellt! Hier sind Ihre Anmeldeinformationen:\n\nE-Mail: {email}\nPasswort: {password}\n\nBitte bewahren Sie Ihre Anmeldeinformationen sicher auf.\n\nMit freundlichen Grüßen,\nDas Our GFal-Team"
            email = EmailMessage(subject, body, to=[email])
            email.send()
            return Response({"success": "User created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Klasse zum Ändern des Passworts
class Passwordchangeview(APIView):
    # POST-Methode zum Ändern des Passworts
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        old_password = request.data.get("oldPassword")
        new_password = request.data.get("newPassword")

        # Überprüfe, ob alle erforderlichen Felder ausgefüllt sind
        if not email or not old_password or not new_password:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Ändere das Passwort, wenn der Benutzer gefunden wird und das alte Passwort korrekt ist
        try:
            user = User.objects.get(email=email)

            # Überprüfen, ob das alte Passwort korrekt ist
            if not user.check_password(old_password):
                return Response({"error": "Altes Passwort ist nicht korrekt"}, status=status.HTTP_400_BAD_REQUEST)

            # Neues Passwort setzen
            user.set_password(new_password)
            # Update the user's password and last_login
            user.last_login = timezone.now()
            user.save()
            subject = 'Passwort erfolgreich geändert für Ihr GFal-Konto'

            body = f"""Lieber {user.name},

            Ihr Passwort wurde erfolgreich geändert. Wenn Sie Ihr Passwort nicht geändert haben, können Sie den Zugang über die Funktion "Passwort vergessen" auf der Anmeldeseite wiederherstellen oder unser Team kontaktieren.

            Mit freundlichen Grüßen,
            Das GFal-Team

            ---

            Dear {user.name},

            Your password has been successfully changed. If you did not change your password, you can regain access by using the "Forgot Password" feature on the login page or by contacting our team.

            Best regards,
            The GFal Team
            """
           
            email = EmailMessage(subject, body, to=[email])
            email.send()
            return Response({"success": "Passwort erfolgreich geändert"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error": "Benutzer nicht gefunden"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
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
    
    
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        # ... (authenticate the user)
        user = User.objects.get(email=email)

        # Check if this is the user's first login (last_login is None)
        if user.last_login is None:
            # Return a response indicating that the user needs to change their password
            return Response({"message": "Please change your password on first login"},
                            status=status.HTTP_403_FORBIDDEN)

        # ... (proceed with the login)