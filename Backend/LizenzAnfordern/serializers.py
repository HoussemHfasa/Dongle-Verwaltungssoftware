from rest_framework import serializers
from .models import Ticket
from rest_framework import generics


class TicketSerializer(serializers.ModelSerializer):
    id_ticket = serializers.IntegerField()
    titel = serializers.CharField()
    beschreibung = serializers.CharField()
    status = serializers.CharField(required=False)
    erstellungsdatum = serializers.DateField()
    schliessungsdatum = serializers.DateField()
    grund_der_ablehnung=serializers.CharField(required=False)
    dongle_lizenz = serializers.IntegerField(required=False)
    dongle_name = serializers.CharField(required=False)
    dongle_seriennummer = serializers.CharField(required=False, allow_blank=True)
    lizenzname = serializers.CharField()
    firmcode = serializers.CharField()
    gueltig_von = serializers.DateField()
    gueltig_bis = serializers.DateField()
    einheiten = serializers.IntegerField()
    projekt = serializers.CharField()
    admin_verwalter_email = serializers.CharField(required=False)
    haendler = serializers.CharField(required=False)
    standort = serializers.CharField(required=False)
    productcode = serializers.IntegerField()
    lizenzanzahl = serializers.IntegerField()

    class Meta:
        model = Ticket
        fields = '__all__'
