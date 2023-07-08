from rest_framework import serializers
from .models import Ticket
from rest_framework import generics


class TicketSerializer(serializers.ModelSerializer):
    id_ticket = serializers.IntegerField(required=False)
    titel = serializers.CharField()
    beschreibung = serializers.CharField(max_length=255)
    status = serializers.CharField(required=False)
    erstellungsdatum = serializers.DateField()
    schliessungsdatum = serializers.DateField(required=False, allow_null=True)
    grund_der_ablehnung = serializers.CharField(required=False, allow_null=True)
    dongle_lizenz = serializers.IntegerField(required=False, allow_null=True)
    dongle_name = serializers.CharField(required=False, allow_null=True)
    dongle_seriennummer = serializers.CharField(required=False, allow_null=True,allow_blank=True)
    lizenzname = serializers.CharField(required=False, allow_null=True)
    firmcode = serializers.CharField()
    gueltig_von = serializers.DateField(required=False, allow_null=True)
    gueltig_bis = serializers.DateField(required=False, allow_null=True)
    einheiten = serializers.IntegerField(required=False, allow_null=True)
    projekt = serializers.CharField(required=False, allow_null=True)
    admin_verwalter_email = serializers.CharField(required=False, allow_null=True)
    haendler = serializers.CharField(required=False, allow_null=True)
    standort = serializers.CharField(required=False, allow_null=True)
    productcode = serializers.IntegerField(required=False, allow_null=True)
    lizenzanzahl = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Ticket
        fields = '__all__'