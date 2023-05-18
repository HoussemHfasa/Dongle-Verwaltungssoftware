from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CustomTokenObtainPairSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def login(request):
    serializer = CustomTokenObtainPairSerializer(data=request.data)
    if serializer.is_valid():
        role = serializer.validated_data['role']
        if role == 'Admin':
            return Response({'message': 'Willkommen Admin'})
        elif role == 'Verwalter':
            return Response({'message': 'Willkommen Verwalter'})
        else:
            return Response({'message': 'Willkommen Kunde'})
    else:
        return Response(serializer.errors, status=400)
    
from django.contrib.auth.backends import BaseBackend
from .models import admin_verwalter, kunde


class CustomAuthenticationBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = admin_verwalter.objects.get(email=email)
        except admin_verwalter.DoesNotExist:
            try:
                user = kunde.objects.get(email=email)
            except kunde.DoesNotExist:
                return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return admin_verwalter.objects.get(pk=user_id)
        except admin_verwalter.DoesNotExist:
            try:
                return kunde.objects.get(pk=user_id)
            except kunde.DoesNotExist:
                return None