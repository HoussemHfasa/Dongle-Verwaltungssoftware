from rest_framework import serializers
from .models import Dongle



# Dongle-Serializer-Klasse
class DongleSerializer(serializers.ModelSerializer):
    # Felder des Dongle-Serializers
    lfd_nr_field = serializers.IntegerField()
    serien_nr = serializers.CharField(max_length=45)
    name = serializers.CharField(max_length=45)
    gueltig_von = serializers.DateField()
    gueltig_bis = serializers.DateField()
    projekt_produkt = serializers.CharField(max_length=45)
    kunde = serializers.CharField(max_length=45)
    standort = serializers.CharField(max_length=45)
    haendler = serializers.CharField(max_length=45)
    datum_letzte_aenderung  = serializers.DateField()
    datum_erstausgabe = serializers.DateField()
    firmcode = serializers.CharField(max_length=45)

    class Meta:
        # Verknüpfung des Serializers mit dem Dongle-Modell
        model = Dongle
        # Alle Felder des Modells werden serialisiert
        fields = '__all__'