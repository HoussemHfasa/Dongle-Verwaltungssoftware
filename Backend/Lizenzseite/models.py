from django.db import models
from homepage.models import Dongle

# Lizenz-Modell
class Lizenz(models.Model):
    # Laufende Nummer (Primärschlüssel)
    lfd_nr_field = models.IntegerField(db_column='Lfd. Nr.', primary_key=True)
    
    # Produktcode
    productcode = models.IntegerField(db_column='ProductCode')
    
    # Lizenzname
    lizenzname = models.CharField(db_column='LizenzName', max_length=45)
    
    # Anzahl der Einheiten (optional)
    einheiten = models.IntegerField(db_column='Einheiten', blank=True, null=True)
    
    # Gültigkeitsbeginn
    gueltig_von = models.DateField(db_column='Gueltig von')
    
    # Ablaufdatum der Lizenz
    ablaufdatum = models.DateField(db_column='Ablaufdatum')
    
    # Anzahl der Lizenzen
    lizenzanzahl = models.IntegerField(db_column='LizenzAnzahl')
    
    # Mitarbeiter, der die Lizenz verwendet
    mitarbeiter = models.CharField(db_column='Mitarbeiter', max_length=45)
    
    # Projekt, für das die Lizenz verwendet wird
    projekt = models.CharField(db_column='Projekt', max_length=45)
    
    # Fremdschlüsselbeziehung zum Dongle-Modell (Laufende Nummer des Dongles)
    dongle_lfd_nr_field = models.ForeignKey(Dongle, models.DO_NOTHING, db_column='dongle_Lfd. Nr.')

    class Meta:        
        managed = False
        db_table = 'lizenz'
        unique_together = (('lfd_nr_field', 'dongle_lfd_nr_field'),)