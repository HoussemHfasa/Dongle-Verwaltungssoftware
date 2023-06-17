#api.py
# Nutzermodell importieren  
from django.contrib.auth import get_user_model   

# Filter und Viewsets importieren
from rest_framework import filters
from rest_framework import viewsets   

# Models, Serialisizers und Permissions importieren 
from . import serializers   
from . import permissions  


# APIView, Response und Status codes importieren
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST   
from rest_framework.permissions import AllowAny

# Authentifizierung importieren
from django.contrib.auth import authenticate


import logging

logger = logging.getLogger(__name__)

# Nutzermodel definieren
User = get_user_model()   

# Login View
class UserLoginAPIView(APIView):   
    permission_classes = [AllowAny]   

    def post(self, request, *args, **kwargs):
        data = request.data   
        email = data.get('email', None)
        password = data.get('password', None)


        user = authenticate(request, email=email, password=password)   

        if user is not None:    
            serializer = serializers.UserSerializer(user)
            response = super().post(request, *args, **kwargs)
            logger.info(f'Firmcode: {response.data["Firmcode"]}')
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
            
