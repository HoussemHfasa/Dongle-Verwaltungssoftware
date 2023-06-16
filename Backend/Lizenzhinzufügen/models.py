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


class UserLogginCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    email = models.CharField(unique=True, max_length=254)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10)
    firm_code = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_loggin_customuser'

class Dongle(models.Model):
    lfd_nr_field = models.IntegerField(db_column='Lfd. Nr.', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    serien_nr = models.CharField(db_column='Serien-Nr', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    gueltig_von = models.DateField(db_column='Gueltig von', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gueltig_bis = models.DateField(db_column='Gueltig bis', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    projekt_produkt = models.CharField(db_column='Projekt/Produkt', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kunde = models.CharField(db_column='Kunde', max_length=45)  # Field name made lowercase.
    standort = models.CharField(db_column='Standort', max_length=45)  # Field name made lowercase.
    haendler = models.CharField(db_column='Haendler', max_length=45, blank=True, null=True)  # Field name made lowercase.
    datum_letzte_aenderung = models.DateField(db_column='Datum letzte Aenderung')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    datum_erstausgabe = models.DateField(db_column='Datum Erstausgabe')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    firmcode = models.CharField(db_column='Firmcode', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dongle'
