from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Customuser

class CustomuserSerializer(serializers.ModelSerializer):
    id = models.BigAutoField(primary_key=True)
    last_login = serializers.DateTimeField(required=False, allow_null=True)
    is_superuser = serializers.IntegerField()
    email = serializers.CharField(max_length=254, validators=[UniqueValidator(queryset=Customuser.objects.all())])
    name = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    role = serializers.CharField(max_length=10)
    firm_code = serializers.CharField(max_length=45, allow_blank=True, allow_null=True)

    class Meta:
        model = Customuser
        fields = '__all__'