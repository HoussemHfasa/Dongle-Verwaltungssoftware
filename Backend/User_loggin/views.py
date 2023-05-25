from multiprocessing import AuthenticationError
from django.contrib.auth.backends import BaseBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import AdminVerwalter, Kunde
from .serializers import CustomTokenObtainPairSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password


@api_view(['POST'])
def user_role(request):
    email = request.data.get('email')
    password = request.data.get('password')

    # Use the custom authentication backend
    backend = CustomAuthenticationBackend()
    user = backend.authenticate(request, email=email, password=password)

    if user:
        if isinstance(user, AdminVerwalter):
            role = user.role
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

        if check_password(password, user.password):
            return user

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer