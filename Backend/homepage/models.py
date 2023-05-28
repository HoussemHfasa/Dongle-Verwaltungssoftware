from django.db import models

# Dongle-Modell
class Dongle(models.Model):
    # Laufende Nummer (Primärschlüssel)
    lfd_nr_field = models.IntegerField(db_column='Lfd. Nr.', primary_key=True)
    
    # Seriennummer
    serien_nr = models.CharField(db_column='Serien-Nr', max_length=45)
    
    # Name des Dongles
    name = models.CharField(db_column='Name', max_length=45)
    
    # Gültigkeitsbeginn
    gueltig_von = models.DateField(db_column='Gueltig von')
    
    # Gültigkeitsende
    gueltig_bis = models.DateField(db_column='Gueltig bis')
    
    # Projekt oder Produkt, für das der Dongle verwendet wird
    projekt_produkt = models.CharField(db_column='Projekt/Produkt', max_length=45)
    
    # Standort des Dongles
    standort = models.CharField(db_column='Standort', max_length=45)
    
    # Händler, der den Dongle verkauft hat
    haendler = models.CharField(db_column='Haendler', max_length=45)
    
    # Datum der letzten Änderung
    datum_letzte_aenderung = models.DateField(db_column='Datum letzte Aenderung')
    
    # Datum der Erstausgabe
    datum_erstausgabe = models.DateField(db_column='Datum Erstausgabe')
    
    # Benutzer und Firmencode
    benutzer_firmcode = models.CharField(db_column='Benutzer_Firmcode', max_length=45)

    class Meta:
        
        managed = False
        db_table = 'dongle'
        
        unique_together = (('lfd_nr_field', 'benutzer_firmcode'),)