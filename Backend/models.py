# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminVerwalter(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E-mail', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    passwort = models.CharField(db_column='Passwort', max_length=45)  # Field name made lowercase.
    rolle = models.CharField(db_column='Rolle', max_length=9)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin_verwalter'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
    lfd_nr_field = models.IntegerField(db_column='Lfd. Nr.', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. The composite primary key (Lfd. Nr., Benutzer_Firmcode) found, that is not supported. The first column is selected.
    serien_nr = models.CharField(db_column='Serien-Nr', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    g³ltig_von = models.DateField(db_column='G³ltig von')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g³ltig_bis = models.DateField(db_column='G³ltig bis')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    projekt_produkt = models.CharField(db_column='Projekt/Produkt', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    standort = models.CharField(db_column='Standort', max_length=45)  # Field name made lowercase.
    hõndler = models.CharField(db_column='Hõndler', max_length=45)  # Field name made lowercase.
    datum_letzte_õnderung = models.DateField(db_column='Datum letzte ─nderung')  # Field name made lowercase. Field renamed to remove unsuitable characters.
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
    g³ltig_von = models.DateField(db_column='G³ltig von')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ablaufdatum = models.DateField(db_column='Ablaufdatum')  # Field name made lowercase.
    lizenzanzahl = models.IntegerField(db_column='LizenzAnzahl')  # Field name made lowercase.
    mitarbeiter = models.CharField(db_column='Mitarbeiter', max_length=45)  # Field name made lowercase.
    projekt = models.CharField(db_column='Projekt', max_length=45)  # Field name made lowercase.
    dognle_lfd_nr_field = models.IntegerField(db_column='Dognle_Lfd. Nr.')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'lizenz'
        unique_together = (('lfd_nr_field', 'dognle_lfd_nr_field'),)


class Ticket(models.Model):
    id_ticket = models.IntegerField(db_column='ID_Ticket', primary_key=True)  # Field name made lowercase. The composite primary key (ID_Ticket, Admin/Verwalter_ID, Dognle_Lfd. Nr., Dognle_Benutzer_Firmcode, Benutzer_Firmcode) found, that is not supported. The first column is selected.
    titel = models.CharField(db_column='Titel', max_length=45)  # Field name made lowercase.
    beschreibung = models.CharField(db_column='Beschreibung', max_length=45)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45)  # Field name made lowercase.
    erstellungsdatum = models.DateField(db_column='Erstellungsdatum')  # Field name made lowercase.
    schlie▀ungsdatum = models.DateField(db_column='Schlie▀ungsdatum')  # Field name made lowercase.
    admin_verwalter = models.ForeignKey(AdminVerwalter, models.DO_NOTHING, db_column='Admin/Verwalter_ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dognle_lfd_nr_field = models.IntegerField(db_column='Dognle_Lfd. Nr.')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dognle_benutzer_firmcode = models.IntegerField(db_column='Dognle_Benutzer_Firmcode')  # Field name made lowercase.
    benutzer_firmcode = models.IntegerField(db_column='Benutzer_Firmcode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ticket'
        unique_together = (('id_ticket', 'admin_verwalter', 'dognle_lfd_nr_field', 'dognle_benutzer_firmcode', 'benutzer_firmcode'),)


class UserLogginAdminverwalter(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    email = models.CharField(unique=True, max_length=254)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10)
    is_admin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_loggin_adminverwalter'


class UserLogginAdminverwalterGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    adminverwalter = models.ForeignKey(UserLogginAdminverwalter, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_loggin_adminverwalter_groups'
        unique_together = (('adminverwalter', 'group'),)


class UserLogginAdminverwalterUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    adminverwalter = models.ForeignKey(UserLogginAdminverwalter, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_loggin_adminverwalter_user_permissions'
        unique_together = (('adminverwalter', 'permission'),)


class UserLogginKunde(models.Model):
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    firmcode = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=254)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_loggin_kunde'


class UserLogginKundeGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    kunde = models.ForeignKey(UserLogginKunde, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_loggin_kunde_groups'
        unique_together = (('kunde', 'group'),)


class UserLogginKundeUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    kunde = models.ForeignKey(UserLogginKunde, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_loggin_kunde_user_permissions'
        unique_together = (('kunde', 'permission'),)


class UsersAdminVerwalter(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    email = models.CharField(unique=True, max_length=254)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'users_admin_verwalter'


class UsersAdminVerwalterGroups(models.Model):
    admin_verwalter = models.ForeignKey(UsersAdminVerwalter, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_admin_verwalter_groups'
        unique_together = (('admin_verwalter', 'group'),)


class UsersAdminVerwalterUserPermissions(models.Model):
    admin_verwalter = models.ForeignKey(UsersAdminVerwalter, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_admin_verwalter_user_permissions'
        unique_together = (('admin_verwalter', 'permission'),)


class UsersKunde(models.Model):
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    firmcode = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=254)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users_kunde'


class UsersKundeGroups(models.Model):
    kunde = models.ForeignKey(UsersKunde, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_kunde_groups'
        unique_together = (('kunde', 'group'),)


class UsersKundeUserPermissions(models.Model):
    kunde = models.ForeignKey(UsersKunde, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_kunde_user_permissions'
        unique_together = (('kunde', 'permission'),)
