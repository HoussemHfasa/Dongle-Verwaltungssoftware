# Generated by Django 4.2.1 on 2023-07-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id_ticket', models.IntegerField(db_column='ID_Ticket', primary_key=True, serialize=False)),
                ('titel', models.CharField(db_column='Titel', max_length=45)),
                ('beschreibung', models.CharField(db_column='Beschreibung', max_length=255)),
                ('status', models.CharField(db_column='Status', max_length=45)),
                ('erstellungsdatum', models.DateField(db_column='Erstellungsdatum')),
                ('schliessungsdatum', models.DateField(blank=True, db_column='Schliessungsdatum', null=True)),
                ('dongle_lizenz', models.IntegerField(blank=True, db_column='Dongle/Lizenz', null=True)),
                ('dongle_name', models.CharField(blank=True, db_column='Dongle_Name', max_length=45, null=True)),
                ('dongle_seriennummer', models.CharField(blank=True, db_column='Dongle_seriennummer', max_length=45, null=True)),
                ('lizenzname', models.CharField(blank=True, db_column='LizenzName', max_length=45, null=True)),
                ('firmcode', models.CharField(db_column='Firmcode', max_length=45)),
                ('gueltig_von', models.DateField(blank=True, db_column='Gueltig von', null=True)),
                ('gueltig_bis', models.DateField(blank=True, db_column='Gueltig bis', null=True)),
                ('einheiten', models.IntegerField(blank=True, db_column='Einheiten', null=True)),
                ('projekt', models.CharField(blank=True, db_column='Projekt', max_length=45, null=True)),
                ('grund_der_ablehnung', models.CharField(blank=True, db_column='Grund_der_Ablehnung', max_length=45, null=True)),
                ('admin_verwalter_email', models.CharField(blank=True, db_column='Admin/Verwalter_Email', max_length=45, null=True)),
                ('haendler', models.CharField(blank=True, db_column='Haendler', max_length=45, null=True)),
                ('standort', models.CharField(blank=True, db_column='Standort', max_length=45, null=True)),
                ('productcode', models.IntegerField(blank=True, db_column='Productcode', null=True)),
                ('lizenzanzahl', models.IntegerField(blank=True, db_column='Lizenzanzahl', null=True)),
            ],
            options={
                'db_table': 'ticket',
            },
        ),
    ]
