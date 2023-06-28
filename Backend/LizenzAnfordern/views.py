from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Max
from .models import Ticket
from .models import Dongle
from .serializers import TicketSerializer
from .models import UserLogginCustomuser
from rest_framework.permissions import IsAuthenticated, BasePermission
#houssem
from datetime import date
    

class TicketCreateView(APIView):

    def post(self, request, *args, **kwargs):
        print("Request data:", request.data)  # Debugging print statement

        serializer = TicketSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print("Serializer error:", str(e))  # Debugging print statement
            return JsonResponse({"error": f"An error occurred while creating the license: {str(e)}"}, status=400)

        # Get the highest lfd_nr_field value
        id_ticket = Ticket.objects.aggregate(Max('id_ticket'))['id_ticket__max']
        if lfd_nr_field is None:
            lfd_nr_field = 1
        else:
            lfd_nr_field += 1

        # Retrieve the values from the React inputs
        
        lizenzname = request.data.get('lizenzname')
        schliessungsdatum = request.data.get('schliessungsdatum')
        erstellungsdatum = request.data.get('erstellungsdatum')
        status = request.data.get('status')
        beschreibung = request.data.get('beschreibung')
        titel = request.data.get('titel')
        admin_verwalter_id=request.data.get('admin_verwalter_id')
        dongle_seriennumemr = request.data.get('dongle_seriennumemr')
     

        try:
            ticket_data = {
                'id_ticket': id_ticket,
                'titel': titel,
                'lizenzname': lizenzname,
                'erstellungsdatum': erstellungsdatum,
                'schliessungsdatum': schliessungsdatum,
                'beschreibung': beschreibung,
                'status': status,
                'admin_verwalter_id': admin_verwalter_id,
                'dongle_seriennumemr': dongle_seriennumemr,
            }
            Ticket = Ticket(**ticket_data)
            Ticket.save()

            

            return JsonResponse({"success": "Die Lizenz wurde erfolgreich erstellt."}, status=201)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred while creating the license: {str(e)}"}, status=400)
# Create your views here.
