from rest_framework import serializers
from .models import Ticket
from rest_framework import generics


class TicketSerializer(serializers.ModelSerializer):
    id_ticket = serializers.IntegerField(required=False)
    titel = serializers.CharField()
    beschreibung = serializers.CharField(allow_blank=True)
    erstellungsdatum = serializers.DateField()
    schliessungsdatum = serializers.DateField()
    admin_verwalter_id = serializers.IntegerField()
    status = serializers.CharField()
    dongle_seriennumemr = serializers.CharField(required=False, allow_blank=True)
    lizenzname = serializers.CharField()

    class Meta:
        model = Ticket
        fields = '__all__'

# View
class DongleCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
