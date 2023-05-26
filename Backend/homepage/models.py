from django.db import models


class Dongle(models.Model):
    lfd_nr_field = models.IntegerField(db_column='Lfd. Nr.', primary_key=True)
    serien_nr = models.CharField(db_column='Serien-Nr', max_length=45)
    name = models.CharField(db_column='Name', max_length=45)
    
    benutzer_firmcode = models.IntegerField(db_column='Benutzer_Firmcode')

    class Meta:
        managed = False
        db_table = 'dongle'
        unique_together = (('lfd_nr_field', 'benutzer_firmcode'),)
        