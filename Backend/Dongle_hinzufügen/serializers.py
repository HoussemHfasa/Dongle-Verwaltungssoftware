from rest_framework import serializers
from .models import Dongle
from rest_framework import generics


class DongleSerializer(serializers.ModelSerializer):
    lfd_nr_field = serializers.IntegerField(required=False)  # Anpassung: Das Feld ist optional

    class Meta:
        model = Dongle
        fields = ['lfd_nr_field', 'serien_nr', 'name', 'gueltig_von', 'gueltig_bis', 'projekt_produkt', 'kunde', 'standort', 'haendler', 'datum_letzte_aenderung', 'datum_erstausgabe', 'firmcode']

# View
class DongleCreateView(generics.CreateAPIView):
    queryset = Dongle.objects.all()
    serializer_class = DongleSerializer
