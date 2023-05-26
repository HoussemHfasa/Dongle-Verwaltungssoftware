from django.db import models

# Create your models here.

from django.db import models

class YourModel(models.Model):
    lfd_nr = models.IntegerField()
    serien_nr = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    gueltig_von = models.DateField()
    gueltig_bis = models.DateField()
    projekt_produkt = models.CharField(max_length=100)
    standort = models.CharField(max_length=100)
    haendler = models.CharField(max_length=100)
    datum_letzte_aenderung = models.DateField()
    datum_erstausgabe = models.DateField()
    benutzer_firmcode = models.CharField(max_length=100)

    # Add any other fields and methods as needed

