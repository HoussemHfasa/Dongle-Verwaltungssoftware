from rest_framework import serializers  
from .models import Dongle  
  
class DongleSerializer(serializers.ModelSerializer):  
    lfd_nr_field = serializers.CharField(max_length=200, required=True)  
    serien_nr = serializers.CharField(max_length=200, required=True)  
    name = serializers.CharField(max_length=200, required=True)  
    
    class Meta:  
        model = Dongle  
        fields = ('__all__')  