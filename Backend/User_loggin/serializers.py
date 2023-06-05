#serializers.py
# Serializers importieren 
from rest_framework import serializers

# Nutzermodell importieren
from django.contrib.auth import get_user_model

# JWT Token importieren 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 



# Nutzermodell definieren
User = get_user_model()

# Eigene Token Serializer-Klasse 
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Token generieren und Nutzerrolle hinzufügen
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        token['firm_code'] = user.firm_code  # Add firm_code here
        return token

# Login Serializer 
class UserLoginSerializer(CustomTokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        data['role'] = self.user.role
        data['firm_code'] = self.user.firm_code  # Add firm_code here
        return data

# Nutzer Serializer
class UserSerializer(serializers.ModelSerializer):
    # Token Serializer Methode hinzufügen  
    token = serializers.SerializerMethodField()
    firm_code = serializers.CharField(max_length=45, required=False)

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