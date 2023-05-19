from multiprocessing import AuthenticationError
from django.contrib.auth.backends import BaseBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import AdminVerwalter, Kunde
from .serializers import CustomTokenObtainPairSerializer
from django.contrib.auth import authenticate

@api_view(['POST'])
def user_role(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = AuthenticationError(request, email=email, password=password)

    if user:
        if isinstance(user, AdminVerwalter):
            role = 'Admin' if user.is_admin else 'Verwalter'
        elif isinstance(user, Kunde):
            role = 'Kunde'
        else:
            role = 'Unknown'

        return Response({'email': email, 'role': role}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'User not found or password incorrect.'}, status=status.HTTP_404_NOT_FOUND)

class CustomAuthenticationBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = AdminVerwalter.objects.get(email=email)
        except AdminVerwalter.DoesNotExist:
            try:
                user = Kunde.objects.get(email=email)
            except Kunde.DoesNotExist:
                return None

        if user.check_password(password):
            return user

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer