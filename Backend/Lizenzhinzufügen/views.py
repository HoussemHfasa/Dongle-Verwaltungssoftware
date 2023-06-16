from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Max
from .models import Lizenz
from .models import Dongle
from .serializers import LizenzSerializer
from .models import UserLogginCustomuser
from rest_framework.permissions import IsAuthenticated, BasePermission
#houssem
from datetime import date
    

class LizenzCreateView(APIView):

    def post(self, request, *args, **kwargs):
        print("Request data:", request.data)  # Debugging print statement

        serializer = LizenzSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print("Serializer error:", str(e))  # Debugging print statement
            return JsonResponse({"error": f"An error occurred while creating the license: {str(e)}"}, status=400)

        # Get the highest lfd_nr_field value
        lfd_nr_field = Lizenz.objects.aggregate(Max('lfd_nr_field'))['lfd_nr_field__max']
        if lfd_nr_field is None:
            lfd_nr_field = 1
        else:
            lfd_nr_field += 1

        # Retrieve the values from the React inputs
        
        lizenzname = request.data.get('lizenzname')
        gueltig_von = request.data.get('gueltig_von')
        gueltig_bis = request.data.get('gueltig_bis')
        projekt = request.data.get('projekt')
        einheiten = request.data.get('einheiten')
        productcode = request.data.get('productcode')
        mitarbeiter=request.data.get('mitarbeiter')
        #datum_erstausgabe =date.today()
        firmcode = request.data.get('firmcode')
        lizenzanzahl=request.data.get('lizenzanzahl')

        # Retrieve the customer name based on the email address
        serienNr=Dongle.objects.filter(firmcode=firmcode).first()
        if serienNr:
            dongle_serien_nr= serienNr.serien_nr
        else:
            dongle_serien_nr=""

        customer = UserLogginCustomuser.objects.filter(firm_code=firmcode).first()
        if customer:
            kunde = customer.name
            kunde_email = customer.email
        else:
            kunde = ""
            kunde_email = ""

        try:
            lizenz_data = {
                'lfd_nr_field': lfd_nr_field,
                'dongle_serien_nr': dongle_serien_nr,
                'lizenzname': lizenzname,
                'gueltig_von': gueltig_von,
                'gueltig_bis': gueltig_bis,
                'projekt': projekt,
                'kunde': kunde,
                'einheiten': einheiten,
                'productcode': productcode,
                'firmcode': firmcode,
                'mitarbeiter': mitarbeiter,
                'lizenzanzahl': lizenzanzahl
            }
            lizenz = Lizenz.objects.create(**lizenz_data)
            lizenz.save()

            # Send email to the customer
            email_subject = f"New license Created: {dongle_serien_nr}"
            email_body = f"Liebe {kunde},\n\n der Administrator hat Ihnen einen Lizenz zugewiesen mit der Seriennummer {dongle_serien_nr}.  \n\nEnglish Version:\n\nDear {kunde},\n\nThe administrator has assigned a license to you with the serial number: {dongle_serien_nr}."
            email = EmailMessage(email_subject, email_body, to=[kunde_email])
            email.send()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred while creating the license: {str(e)}"}, status=400)