from models import models


class Dongle(models.Model):
    lfd_nr_field = models.IntegerField(db_column='Lfd. Nr.',
                                       primary_key=True)
    serien_nr = models.CharField(db_column='Serien-Nr',
                                 max_length=45)
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    gültig_von = models.DateField(
        db_column='Gültig von')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gültig_bis = models.DateField(
        db_column='Gültig bis')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    projekt_produkt = models.CharField(db_column='Projekt/Produkt',
                                       max_length=45)
    standort = models.CharField(db_column='Standort', max_length=45)
    händler = models.CharField(db_column='Händler', max_length=45)
    datum_letzteänderung = models.DateField(
        db_column='Datum letzteänderung')
    datum_erstausgabe = models.DateField(
        db_column='Datum Erstausgabe')
    benutzer_firmcode = models.IntegerField(db_column='Benutzer_Firmcode')

    class Meta:
        managed = False
        db_table = 'dongle'
        unique_together = (('lfd_nr_field', 'benutzer_firmcode'),)


class Kunde(models.Model):
    firmcode = models.IntegerField(db_column='Firmcode', primary_key=True)
    name = models.CharField(db_column='Name', max_length=45)
    e_mail = models.CharField(db_column='E-mail',
                              max_length=45)
    passwort = models.CharField(db_column='Passwort', max_length=45)

    class Meta:
        managed = False
        db_table = 'kunde'


class Lizenz(models.Model):
    lfd_nr_field = models.IntegerField(db_column='Lfd. Nr.',
                                       primary_key=True)
    productcode = models.IntegerField(db_column='ProductCode')  # Field name made lowercase.
    lizenzname = models.CharField(db_column='LizenzName', max_length=45)  # Field name made lowercase.
    einheiten = models.IntegerField(db_column='Einheiten', blank=True, null=True)  # Field name made lowercase.
    gültig_von = models.DateField(
        db_column='G³ltig von')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ablaufdatum = models.DateField(db_column='Ablaufdatum')  # Field name made lowercase.
    lizenzanzahl = models.IntegerField(db_column='LizenzAnzahl')  # Field name made lowercase.
    mitarbeiter = models.CharField(db_column='Mitarbeiter', max_length=45)  # Field name made lowercase.
    projekt = models.CharField(db_column='Projekt', max_length=45)  # Field name made lowercase.
    dognle_lfd_nr_field = models.IntegerField(
        db_column='Dognle_Lfd. Nr.')

    class Meta:
        managed = False
        db_table = 'lizenz'
        unique_together = (('lfd_nr_field', 'dognle_lfd_nr_field'),)
