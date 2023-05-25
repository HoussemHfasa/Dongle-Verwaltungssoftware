



from django.db import models


class Kunde(models.Model):
    firmcode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    passwort = models.CharField(max_length=45)

    class Meta:
        db_table = 'kunde'


class Dongle(models.Model):
    lfd_nr = models.IntegerField()
    serien_nr = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    gueltig_von = models.DateField()
    gueltig_bis = models.DateField()
    projekt_produkt = models.CharField(max_length=45)
    standort = models.CharField(max_length=45)
    haendler = models.CharField(max_length=45)
    datum_letzte_aenderung = models.DateField()
    datum_erstausgabe = models.DateField()
    benutzer_firmcode = models.IntegerField()

    class Meta:
        db_table = 'dongle'
        unique_together = (('lfd_nr', 'benutzer_firmcode'),)


class Lizenz(models.Model):
    lfd_nr = models.IntegerField()
    productcode = models.IntegerField()
    lizenzname = models.CharField(max_length=45)
    einheiten = models.IntegerField(null=True, blank=True)
    gueltig_von = models.DateField()
    ablaufdatum = models.DateField()
    lizenzanzahl = models.IntegerField()
    mitarbeiter = models.CharField(max_length=45)
    projekt = models.CharField(max_length=45)
    dongle_lfd_nr = models.IntegerField()

    class Meta:
        db_table = 'lizenz'
        unique_together = (('lfd_nr', 'dongle_lfd_nr'),)

    def __str__(self):
        return f'{self.lizenzname} ({self.lfd_nr})'
