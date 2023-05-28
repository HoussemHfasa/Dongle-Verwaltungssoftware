from rest_framework_simplejwt.tokens import AccessToken

class CustomAccessToken(AccessToken):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.payload['email'] = self.user.email
        self.payload['name'] = self.user.name
        self.payload['role'] = self.user.role