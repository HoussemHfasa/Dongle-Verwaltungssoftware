from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Lizenzhinzufügen.models import Lizenz
from .serializers import LizenzSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

# LizenzView ist eine Klasse, die Lizenzen anzeigt, basierend auf der Rolle und dem FirmCode des authentifizierten Benutzers.
class LizenzView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user_role = request.user.role
        user_firmcode = request.user.firm_code

        if user_role == 'Admin':
            result = Lizenz.objects.all()
        elif user_role == 'Verwalter':
            result = Lizenz.objects.all()
        elif user_role == 'Kunde':
            result = Lizenz.objects.filter(firmcode=user_firmcode, kunde=request.user.name)
        else:
            result = Lizenz.objects.none()
       
        
        serializers = LizenzSerializer(result, many=True)
        
        return Response({'status': 'success', "Lizenz": serializers.data}, status=200)