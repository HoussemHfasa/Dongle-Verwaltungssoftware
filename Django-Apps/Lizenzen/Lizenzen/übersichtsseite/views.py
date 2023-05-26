from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import YourModel

def get_table_data(request):
    data = dongle.objects.values(
        'lfd_nr',
        'serien_nr',
        'name',
        'gueltig_von',
        'gueltig_bis',
        'projekt_produkt',
        'standort',
        'haendler',
        'datum_letzte_aenderung',
        'datum_erstausgabe',
        'benutzer_firmcode',
    )
    return JsonResponse(list(data), safe=False)

