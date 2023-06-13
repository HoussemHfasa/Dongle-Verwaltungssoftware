from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Max
from .models import Dongle
from .serializers import DongleSerializer
from .models import UserLogginCustomuser

class DongleCreateView(APIView):
    def post(self, request, *args, **kwargs):
        print("Request data:", request.data)  # Debugging print statement

        serializer = DongleSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print("Serializer error:", str(e))  # Debugging print statement
            return JsonResponse({"error": f"An error occurred while creating the dongle: {str(e)}"}, status=400)

        # Get the highest lfd_nr_field value
        lfd_nr_field = Dongle.objects.aggregate(Max('lfd_nr_field'))['lfd_nr_field__max']
        if lfd_nr_field is None:
            lfd_nr_field = 1
        else:
            lfd_nr_field += 1

        # Retrieve the values from the React inputs
        serien_nr = request.data.get('serien_nr')
        name = request.data.get('name')
        gueltig_von = request.data.get('gueltig_von')
        gueltig_bis = request.data.get('gueltig_bis')
        projekt_produkt = request.data.get('projekt_produkt')
        standort = request.data.get('standort')
        haendler = request.data.get('haendler')
        datum_letzte_aenderung = request.data.get('datum_letzte_aenderung')
        datum_erstausgabe = request.data.get('datum_erstausgabe')
        firmcode = request.data.get('firmcode')

        # Retrieve the customer name based on the email address
        customer = UserLogginCustomuser.objects.filter(firm_code=firmcode).first()
        if customer:
            kunde = customer.name
            kunde_email = customer.email
        else:
            kunde = ""
            kunde_email = ""

        try:
            dongle_data = {
                'lfd_nr_field': lfd_nr_field,
                'serien_nr': serien_nr,
                'name': name,
                'gueltig_von': gueltig_von,
                'gueltig_bis': gueltig_bis,
                'projekt_produkt': projekt_produkt,
                'kunde': kunde,
                'standort': standort,
                'haendler': haendler,
                'datum_letzte_aenderung': datum_letzte_aenderung,
                'datum_erstausgabe': datum_erstausgabe,
                'firmcode': firmcode
            }
            dongle = Dongle.objects.create(**dongle_data)
            dongle.save()

            # Send email to the customer
            email_subject = f"New Dongle Created: {serien_nr}"
            email_body = f"Liebe {kunde},\n\n der Administrator hat Ihnen einen Dongle zugewiesen mit der Seriennummer {serien_nr}.  \n\nEnglish Version:\n\nDear {kunde},\n\nThe administrator has assigned a dongle to you with the serial number: {serien_nr}."
            email = EmailMessage(subject=email_subject, body=email_body, to=[kunde_email])
            email.send()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred while creating the dongle: {str(e)}"}, status=400)