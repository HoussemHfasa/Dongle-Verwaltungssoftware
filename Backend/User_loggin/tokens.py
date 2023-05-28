# AccessToken importieren
from rest_framework_simplejwt.tokens import AccessToken  

# Eigene AccessToken-Klasse 
class CustomAccessToken(AccessToken):

    # Payload mit zusätzlichen Nutzerdaten füllen 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.payload['email'] = self.user.email
        self.payload['name'] = self.user.name
        self.payload['role'] = self.user.role