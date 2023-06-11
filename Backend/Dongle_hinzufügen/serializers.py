from rest_framework import serializers
from .models import Dongle

class DongleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dongle
        fields = '__all__'
