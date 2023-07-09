from rest_framework import serializers
from .models import Dongle
from rest_framework import generics


# Serializer für das Dongle-Modell zur Umwandlung von Django-Objekten in JSON
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
def validate(self, attrs):
        if not attrs['serien_nr']:
            raise serializers.ValidationError("Seriennummer ist erforderlich.")
        if not attrs['name']:
            raise serializers.ValidationError("Name ist erforderlich.")
        if not attrs['gueltig_von']:
            raise serializers.ValidationError("Gültig von ist erforderlich.")
        if not attrs['gueltig_bis']:
            raise serializers.ValidationError("Gültig bis ist erforderlich.")
        if not attrs['projekt_produkt']:
            raise serializers.ValidationError("Projekt/Produkt ist erforderlich.")
        if not attrs['standort']:
            raise serializers.ValidationError("Standort ist erforderlich.")
        if not attrs['haendler']:
            raise serializers.ValidationError("Händler ist erforderlich.")
        if not attrs['datum_letzte_aenderung']:
            raise serializers.ValidationError("Datum der letzten Änderung ist erforderlich.")
        if not attrs['datum_erstausgabe']:
            raise serializers.ValidationError("Datum der Erstausgabe ist erforderlich.")
        if not attrs['firmcode']:
            raise serializers.ValidationError("Firmcode ist erforderlich.")

        return attrs