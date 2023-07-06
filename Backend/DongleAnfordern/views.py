from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Max
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
#houssem
from datetime import date
from rest_framework import generics #yassin
    

class TicketCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TicketSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred while creating the license: {str(e)}"}, status=400)

        # Get the highest id_ticket value
        id_ticket = Ticket.objects.aggregate(Max('id_ticket'))['id_ticket__max']
        if id_ticket is None:
            id_ticket = 1
        else:
            id_ticket += 1

        # Retrieve the values from the React inputs
        
        schliessungsdatum = request.data.get('schliessungsdatum')
        erstellungsdatum = request.data.get('erstellungsdatum')
        beschreibung = request.data.get('beschreibung')
        titel = request.data.get('titel')
        dongle_seriennummer = request.data.get('dongle_seriennummer')

        try:
            ticket_data = {
                'id_ticket': id_ticket,
                'titel': titel,
                'lizenzname': "",
                'erstellungsdatum': erstellungsdatum,
                'schliessungsdatum': schliessungsdatum,
                'beschreibung': beschreibung,
                'status': 'offen',
                'admin_verwalter_id': 5,
                'dongle_seriennummer': dongle_seriennummer,
                'grund_der_ablehnung': "",
            }
            new_ticket = Ticket(**ticket_data)
            new_ticket.save()

            return JsonResponse({"success": "Die Lizenz wurde erfolgreich erstellt."}, status=201)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred while creating the license: {str(e)}"}, status=400)

