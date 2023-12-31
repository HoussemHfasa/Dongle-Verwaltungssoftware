# Generated by Django 4.2.1 on 2023-05-28 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dongle',
            fields=[
                ('lfd_nr_field', models.IntegerField(db_column='Lfd. Nr.', primary_key=True, serialize=False)),
                ('serien_nr', models.CharField(db_column='Serien-Nr', max_length=45)),
                ('name', models.CharField(db_column='Name', max_length=45)),
                ('gueltig_von', models.DateField(db_column='Gueltig von')),
                ('gueltig_bis', models.DateField(db_column='Gueltig bis')),
                ('projekt_produkt', models.CharField(db_column='Projekt/Produkt', max_length=45)),
                ('standort', models.CharField(db_column='Standort', max_length=45)),
                ('haendler', models.CharField(db_column='Haendler', max_length=45)),
                ('datum_letzte_aenderung', models.DateField(db_column='Datum letzte Aenderung')),
                ('datum_erstausgabe', models.DateField(db_column='Datum Erstausgabe')),
                ('benutzer_firmcode', models.IntegerField(db_column='Benutzer_Firmcode')),
            ],
            options={
                'db_table': 'dongle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kunde',
            fields=[
                ('firmcode', models.IntegerField(db_column='Firmcode', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=45)),
                ('e_mail', models.CharField(db_column='E-mail', max_length=45)),
                ('passwort', models.CharField(db_column='Passwort', max_length=45)),
            ],
            options={
                'db_table': 'kunde',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lizenz',
            fields=[
                ('lfd_nr_field', models.IntegerField(db_column='Lfd. Nr.', primary_key=True, serialize=False)),
                ('productcode', models.IntegerField(db_column='ProductCode')),
                ('lizenzname', models.CharField(db_column='LizenzName', max_length=45)),
                ('einheiten', models.IntegerField(blank=True, db_column='Einheiten', null=True)),
                ('gueltig_von', models.DateField(db_column='Gueltig von')),
                ('ablaufdatum', models.DateField(db_column='Ablaufdatum')),
                ('lizenzanzahl', models.IntegerField(db_column='LizenzAnzahl')),
                ('mitarbeiter', models.CharField(db_column='Mitarbeiter', max_length=45)),
                ('projekt', models.CharField(db_column='Projekt', max_length=45)),
                ('dognle_lfd_nr_field', models.IntegerField(db_column='Dognle_Lfd. Nr.')),
            ],
            options={
                'db_table': 'lizenz',
                'managed': False,
            },
        ),
    ]
