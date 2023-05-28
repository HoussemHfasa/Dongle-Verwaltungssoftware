from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dongle
from .serializers import DongleSerializer


class DongleView(APIView):

    # GET-Methode für die API-Anfrage
    def get(self, request, *args, **kwargs):
        # Abfrage aller Dongle-Objekte aus der Datenbank
        result = Dongle.objects.all()
        
        serializers = DongleSerializer(result, many=True)
        
        # Rückgabe der serialisierten Daten als JSON-Antwort
        return Response({'status': 'success', "Dongle": serializers.data}, status=200)