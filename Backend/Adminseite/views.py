from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customuser
from .serializers import CustomuserSerializer


class CustomuserView(APIView):
    def get(self, request, *args, **kwargs):
        result = Customuser.objects.all()
        serializer = CustomuserSerializer(result, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=200)

    def post(self, request, *args, **kwargs):
        serializer = CustomuserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Customuser, pk=pk)
        serializer = CustomuserSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Customuser, pk=pk)
        instance.delete()
        return Response({'status': 'success', 'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)