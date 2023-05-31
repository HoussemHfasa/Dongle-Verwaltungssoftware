from django.db import models
from homepage.models import Dongle

# Lizenz-Modell
class Lizenz(models.Model):
    lfd_nr_field = models.IntegerField(db_column='Lfd. Nr.', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    firmcode = models.CharField(db_column='FirmCode', max_length=45)  # Field name made lowercase.
    productcode = models.IntegerField(db_column='ProductCode')  # Field name made lowercase.
    lizenzname = models.CharField(db_column='LizenzName', max_length=45)  # Field name made lowercase.
    einheiten = models.IntegerField(db_column='Einheiten', blank=True, null=True)  # Field name made lowercase.
    gueltig_von = models.DateField(db_column='Gueltig von')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gueltig_bis = models.DateField(db_column='Gueltig bis', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lizenzanzahl = models.IntegerField(db_column='LizenzAnzahl', blank=True, null=True)  # Field name made lowercase.
    mitarbeiter = models.CharField(db_column='Mitarbeiter', max_length=45)  # Field name made lowercase.
    projekt = models.CharField(db_column='Projekt', max_length=45)  # Field name made lowercase.
    kunde = models.CharField(db_column='Kunde', max_length=45)  # Field name made lowercase.
    dongle_serien_nr = models.CharField(db_column='Dongle_Serien-Nr', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'lizenz'
        unique_together = (('lfd_nr_field', 'dongle_serien_nr'),)