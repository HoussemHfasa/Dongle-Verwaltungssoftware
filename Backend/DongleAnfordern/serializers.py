from rest_framework import serializers
from .models import Ticket
from rest_framework import generics


class TicketSerializer(serializers.ModelSerializer):
    id_ticket = serializers.IntegerField(required=False)
    titel = serializers.CharField()
    beschreibung = serializers.CharField()
    status = serializers.CharField(required=False)
    erstellungsdatum = serializers.DateField()
    schliessungsdatum = serializers.DateField()
    grund_der_ablehnung=serializers.CharField(required=False)
    dongle_lizenz = serializers.CharField(required=False)
    dongle_name = serializers.CharField()
    dongle_seriennummer = serializers.CharField()
    lizenzname = serializers.CharField(required=False)
    firmcode = serializers.CharField()
    gueltig_von = serializers.DateField()
    gueltig_bis = serializers.DateField()
    einheiten = serializers.IntegerField(required=False)
    projekt = serializers.CharField()
    admin_verwalter_email = serializers.CharField(required=False)
    haendler = serializers.CharField()
    standort = serializers.CharField()

    class Meta:
        model = Ticket
        fields = '__all__'
