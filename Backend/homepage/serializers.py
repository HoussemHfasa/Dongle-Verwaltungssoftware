from rest_framework import serializers
from .models import Dongle


class DongleSerializer(serializers.ModelSerializer):
    # Laufende Nummer (Primärschlüssel)
    lfd_nr_field = serializers.IntegerField()
        
    # Seriennummer
    serien_nr = serializers.CharField(max_length=45)
    
    # Name des Dongles
    name = serializers.CharField(max_length=45)
    
    # Gültigkeitsbeginn
    gueltig_von = serializers.DateField()
    
    # Gültigkeitsende
    gueltig_bis = serializers.DateField()
    
    # Projekt oder Produkt, für das der Dongle verwendet wird
    projekt_produkt = serializers.CharField(max_length=45)
    
    #houssem
    kunde=serializers.CharField(max_length=45)
    # Standort des Dongles
    standort = serializers.CharField(max_length=45)
    
    # Händler, der den Dongle verkauft hat
    haendler = serializers.CharField(max_length=45)
    
    # Datum der letzten Änderung
    datum_letzte_aenderung  = serializers.DateField()
    
    # Datum der Erstausgabe
    datum_erstausgabe = serializers.DateField()
    firmcode = serializers.CharField(max_length=45)

    class Meta:
        # Verknüpfung des Serializers mit dem Dongle-Modell
        model = Dongle
        
        # Alle Felder des Modells werden serialisiert
        fields = '__all__'