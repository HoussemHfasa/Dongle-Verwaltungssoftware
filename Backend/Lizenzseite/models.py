
# Create your models here.
from django.db import models
from homepage.models import Dongle


class Lizenz(models.Model):
    lfd_nr_field = models.IntegerField(db_column='Lfd. Nr.', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    productcode = models.IntegerField(db_column='ProductCode')  # Field name made lowercase.
    lizenzname = models.CharField(db_column='LizenzName', max_length=45)  # Field name made lowercase.
    einheiten = models.IntegerField(db_column='Einheiten', blank=True, null=True)  # Field name made lowercase.
    gueltig_von = models.DateField(db_column='Gueltig von')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ablaufdatum = models.DateField(db_column='Ablaufdatum')  # Field name made lowercase.
    lizenzanzahl = models.IntegerField(db_column='LizenzAnzahl')  # Field name made lowercase.
    mitarbeiter = models.CharField(db_column='Mitarbeiter', max_length=45)  # Field name made lowercase.
    projekt = models.CharField(db_column='Projekt', max_length=45)  # Field name made lowercase.
    dongle_lfd_nr_field = models.ForeignKey(Dongle, models.DO_NOTHING, db_column='dongle_Lfd. Nr.')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'lizenz'
        unique_together = (('lfd_nr_field', 'dongle_lfd_nr_field'),)
        