from rest_framework import serializers
from .models import Dongle

class DongleSerializer(serializers.ModelSerializer):
    lfd_nr_field = serializers.IntegerField()
    serien_nr = serializers.CharField(max_length=45)
    name = serializers.CharField(max_length=45)
    gueltig_von = serializers.DateField()
    gueltig_bis = serializers.DateField()
    projekt_produkt = serializers.CharField(max_length=45)
    standort = serializers.CharField(max_length=45)
    haendler = serializers.CharField(max_length=45)
    #datum_letzte_anderung = serializers.DateField()
    datum_erstausgabe = serializers.DateField()
    benutzer_firmcode = serializers.IntegerField()

    class Meta:
        model = Dongle
        fields = '__all__'