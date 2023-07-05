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
        lizenzname = request.data.get('lizenzname')
        schliessungsdatum = request.data.get('schliessungsdatum')
        erstellungsdatum = request.data.get('erstellungsdatum')
        beschreibung = request.data.get('beschreibung')
        titel = request.data.get('titel')
        dongle_seriennummer = request.data.get('dongle_seriennummer')

        try:
            ticket_data = {
                'id_ticket': id_ticket,
                'titel': titel,
                'lizenzname': lizenzname,
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


#houssem
from .models import Ticket, Lizenz  # Import the Lizenz model

# ... other imports

class TicketAnnehmenView(APIView):
    def post(self, request, *args, **kwargs):
        ticket_id = request.data.get("id_ticket")
        ticket = Ticket.objects.get(id_ticket=ticket_id)

        # Create a new Lizenz
        #new_lizenz = Lizenz(...)
        #new_lizenz.save()

        # Update the ticket status to beendet
        ticket.status = "beendet"
        ticket.save()

        return JsonResponse({"success": "Die Lizenz wurde angenommen und erstellt."}, status=200)

class TicketAblehnenView(APIView):
    def post(self, request, *args, **kwargs):
        ticket_id = request.data.get("id_ticket")
        grund_der_ablehnung = request.data.get("grund_der_ablehnung")
        ticket = Ticket.objects.get(id_ticket=ticket_id)

        # Update the ticket status and store the reason for rejection
        ticket.status = "beendet"
        ticket.grund_der_ablehnung = grund_der_ablehnung
        ticket.save()

        return JsonResponse({"success": "Die Lizenz wurde abgelehnt."}, status=200)


#yassin

class TicketDetailsView(generics.RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get(self, request, *args, **kwargs):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        ticket_id = request.data.get("id_ticket")
        try:
            ticket = Ticket.objects.get(id_ticket=ticket_id)
            serializer = TicketSerializer(ticket, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return JsonResponse({"success": "Ticket updated successfully."}, status=200)
            else:
                return JsonResponse({"error": "Invalid data."}, status=400)
        except Ticket.DoesNotExist:
            return JsonResponse({"error": "Ticket not found."}, status=404)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=400)

    def patch(self, request, *args, **kwargs):
        ticket = self.get_object()
        serializer = self.get_serializer(ticket, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
