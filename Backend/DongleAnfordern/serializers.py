from rest_framework import serializers
from .models import Ticket
from rest_framework import generics


class TicketSerializer(serializers.ModelSerializer):
    id_ticket = serializers.IntegerField(required=False)
    titel = serializers.CharField()
    beschreibung = serializers.CharField()
    erstellungsdatum = serializers.DateField()
    schliessungsdatum = serializers.DateField()
    admin_verwalter_id = serializers.IntegerField(required=False)
    status = serializers.CharField(required=False)
    dongle_seriennummer = serializers.CharField()
    lizenzname = serializers.CharField(required=False)
    grund_der_ablehnung=serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Ticket
        fields = '__all__'
