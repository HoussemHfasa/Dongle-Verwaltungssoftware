from django.db import models
from django.shortcuts import render
from .models import Dongle, Ticket
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
 
# Create your models here.
