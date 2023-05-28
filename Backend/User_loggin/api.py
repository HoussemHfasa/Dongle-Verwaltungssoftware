from django.contrib.auth import get_user_model
from rest_framework import filters
from rest_framework import viewsets
from . import models
from . import serializers
from . import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth import authenticate
from .models import CustomUser as User

User = get_user_model()
class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(request, email=email, password=password)

        if user is not None:
            # You can return the user data or a token if you are using token-based authentication
            serializer = serializers.UserSerializer(user)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response({"detail": "Invalid email or password"}, status=HTTP_400_BAD_REQUEST)
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'name']

    def get_queryset(self):
        if self.request.user.role == 'Admin':
            return User.objects.all()
        elif self.request.user.role == 'Verwalter':
            return User.objects.filter(role='Kunde')
        else:
            return User.objects.none()

class AdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]

class VerwalterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]

class KundeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]