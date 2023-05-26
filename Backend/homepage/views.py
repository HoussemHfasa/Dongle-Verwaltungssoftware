from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Dongle  
from .serializers import DongleSerializer  
# Create your views here.  
  
class DongleView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Dongle.objects.all()  
        serializers = DongleSerializer(result, many=True)  
        return Response({'status': 'success', "Dongle":serializers.data}, status=200)  
  
      