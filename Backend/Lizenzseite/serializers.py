from rest_framework import serializers
from .models import Lizenz
from homepage.models import Dongle

class LizenzSerializer(serializers.ModelSerializer):
    # Laufende Nummer (Primärschlüssel)
    lfd_nr_field = serializers.IntegerField()
    
    # Produktcode
    productcode = serializers.IntegerField()
    
    firmcode= serializers.CharField(max_length=45)

    productcode=serializers.IntegerField()
    # Lizenzname
    lizenzname = serializers.CharField(max_length=45)
    
    # Anzahl der Einheiten
    einheiten = serializers.IntegerField()
    
    # Gültigkeitsbeginn
    gueltig_von = serializers.DateField()
    
    # Ablaufdatum der Lizenz
    gueltig_bis = serializers.DateField()
    
    # Anzahl der Lizenzen
    lizenzanzahl = serializers.IntegerField()
    
    # Mitarbeiter, der die Lizenz verwendet
    mitarbeiter = serializers.CharField(max_length=45)
    
    # Projekt, für das die Lizenz verwendet wird
    projekt = serializers.CharField(max_length=45)
    
    kunde=serializers.CharField(max_length=45)
    # Primärschlüsselbezogenes Feld für den Dongle (Laufende Nummer des Dongles)
    dongle_serien_nr = serializers.PrimaryKeyRelatedField(queryset=Dongle.objects.all())



    class Meta:
        model = Lizenz
        fields = '__all__'