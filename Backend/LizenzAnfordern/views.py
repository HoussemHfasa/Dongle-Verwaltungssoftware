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
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated
#testing
import random
import string
from datetime import datetime, timedelta
 
def random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))


class TicketCreateViewL(APIView):
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
        #datum_erstausgabe =date.today()
        firmcode = request.data.get('firmcode')

        # Retrieve the customer name based on the email address
        #customer = UserLogginCustomuser.objects.filter(firm_code=firmcode).first()
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
        lizenzname = request.data.get('lizenzname')
        lizenzanzahl= request.data.get('lizenzanzahl')

        try:
            ticket_data = {
                'id_ticket': random.randint(1, 1000),
                'titel': random_string(10),
                'beschreibung': random_string(50),
                'status': random.choice(['offen', 'geschlossen']),
                'erstellungsdatum': datetime.now().date(),
                'schliessungsdatum': (datetime.now() + timedelta(days=random.randint(1, 10))).date(),
                'dongle_lizenz': random.randint(1, 10),
                'dongle_name': random_string(5),
                'dongle_seriennummer': random_string(10),
                'lizenzname': random_string(10),
                'firmcode': random_string(8),
                'gueltig_von': datetime.now().date(),
                'gueltig_bis': (datetime.now() + timedelta(days=random.randint(1, 365))).date(),
                'einheiten': random.randint(1, 100),
                'projekt': random_string(15),
                'grund_der_ablehnung': random_string(20),
                'admin_verwalter_email': f"{random_string(5)}@example.com",
                'haendler': random_string(10),
                'standort': random_string(10),
                'productcode': random.randint(1, 1000),
                'lizenzanzahl': random.randint(1, 100),
            }
            new_ticket = Ticket(**ticket_data)
            new_ticket.save()

            return JsonResponse({"success": "Die Lizenz wurde erfolgreich erstellt."}, status=201)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred while creating the license: {str(e)}"}, status=400)




#houssem

# ... other imports

def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class TicketAnnehmenView(APIView):
    def post(self, request, *args, **kwargs):
         
        ticket_id = request.data.get("id_ticket")
        Mitarbeiter=request.data.get("Mitarbeiter_email")
        print("Request data: 3asba", request.data," Ticket id",ticket_id)
        ticket = Ticket.objects.get(id_ticket=ticket_id)


        if ticket_id == 1:
            # Create a new Lizenz
             lfd_nr_field = Lizenz.objects.aggregate(Max('lfd_nr_field'))['lfd_nr_field__max']
             if lfd_nr_field is None:
              lfd_nr_field = 1
             else:   
              lfd_nr_field += 1

             if ticket.dongle_seriennumemr:
                dongle = Dongle.objects.filter(serien_nr=ticket.dongle_seriennumemr).first()
             if not dongle:
                return JsonResponse({"error": "'dongle_serien_nr' nicht vorhanden."}, status=400)
             else:
               dongle_serien_nr = ""
               # Retrieve the customer name based on the email address
             customer = CustomUser.objects.filter(firm_code=ticket.firmcode).first()
             if customer:
                kunde = customer.name
                kunde_Firmcode = customer.firm_code
             else:
                kunde = ""
                kunde_Firmcode = ""
             try:
                 new_lizenz_data = {
                 'lizenzname': ticket.lizenzname,
                 'gueltig_von': ticket.gueltig_von,
                 'gueltig_bis': ticket.gueltig_bis,
                'projekt': ticket.projekt,
                'einheiten': ticket.einheiten,
                'productcode': ticket.productcode,
                'firmcode': kunde_Firmcode,
                'mitarbeiter': ticket.admin_verwalter_email,
                'lizenzanzahl': ticket.lizenzanzahl,
                'dongle_serien_nr': ticket.dongle_seriennumemr
                
                   }
                 lizenz = Lizenz(**new_lizenz_data)
                 lizenz.save()

                 ticket.status = "angenommen"
                 ticket.admin_verwalter_email=Mitarbeiter
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
                print("eli normalement tsaiva id teeou", lfd_nr_field)
                ticket.status = "angenommen"
                ticket.admin_verwalter_email=Mitarbeiter;
                ticket.save()
                return Response({"success": "Der Dongle wurde angenommen und erstellt."}, status=status.HTTP_201_CREATED)      
            except Exception as e:
                return JsonResponse({"error": f"An error occurred while creating the dongle: {str(e)}"}, status=400)


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

    