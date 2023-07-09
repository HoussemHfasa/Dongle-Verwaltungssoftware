from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Max
from DongleAnfordern.models import Ticket
from Lizenzhinzufügen.models import Lizenz
from Lizenzhinzufügen.serializers import LizenzSerializer
from Dongle_hinzufügen.models import Dongle
from Dongle_hinzufügen.serializers import DongleSerializer
from User_loggin.models import CustomUser
import datetime
from django.db.models import Max
#from .serializers import TicketSerializer
from DongleAnfordern.serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
#houssem
from datetime import date
from rest_framework import generics #yassin
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.permissions import IsAuthenticated


class TicketAnnehmenView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):      
        ticket_id = request.data.get("id_ticket")
        Mitarbeiter=request.data.get("Mitarbeiter_email")
        ticket = Ticket.objects.get(id_ticket=ticket_id)

        if ticket.dongle_lizenz == 1:
            # Create a new Lizenz
             lfd_nr_field = Lizenz.objects.aggregate(Max('lfd_nr_field'))['lfd_nr_field__max']
             if lfd_nr_field is None:
              lfd_nr_field = 1
             else:   
              lfd_nr_field += 1

             if ticket.dongle_seriennummer:
                dongle = Dongle.objects.filter(serien_nr=ticket.dongle_seriennummer).first()
             if not dongle:
                return JsonResponse({"error": "'dongle_serien_nr' nicht vorhanden."}, status=400)
             
               # Retrieve the customer name based on the email address
             customer = CustomUser.objects.filter(firm_code=ticket.firmcode).first()
             if customer:
                kunde = customer.name
                kunde_Firmcode = customer.firm_code
             else:
                return JsonResponse({"error": "Der FirmCode ist nicht vorhanden."}, status=400)

             try:
                 new_lizenz_data = {
                 'lfd_nr_field': lfd_nr_field,
                 'lizenzname': ticket.lizenzname,
                 'gueltig_von': ticket.gueltig_von,
                 'gueltig_bis': ticket.gueltig_bis,
                 'kunde':kunde,
                'projekt': ticket.projekt,
                'einheiten': ticket.einheiten,
                'productcode': ticket.productcode,
                'firmcode': kunde_Firmcode,
                'mitarbeiter': ticket.admin_verwalter_email,
                'lizenzanzahl': ticket.lizenzanzahl,
                'dongle_serien_nr': ticket.dongle_seriennummer
                
                   }
                 lizenz = Lizenz(**new_lizenz_data)
                 lizenz.save()
                 # Send an email notification
                 subject = f"Neue Lizenz erstellt: {ticket.lizenzname}"
                 message = f"Es wurde eine neue Lizenz erstellt:\n\n" \
                      f"Lizenzname: {ticket.lizenzname}\n" \
                      f"Gültig von: {ticket.gueltig_von}\n" \
                      f"Gültig bis: {ticket.gueltig_bis}\n" \
                      f"Projekt: {ticket.projekt}\n" \
                      f"Einheiten: {ticket.einheiten}\n" \
                      f"Productcode: {ticket.productcode}\n" \
                      f"Firmcode: {kunde_Firmcode}\n" \
                      f"Mitarbeiter: {Mitarbeiter}\n" \
                      f"Lizenzanzahl: {ticket.lizenzanzahl}\n" \
                      f"Dongle Seriennummer: {ticket.dongle_seriennummer}\n"

                 send_mail(
                subject=subject,
                message=message,
                from_email="sender@example.com",
                recipient_list=[customer.email],
                fail_silently=True,
            )
                 ticket.status = "angenommen"
                 ticket.admin_verwalter_email=Mitarbeiter
                 ticket.grund_der_ablehnung="keine"
                 ticket.save()
                 return Response({"success": "Lizenz wurde angenommen und erstellt."}, status=status.HTTP_201_CREATED)      
             except Exception as e:
                return JsonResponse({"error": f"An error occurred while creating the dongle: {str(e)}"}, status=400)
        else:
            # Get the highest lfd_nr_field value
            lfd_nr_field = Dongle.objects.aggregate(Max('lfd_nr_field'))['lfd_nr_field__max']
            if lfd_nr_field is None:
                lfd_nr_field = 1
            else:
                lfd_nr_field += 1

            # Retrieve the customer name based on the email address
            customer = CustomUser.objects.filter(firm_code=ticket.firmcode).first()
            if customer:
                kunde = customer.name
                kunde_Firmcode = customer.firm_code
            else:
                kunde = ""
                kunde_Firmcode = ""
            try:
                new_dongle_data = {
                       'lfd_nr_field': lfd_nr_field,
                      'serien_nr': ticket.dongle_seriennummer,
                      'name': ticket.dongle_name,
                      'gueltig_von': ticket.gueltig_von,
                      'gueltig_bis': ticket.gueltig_bis,
                      'projekt_produkt': ticket.projekt,
                      'kunde': kunde,
                      'standort': ticket.standort,
                      'haendler': ticket.haendler,
                      'datum_letzte_aenderung': datetime.date(2020, 5, 21),
                      'datum_erstausgabe': datetime.date(2020, 5, 21),
                      'firmcode': kunde_Firmcode
                }

                dongle = Dongle.objects.create(**new_dongle_data)
                dongle.save()
                email_subject = f"New Dongle Created: {ticket.dongle_seriennummer}"
                email_body = f"Liebe {kunde},\n\n der Administrator hat Ihnen einen Dongle zugewiesen mit der Seriennummer {ticket.dongle_seriennummer}.  \n\nEnglish Version:\n\nDear {kunde},\n\nThe administrator has assigned a dongle to you with the serial number: {ticket.dongle_seriennummer}."
                email = EmailMessage(subject=email_subject, body=email_body, to=[customer.email])
                email.send()
                ticket.status = "angenommen"
                ticket.admin_verwalter_email=Mitarbeiter;
                ticket.grund_der_ablehnung="keine"
                ticket.save()
                return Response({"success": "Der Dongle wurde angenommen und erstellt."}, status=status.HTTP_201_CREATED)      
            except Exception as e:
                return JsonResponse({"error": f"An error occurred while creating the dongle: {str(e)}"}, status=400)


class TicketAblehnenView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        ticket_id = request.data.get("id_ticket")
        grund_der_ablehnung = request.data.get("grund_der_ablehnung")
        ticket = Ticket.objects.get(id_ticket=ticket_id)

        # Update the ticket status and store the reason for rejection
        ticket.status = "abgelehnt"
        ticket.grund_der_ablehnung = grund_der_ablehnung
        ticket.save()

        return JsonResponse({"success": "Die Lizenz wurde abgelehnt."}, status=200)


#yassin

class TicketDetailsView(generics.RetrieveUpdateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
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

    