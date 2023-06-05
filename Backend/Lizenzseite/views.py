from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Lizenz
from .serializers import LizenzSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication

class LizenzView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

    # GET-Methode für die API-Anfrage
    def get(self, request, *args, **kwargs):
        # Get role and firmcode from the authenticated user
        user_role = request.user.role
        user_firmcode = request.user.firm_code

         # Apply filters based on user's role and firmcode
        if user_role == 'Admin':
            # Admin can see all dongles
            result = Lizenz.objects.all()
        elif user_role == 'Verwalter':
            # Verwalter can see all dongles with the same firmcode
            result = Lizenz.objects.all()
        elif user_role == 'Kunde':
            # Kunde can see only their dongles with the same firmcode
            result = Lizenz.objects.filter(firmcode=user_firmcode, kunde=request.user.name)
        else:
            # Return an empty queryset if the role is not recognized
            result = Lizenz.objects.none()
       
        
        serializers = LizenzSerializer(result, many=True)
        
        # Rückgabe der serialisierten Daten als JSON-Antwort
        return Response({'status': 'success', "Lizenz": serializers.data}, status=200)