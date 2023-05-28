# Standard Backend importieren 
from django.contrib.auth.backends import BaseBackend

# Nutzermodell importieren 
from django.contrib.auth import get_user_model   

# Nutzermodel definieren
User = get_user_model()  

# Eigene Backend-Klasse 
class CustomUserModelAuthBackend(BaseBackend):
    # Nutzer authentifizieren
    def authenticate(self, request, email=None, password=None, **kwargs): 
        try:
            # Nutzer mit Email abrufen
            user = User.objects.get(email=email)  
            # Prüfen, ob Passwort korrekt ist
            if user.check_password(password):  
                return user
        except User.DoesNotExist:  
            # Keinen Nutzer gefunden, None zurückgeben 
            return None

    # Nutzer mit Nutzer-ID abrufen
    def get_user(self, user_id):  
        try:
            return User.objects.get(pk=user_id) 
        except User.DoesNotExist:  
            return None