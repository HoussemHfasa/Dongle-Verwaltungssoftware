from datetime import timedelta, date

from django.core import mail
from django.test import TestCase

from Dongle_hinzufügen.models import Dongle
from Lizenzhinzufügen.models import Lizenz
from license_management.views import check_license_expiry, send_expiry_notification


class CheckLicenseExpiryTest(TestCase):
    def test_check_license_expiry(self):
        Lizenz.objects.create(
            lfd_nr_field=1,
            productcode=1,
            lizenzname='Testlizenz',
            einheiten=1,
            gueltig_von=date.today() - timedelta(days=30),
            ablaufdatum=date.today() + timedelta(days=3),
            dognle_lfd_nr_field=Dongle.objects.create(
                lfd_nr_field=1,
                serien_nr='12345',
                name='Testdongle',
                gueltig_von=date.today() - timedelta(days=30),
                gueltig_bis=date.today() + timedelta(days=30),
                projekt_produkt='Testprojekt',
                standort='Teststandort',
                haendler='Testhaendler',
                datum_letzte_änderung=date.today(),
                datum_erstausgabe=date.today() - timedelta(days=30),
                benutzer_firmcode=1
            ))
        users = check_license_expiry()
        self.assertEqual(len(users), 1)


class SendExpiryNotificationTest(TestCase):
    def test_send_expiry_notification(self):
        user = {'name': 'Testuser', 'email': 'ramaabazeed654@gmail.com'}

        send_expiry_notification(user)

        self.assertEqual(len(mail.outbox), 1)

        self.assertEqual(mail.outbox[0].subject, 'Ihre Lizenz läuft bald ab')
        self.assertEqual(mail.outbox[0].to, ['ramaabazeed654@gmail.com'])

