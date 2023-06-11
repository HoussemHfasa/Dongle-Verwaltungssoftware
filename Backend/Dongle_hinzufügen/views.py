from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Max
from .models import Dongle
from .serializers import DongleSerializer
from .models import UserLogginCustomuser


class DongleCreateView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = DongleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Den höchsten lfd_nr_field-Wert des aktuellen Benutzers abrufen
        lfd_nr_field = Dongle.objects.filter(created_by=request.user).aggregate(Max('lfd_nr_field'))[
            'lfd_nr_field__max']
        if lfd_nr_field is None:
            lfd_nr_field = 1
        else:
            lfd_nr_field += 1

        # Die Werte aus den React-Eingaben abrufen
        serien_nr = request.data.get('serien_nr')
        name = request.data.get('name')
        gueltig_von = request.data.get('gueltig_von')
        gueltig_bis = request.data.get('gueltig_bis')
        projekt_produkt = request.data.get('projekt_produkt')
        kunde_email = request.data.get('email')
        standort = request.data.get('standort')
        haendler = request.data.get('haendler')
        datum_letzte_aenderung = request.data.get('datum_letzte_aenderung')
        datum_erstausgabe = request.data.get('datum_erstausgabe')
        firmcode = request.data.get('firmcode')

        # Den Kundenname basierend auf der E-Mail-Adresse abrufen
        customer = UserLogginCustomuser.objects.filter(email=kunde_email).first()
        if customer:
            kunde = customer.name
        else:
            kunde = ""

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
            return Response({"success": "Dongle created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)