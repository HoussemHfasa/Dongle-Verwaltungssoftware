from django.db import models


class Dongle(models.Model):
    lfd_nr_field = models.IntegerField(db_column='Lfd. Nr.', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. The composite primary key (Lfd. Nr., Benutzer_Firmcode) found, that is not supported. The first column is selected.
    serien_nr = models.CharField(db_column='Serien-Nr', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    
    benutzer_firmcode = models.IntegerField(db_column='Benutzer_Firmcode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dongle'
        unique_together = (('lfd_nr_field', 'benutzer_firmcode'),)
        