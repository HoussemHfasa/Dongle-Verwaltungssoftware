from django.db import models

# Benutzerdefiniertes Benutzermodell
class UserLogginCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    email = models.CharField(unique=True, max_length=254)
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10)
    firm_code = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    is_staff = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_loggin_customuser'

# Dongle-Modell
class Dongle(models.Model):
    lfd_nr_field = models.IntegerField(db_column='Lfd. Nr.', primary_key=True)
    serien_nr = models.CharField(db_column='Serien-Nr', max_length=45)
    name = models.CharField(db_column='Name', max_length=45)
    gueltig_von = models.DateField(db_column='Gueltig von')
    gueltig_bis = models.DateField(db_column='Gueltig bis')
    projekt_produkt = models.CharField(db_column='Projekt/Produkt', max_length=45)
    standort = models.CharField(db_column='Standort', max_length=45)
    haendler = models.CharField(db_column='Haendler', max_length=45)
    datum_letzte_aenderung = models.DateField(db_column='Datum letzte Aenderung')
    datum_erstausgabe = models.DateField(db_column='Datum Erstausgabe')
    benutzer_firmcode = models.CharField(db_column='Benutzer_Firmcode', max_length=45)

    class Meta:
        managed = False
        db_table = 'dongle'

# Lizenz-Modell
class Lizenz(models.Model):
    lfd_nr_field = models.IntegerField(db_column='Lfd. Nr.', primary_key=True)
    productcode = models.IntegerField(db_column='ProductCode')
    lizenzname = models.CharField(db_column='LizenzName', max_length=45)
    einheiten = models.IntegerField(db_column='Einheiten', blank=True, null=True)
    gueltig_von = models.DateField(db_column='Gueltig von')
    ablaufdatum = models.DateField(db_column='Ablaufdatum')
    lizenzanzahl = models.IntegerField(db_column='LizenzAnzahl')
    mitarbeiter = models.CharField(db_column='Mitarbeiter', max_length=45)
    projekt = models.CharField(db_column='Projekt', max_length=45)
    dongle_lfd_nr_field = models.ForeignKey(Dongle, models.DO_NOTHING, db_column='dongle_Lfd. Nr.')

    class Meta:
        managed = False
        db_table = 'lizenz'