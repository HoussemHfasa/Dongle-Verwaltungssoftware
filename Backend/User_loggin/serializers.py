from django.contrib.auth.models import User  
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import AdminVerwalter, Kunde

User = get_user_model()
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # ...

    def validate(self, attrs):
        user = AdminVerwalter.objects.filter(email=attrs['email']).first()
        if not user:
            user = Kunde.objects.filter(email=attrs['email']).first()
            if not user:
                raise serializers.ValidationError("User not found")

        self.user = user
        role = None

        # Check if the user is an admin, verwalter, or kunde
        if isinstance(user, AdminVerwalter):  
            if hasattr(user, 'is_admin'):
                role = 'Admin' if user.is_admin else 'Verwalter' 
            else:
                role = 'Verwalter'     
        elif isinstance(user, Kunde):
            role = 'Kunde'  
        data = super().validate(attrs)
        data['role'] = role
        return data