from rest_framework import serializers
from .models import Dongle
from rest_framework import generics


class DongleSerializer(serializers.ModelSerializer):
    lfd_nr_field = serializers.IntegerField(required=False)  # Anpassung: Das Feld ist optional
    serien_nr = serializers.CharField()
    gueltig_von = serializers.DateField()
    gueltig_bis = serializers.DateField()
    projekt_produkt = serializers.CharField()
    kunde = serializers.CharField(required=False)
    standort = serializers.CharField()
    haendler = serializers.CharField()
    datum_letzte_aenderung = serializers.DateField()
    datum_erstausgabe = serializers.DateField()
    firmcode = serializers.CharField()
    name = serializers.CharField(allow_blank=True)
    standort = serializers.CharField(allow_blank=True)
    # Füge das kunde-Feld hinzu
    class Meta:
        model = Dongle
        fields = '__all__'

# View
class DongleCreateView(generics.CreateAPIView):
    queryset = Dongle.objects.all()
    serializer_class = DongleSerializer
