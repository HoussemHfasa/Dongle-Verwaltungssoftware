# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserLogginCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    id_ticket = models.IntegerField(db_column='ID_Ticket', primary_key=True)  # Field name made lowercase.
    titel = models.CharField(db_column='Titel', max_length=45)  # Field name made lowercase.
    beschreibung = models.CharField(db_column='Beschreibung', max_length=255)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45)  # Field name made lowercase.
    erstellungsdatum = models.DateField(db_column='Erstellungsdatum')  # Field name made lowercase.
    schliessungsdatum = models.DateField(db_column='Schliessungsdatum', blank=True, null=True)  # Field name made lowercase.
    dongle_lizenz = models.IntegerField(db_column='Dongle/Lizenz', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dongle_name = models.CharField(db_column='Dongle_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dongle_seriennummer = models.CharField(db_column='Dongle_seriennummer', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lizenzname = models.CharField(db_column='LizenzName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    firmcode = models.CharField(db_column='Firmcode', max_length=45)  # Field name made lowercase.
    gueltig_von = models.DateField(db_column='Gueltig von', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gueltig_bis = models.DateField(db_column='Gueltig bis', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    einheiten = models.IntegerField(db_column='Einheiten', blank=True, null=True)  # Field name made lowercase.
    projekt = models.CharField(db_column='Projekt', max_length=45, blank=True, null=True)  # Field name made lowercase.
    grund_der_ablehnung = models.CharField(db_column='Grund_der_Ablehnung', max_length=45, blank=True, null=True)  # Field name made lowercase.
    admin_verwalter_email = models.CharField(db_column='Admin/Verwalter_Email', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    haendler = models.CharField(db_column='Haendler', max_length=45, blank=True, null=True)  # Field name made lowercase.
    standort = models.CharField(db_column='Standort', max_length=45, blank=True, null=True)  # Field name made lowercase.
    productcode = models.IntegerField(db_column='Productcode', blank=True, null=True)  # Field name made lowercase.
    lizenzanzahl = models.IntegerField(db_column='Lizenzanzahl', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ticket'


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


class UserLogginCustomuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(UserLogginCustomuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_loggin_customuser_groups'
        unique_together = (('customuser', 'group'),)


class UserLogginCustomuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(UserLogginCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_loggin_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)
