# Generated by Django 4.2.1 on 2023-05-25 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kunde',
            fields=[
                ('firmcode', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('passwort', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'kunde',
            },
        ),
        migrations.CreateModel(
            name='Lizenz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lfd_nr', models.IntegerField()),
                ('productcode', models.IntegerField()),
                ('lizenzname', models.CharField(max_length=45)),
                ('einheiten', models.IntegerField(blank=True, null=True)),
                ('gueltig_von', models.DateField()),
                ('ablaufdatum', models.DateField()),
                ('lizenzanzahl', models.IntegerField()),
                ('mitarbeiter', models.CharField(max_length=45)),
                ('projekt', models.CharField(max_length=45)),
                ('dongle_lfd_nr', models.IntegerField()),
            ],
            options={
                'db_table': 'lizenz',
                'unique_together': {('lfd_nr', 'dongle_lfd_nr')},
            },
        ),
        migrations.CreateModel(
            name='Dongle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lfd_nr', models.IntegerField()),
                ('serien_nr', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('gueltig_von', models.DateField()),
                ('gueltig_bis', models.DateField()),
                ('projekt_produkt', models.CharField(max_length=45)),
                ('standort', models.CharField(max_length=45)),
                ('haendler', models.CharField(max_length=45)),
                ('datum_letzte_aenderung', models.DateField()),
                ('datum_erstausgabe', models.DateField()),
                ('benutzer_firmcode', models.IntegerField()),
            ],
            options={
                'db_table': 'dongle',
                'unique_together': {('lfd_nr', 'benutzer_firmcode')},
            },
        ),
    ]