from django.db import models


class Ticket(models.Model):
    id_ticket = models.IntegerField(db_column='ID_Ticket', primary_key=True)  # Field name made lowercase.
    titel = models.CharField(db_column='Titel', max_length=45)  # Field name made lowercase.
    beschreibung = models.CharField(db_column='Beschreibung', max_length=45)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45)  # Field name made lowercase.
    erstellungsdatum = models.DateField(db_column='Erstellungsdatum')  # Field name made lowercase.
    schliessungsdatum = models.DateField(db_column='Schliessungsdatum', blank=True, null=True)  # Field name made lowercase.
    dongle_lizenz = models.IntegerField(db_column='Dongle/Lizenz', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dongle_name = models.CharField(db_column='Dongle_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dongle_seriennummer = models.CharField(db_column='Dongle_seriennumemr', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lizenzname = models.CharField(db_column='LizenzName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    firmcode = models.CharField(db_column='Firmcode', max_length=45)  # Field name made lowercase.
    gueltig_von = models.DateField(db_column='Gueltig von', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gueltig_bis = models.DateField(db_column='Gueltig bis', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    einheiten = models.IntegerField(db_column='Einheiten', blank=True, null=True)  # Field name made lowercase.
    projekt = models.CharField(db_column='Projekt', max_length=45, blank=True, null=True)  # Field name made lowercase.
    grund_der_ablehnung = models.CharField(db_column='Grund_der_Ablehnung', max_length=45, blank=True, null=True)  # Field name made lowercase.
    admin_verwalter_email = models.CharField(db_column='Admin/Verwalter_Email', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    haendler = models.CharField(db_column='Haendler', max_length=45, blank=True, null=True)  # Field name made lowercase.
    standort = models.CharField(db_column='Standort', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'ticket'