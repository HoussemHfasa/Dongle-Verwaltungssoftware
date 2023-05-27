from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Lizenz  
from .serializers import LizenzSerializer  
# Create your views here.  
  
class LizenzView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Lizenz.objects.all()  
        serializers = LizenzSerializer(result, many=True)  
        return Response({'status': 'success', "Lizenz":serializers.data}, status=200)  
  
      