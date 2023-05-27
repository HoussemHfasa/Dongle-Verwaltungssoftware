from django.db import models


class Dongle(models.Model):
    lfd_nr_field = models.IntegerField(db_column='Lfd. Nr.', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. The composite primary key (Lfd. Nr., Benutzer_Firmcode) found, that is not supported. The first column is selected.
    serien_nr = models.CharField(db_column='Serien-Nr', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    gueltig_von = models.DateField(db_column='Gueltig von')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gueltig_bis = models.DateField(db_column='Gueltig bis')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    projekt_produkt = models.CharField(db_column='Projekt/Produkt', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    standort = models.CharField(db_column='Standort', max_length=45)  # Field name made lowercase.
    haendler = models.CharField(db_column='Haendler', max_length=45)  # Field name made lowercase.
    datum_letzte_aenderung = models.DateField(db_column='Datum letzte Aenderung')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    datum_erstausgabe = models.DateField(db_column='Datum Erstausgabe')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    benutzer_firmcode = models.IntegerField(db_column='Benutzer_Firmcode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dongle'
        unique_together = (('lfd_nr_field', 'benutzer_firmcode'),)


class Kunde(models.Model):
    firmcode = models.IntegerField(db_column='Firmcode', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E-mail', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    passwort = models.CharField(db_column='Passwort', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kunde'


class Lizenz(models.Model):
    lfd_nr_field = models.IntegerField(db_column='Lfd. Nr.', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. The composite primary key (Lfd. Nr., Dognle_Lfd. Nr.) found, that is not supported. The first column is selected.
    productcode = models.IntegerField(db_column='ProductCode')  # Field name made lowercase.
    lizenzname = models.CharField(db_column='LizenzName', max_length=45)  # Field name made lowercase.
    einheiten = models.IntegerField(db_column='Einheiten', blank=True, null=True)  # Field name made lowercase.
    gueltig_von = models.DateField(db_column='Gueltig von')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ablaufdatum = models.DateField(db_column='Ablaufdatum')  # Field name made lowercase.
    lizenzanzahl = models.IntegerField(db_column='LizenzAnzahl')  # Field name made lowercase.
    mitarbeiter = models.CharField(db_column='Mitarbeiter', max_length=45)  # Field name made lowercase.
    projekt = models.CharField(db_column='Projekt', max_length=45)  # Field name made lowercase.
    dognle_lfd_nr_field = models.IntegerField(db_column='Dognle_Lfd. Nr.')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'lizenz'
        unique_together = (('lfd_nr_field', 'dognle_lfd_nr_field'),)

# Create your models here.
