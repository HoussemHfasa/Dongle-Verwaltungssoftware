from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Max
from .models import Lizenz
from Dongle_hinzufügen.models import Dongle
from .serializers import LizenzSerializer
from User_loggin.models import CustomUser


# LizenzCreateView ist eine Klasse, die zum Erstellen einer neuen Lizenz über eine API verwendet wird.
class LizenzCreateView(APIView):

    def post(self, request, *args, **kwargs):
        print("Request data:", request.data)  # Debugging print statement

        serializer = LizenzSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print("Serializer error:", str(e))  # Debugging print statement
            return JsonResponse({"error": f"An error occurred while creating the license: {str(e)}"}, status=400)

        # Hole den höchsten Wert von lfd_nr_field
        lfd_nr_field = Lizenz.objects.aggregate(Max('lfd_nr_field'))['lfd_nr_field__max']
        if lfd_nr_field is None:
            lfd_nr_field = 1
        else:
            lfd_nr_field += 1

        # Werte aus den React-Eingaben abrufen
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
        dongle_serien_nr = request.data.get('dongle_serien_nr')
        if dongle_serien_nr:
            dongle = Dongle.objects.filter(serien_nr=dongle_serien_nr).first()
            if not dongle:
                return JsonResponse({"error": "'dongle_serien_nr' nicht vorhanden."}, status=400)
        else:
            dongle_serien_nr = ""


        customer = CustomUser.objects.filter(firm_code=firmcode).first()
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
            lizenz = Lizenz(**lizenz_data)
            lizenz.save()

            # E-Mail senden
            subject = f"Neue Lizenz erstellt: {lizenzname}"
            message = f"Es wurde eine neue Lizenz erstellt:\n\n" \
                      f"Lizenzname: {lizenzname}\n" \
                      f"Gültig von: {gueltig_von}\n" \
                      f"Gültig bis: {gueltig_bis}\n" \
                      f"Projekt: {projekt}\n" \
                      f"Einheiten: {einheiten}\n" \
                      f"Productcode: {productcode}\n" \
                      f"Firmcode: {firmcode}\n" \
                      f"Mitarbeiter: {mitarbeiter}\n" \
                      f"Lizenzanzahl: {lizenzanzahl}\n" \
                      f"Dongle Seriennummer: {dongle_serien_nr}\n"

            send_mail(
                subject=subject,
                message=message,
                from_email="sender@example.com",
                recipient_list=[kunde_email],
                fail_silently=True,
            )

            return JsonResponse({"success": "Die Lizenz wurde erfolgreich erstellt."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred while creating the license: {str(e)}"}, status=400)