from django.contrib.auth.models import User
from rest_framework import serializers
from users.models import admin_verwalter,kunde

#class UserSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = User
   #     fields = ('id', 'username', 'email', 'first_name', 'last_name')

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
   
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = get_user_model().EMAIL_FIELD

    def validate(self, attrs):
        user = admin_verwalter.objects.filter(email=attrs['email']).first()
        if not user:
            user = kunde.objects.filter(email=attrs['email']).first()
            if not user:
                raise serializers.ValidationError("User not found")
        
        if not user.check_password(attrs['password']):
            raise serializers.ValidationError("Incorrect password")

        self.user = user
        role = None

        if hasattr(user, 'role'):
            role = user.role
        else:
            role = 'Kunde'

        data = super().validate(attrs)
        data['role'] = role
        return data