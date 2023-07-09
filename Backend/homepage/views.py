from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dongle
from .serializers import DongleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication


class DongleView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # GET-Methode für die API-Anfrage
    def get(self, request, *args, **kwargs):
        # Get role and firmcode from the authenticated user
        user_role = request.user.role
        user_firmcode = request.user.firm_code
        
        # Anwenden von Filtern basierend auf der Rolle und dem Firmencode des Benutzers
        if user_role == 'Admin':
            # Admin kann alle Dongles sehen
            result = Dongle.objects.all()
        elif user_role == 'Verwalter':
            # Verwalter kann alle Dongles mit demselben Firmencode sehen
            result = Dongle.objects.all()
        elif user_role == 'Kunde':
            # Kunde kann nur ihre eigenen Dongles mit demselben Firmencode sehen
            result = Dongle.objects.filter(firmcode=user_firmcode, kunde=request.user.name)
        else:
            # Rückgabe einer leeren Abfrage, wenn die Rolle nicht erkannt wird
            result = Dongle.objects.none()

        
        serializers = DongleSerializer(result, many=True)
        # Rückgabe der serialisierten Daten als JSON-Antwort
        return Response({'status': 'success', "Dongle": serializers.data}, status=200)