from django.db import models

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

class Ticket(models.Model):
    id_ticket = models.IntegerField(db_column='ID_Ticket', primary_key=True) # Field name made lowercase. (yassin)
    titel = models.CharField(db_column='Titel', max_length=45)  # Field name made lowercase.
    beschreibung = models.CharField(db_column='Beschreibung', max_length=45)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45)  # Field name made lowercase.
    erstellungsdatum = models.DateField(db_column='Erstellungsdatum')  # Field name made lowercase.
    schliessungsdatum = models.DateField(db_column='Schliessungsdatum', blank=True, null=True)  # Field name made lowercase.
    admin_verwalter_id = models.IntegerField(db_column='Admin/Verwalter_ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
<<<<<<< HEAD
    dongle_seriennummer = models.CharField(db_column='Dongle_seriennumemr', max_length=45, blank=True, null=True)  # Field name made lowercase.(yassin)
=======
    dongle_seriennummer = models.CharField(db_column='Dongle_seriennumemr', max_length=45, blank=True, null=True)  # Field name made lowercase.
>>>>>>> f360df26dc26800a8b78f789a39cbb8d03186af4
    lizenzname = models.CharField(db_column='LizenzName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    grund_der_ablehnung = models.CharField(db_column='Grund_der_Ablehnung', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ticket'
