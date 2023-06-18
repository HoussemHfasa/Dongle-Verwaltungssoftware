# User_loggin/tokens.py

# AccessToken importieren
from rest_framework_simplejwt.tokens import AccessToken

# Eigene AccessToken-Klasse erstellen
class CustomAccessToken(AccessToken):

    # Payload mit zusätzlichen Nutzerdaten füllen
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # E-Mail-Adresse des Benutzers hinzufügen
        self.payload["email"] = self.user.email
        # Name des Benutzers hinzufügen
        self.payload["name"] = self.user.name
        # Rolle des Benutzers hinzufügen
        self.payload["role"] = self.user.role
        # Firmencode des Benutzers hinzufügen
        self.payload["Firmcode"] = self.user.firm_code