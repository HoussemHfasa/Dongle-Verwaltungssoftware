from django.db import models

from models import AdminVerwalter


class Dongle(models.Model):
    lfd_nr_field = models.IntegerField(db_column='Lfd. Nr.',
                                       primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. The composite primary key (Lfd. Nr., Benutzer_Firmcode) found, that is not supported. The first column is selected.
    serien_nr = models.CharField(db_column='Serien-Nr',
                                 max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    gueltig_von = models.DateField(
        db_column='Gueltig von')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gueltig_bis = models.DateField(
        db_column='Gueltig bis')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    projekt_produkt = models.CharField(db_column='Projekt/Produkt',
                                       max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    standort = models.CharField(db_column='Standort', max_length=45)  # Field name made lowercase.
    haendler = models.CharField(db_column='Haendler', max_length=45)  # Field name made lowercase.
    datum_letzte_aenderung = models.DateField(
        db_column='Datum letzte Aenderung')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    datum_erstausgabe = models.DateField(
        db_column='Datum Erstausgabe')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    benutzer_firmcode = models.IntegerField(db_column='Benutzer_Firmcode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dongle'
        unique_together = (('lfd_nr_field', 'benutzer_firmcode'),)


class Ticket(models.Model):
    id_ticket = models.IntegerField(db_column='ID_Ticket',
                                    primary_key=True)  # Field name made lowercase. The composite primary key (ID_Ticket, Admin/Verwalter_ID, Dognle_Lfd. Nr., Dognle_Benutzer_Firmcode, Benutzer_Firmcode) found, that is not supported. The first column is selected.
    titel = models.CharField(db_column='Titel', max_length=45)  # Field name made lowercase.
    beschreibung = models.CharField(db_column='Beschreibung', max_length=45)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45)  # Field name made lowercase.
    erstellungsdatum = models.DateField(db_column='Erstellungsdatum')  # Field name made lowercase.
    schliessungsdatum = models.DateField(db_column='Schliessungsdatum')  # Field name made lowercase.
    admin_verwalter = models.ForeignKey(AdminVerwalter, models.DO_NOTHING, db_column='Admin/Verwalter_ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    dognle_lfd_nr_field = models.IntegerField(
        db_column='Dognle_Lfd. Nr.')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dognle_benutzer_firmcode = models.IntegerField(db_column='Dognle_Benutzer_Firmcode')  # Field name made lowercase.
    benutzer_firmcode = models.IntegerField(db_column='Benutzer_Firmcode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ticket'
        unique_together = (
            ('id_ticket', 'admin_verwalter', 'dognle_lfd_nr_field', 'dognle_benutzer_firmcode', 'benutzer_firmcode'),)

# Create your models here.
