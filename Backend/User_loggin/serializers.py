# Serializers importieren 
from rest_framework import serializers

# Nutzermodell importieren
from django.contrib.auth import get_user_model

# JWT Token importieren 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 

# Model importieren 
from .models import CustomUser

# Nutzermodell definieren
User = get_user_model()

# Eigene Token Serializer-Klasse 
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Token generieren und Nutzerrolle hinzufügen
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        return token

# Login Serializer 
class UserLoginSerializer(CustomTokenObtainPairSerializer):
    # Beim Validation auch Refresh-Token  und Access Token hinzufügen 
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Zusätzliche Nutzerdaten hinzufügen 
        data['role'] = self.user.role
        return data

# Nutzer Serializer
class UserSerializer(serializers.ModelSerializer):
    # Token Serializer Methode hinzufügen  
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        # Tokenfeld hinzufügen
        fields = ('id', 'email', 'name', 'role', 'password', 'firm_code', 'token')  
        extra_kwargs = {'password': {'write_only': True}}

    # Nutzer erstellen 
    def create(self, validated_data):
        ...

    # Token generieren 
    def get_token(self, obj):
        token = CustomTokenObtainPairSerializer.get_token(obj)
        return str(token.access_token)