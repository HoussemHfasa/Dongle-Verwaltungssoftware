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
import datetime
from datetime import date
from rest_framework import generics #yassin
from User_loggin.models import CustomUser
from Dongle_hinzufügen.models import Dongle
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
import random
import string
from datetime import datetime, timedelta

# Klasse für das Erstellen eines D-Tickets (Dongle)
class TicketCreateViewD(APIView):
        # Authentifizierung und Berechtigungen
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = TicketSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred while creating the license: {str(e)}"}, status=401)

        id_ticket = Ticket.objects.aggregate(Max('id_ticket'))['id_ticket__max']
        if id_ticket is None:
            id_ticket = 1
        else:
            id_ticket += 1

        gueltig_von = request.data.get('gueltig_von')
        gueltig_bis = request.data.get('gueltig_bis')
        projekt = request.data.get('projekt')
        standort = request.data.get('standort')
        haendler = request.data.get('haendler')
        firmcode = request.data.get('firmcode')
        customer = CustomUser.objects.filter(firm_code=firmcode).first()
        if customer:
            kunde = customer.name
            kunde_email = customer.email
        else:
            kunde = ""
            kunde_email = ""
        schliessungsdatum = request.data.get('schliessungsdatum')
        erstellungsdatum = request.data.get('erstellungsdatum')
        beschreibung = request.data.get('beschreibung')
        titel = request.data.get('titel')
        dongle_seriennummer = request.data.get('dongle_seriennummer')
        dongle_name = request.data.get('dongle_name')
        

        try:
            ticket_data = {
                'id_ticket': id_ticket,
                'titel': titel,
                'beschreibung': beschreibung,
                'status': 'offen',
                'erstellungsdatum': erstellungsdatum,
                'schliessungsdatum': schliessungsdatum,
                'dongle_lizenz': 0,
                'dongle_name': dongle_name,
                'dongle_seriennummer': dongle_seriennummer,
                'lizenzname': "",
                'firmcode': firmcode,
                'gueltig_von': gueltig_von,
                'gueltig_bis': gueltig_bis,
                'einheiten' :None,
                'projekt': projekt,
                'grund_der_ablehnung': "",
                'admin_verwalter_email':"",
                'haendler': haendler,
                'standort': standort,
                'productcode' :None,
                'lizenzanzahl':None,
            }
            new_ticket = Ticket(**ticket_data)
            new_ticket.save()
          
            return JsonResponse({"success": "Die Lizenz wurde erfolgreich erstellt."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred while creating the license: {str(e)}"}, status=400)

def random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Klasse für das Erstellen eines L-Tickets (Lizenz)
class TicketCreateViewL(APIView):
    # Authentifizierung und Berechtigungen
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = TicketSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred while creating the license: {str(e)}"}, status=401)

        # Get the highest id_ticket value
        id_ticket = Ticket.objects.aggregate(Max('id_ticket'))['id_ticket__max']
        if id_ticket is None:
            id_ticket = 1
        else:
            id_ticket += 1

        # Retrieve the values from the React inputs
        gueltig_von = request.data.get('gueltig_von')
        gueltig_bis = request.data.get('gueltig_bis')
        einheiten = request.data.get('einheiten')
        projekt = request.data.get('projekt')
        productcode = request.data.get('productcode')
        firmcode = request.data.get('firmcode')
        schliessungsdatum = request.data.get('schliessungsdatum')
        erstellungsdatum = request.data.get('erstellungsdatum')
        beschreibung = request.data.get('beschreibung')
        titel = request.data.get('titel')
        dongle_seriennummer = request.data.get('dongle_seriennummer')
        lizenzname = request.data.get('lizenzname')
        lizenzanzahl= request.data.get('lizenzanzahl')

        Dongle_=Dongle.objects.filter(serien_nr=dongle_seriennummer).first()
        if not Dongle_:
            return JsonResponse({"error": "Dongle Seriennummer nicht gefunden"}, status=404)

        try:
            ticket_data = {
                'id_ticket': id_ticket,
                'titel': titel,
                'beschreibung': beschreibung,
                'status': 'offen',
                'erstellungsdatum': erstellungsdatum,
                'schliessungsdatum': schliessungsdatum,
                'dongle_lizenz': 1,
                'dongle_name': "",
                'dongle_seriennummer': dongle_seriennummer,
                'lizenzname': lizenzname,
                'firmcode': firmcode,
                'gueltig_von': gueltig_von,
                'gueltig_bis': gueltig_bis,
                'einheiten' :einheiten,
                'projekt': projekt,
                'grund_der_ablehnung': "",
                'admin_verwalter_email':"",
                'haendler': "",
                'standort': "",
                'productcode' :productcode,
                'lizenzanzahl':lizenzanzahl,
            }
            new_ticket = Ticket(**ticket_data)
            new_ticket.save()

            return JsonResponse({"success": "Die Lizenz wurde erfolgreich erstellt."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred while creating the license: {str(e)}"}, status=400)


