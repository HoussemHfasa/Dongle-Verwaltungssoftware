from rest_framework import serializers
from ..models import Ticket, Dognle

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

        