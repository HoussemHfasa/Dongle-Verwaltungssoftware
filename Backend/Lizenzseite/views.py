from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Lizenz
from .serializers import LizenzSerializer

class LizenzView(APIView):

    # GET-Methode für die API-Anfrage
    def get(self, request, *args, **kwargs):
        # Abfrage aller Lizenz-Objekte aus der Datenbank
        result = Lizenz.objects.all()
        
        serializers = LizenzSerializer(result, many=True)
        
        # Rückgabe der serialisierten Daten als JSON-Antwort
        return Response({'status': 'success', "Lizenz": serializers.data}, status=200)