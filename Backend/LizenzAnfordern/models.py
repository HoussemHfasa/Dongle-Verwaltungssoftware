from django.db import models

class Ticket(models.Model):
    id_ticket = models.IntegerField(db_column='ID_Ticket',primary_key=True)  # Field name made lowercase.
    titel = models.CharField(db_column='Titel', max_length=45)  # Field name made lowercase.
    beschreibung = models.CharField(db_column='Beschreibung', max_length=45)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45)  # Field name made lowercase.
    erstellungsdatum = models.DateField(db_column='Erstellungsdatum')  # Field name made lowercase.
    schliessungsdatum = models.DateField(db_column='Schliessungsdatum', blank=True, null=True)  # Field name made lowercase.
    admin_verwalter_id = models.IntegerField(db_column='Admin/Verwalter_ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dongle_seriennummer = models.CharField(db_column='Dongle_seriennumemr', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lizenzname = models.CharField(db_column='LizenzName', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ticket'
