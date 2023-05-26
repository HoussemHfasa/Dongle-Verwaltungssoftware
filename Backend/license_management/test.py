from django.test import TestCase
from unittest.mock import patch
from datetime import datetime, timedelta
from models import Kunde, Lizenz
from license_management.views import check_license_expiry


class LicenseExpiryTest(TestCase):
    def setUp(self):
        user1 = Kunde.objects.create(name="Max Mustermann", e_mail="max@muster.de", firmcode="1234")
        user2 = Kunde.objects.create(name="Anna Schmidt", e_mail="anna@schmidt.de", firmcode="5678")
        user3 = Kunde.objects.create(name="Hans Müller", firmcode="9101")
        Lizenz.objects.create(dognle_lfd_nr_field=user1, ablaufdatum=datetime.now().date() + timedelta(days=3))
        Lizenz.objects.create(dognle_lfd_nr_field=user2, ablaufdatum=datetime.now().date() + timedelta(days=2))
        Lizenz.objects.create(dognle_lfd_nr_field=user3, ablaufdatum=datetime.now().date() + timedelta(days=4))

    def test_license_expiry(self):
        with patch('license_management.views.send_mail') as mock_send_mail:
            # Call the check_license_expiry function
            check_license_expiry()
            # Assert that the mock_send_mail function was called twice with the correct arguments
            mock_send_mail.assert_called_with(
                'Ihre Lizenz läuftbald ab',
                'Hallo Max Mustermann, Ihre Lizenz läuft in drei Tagen ab. Bitte verlängern Sie Ihre Lizenz, '
                'um weiterhin das Produkt nutzen zu können.',
                'noreply@example.com',
                ['max@muster.de']
            )
            mock_send_mail.assert_called_with(
                'Ihre Lizenz läuft bald ab',
                'Hallo Anna Schmidt, Ihre Lizenz läuft in zwei Tagen ab. Bitte verlängern Sie Ihre Lizenz, '
                'um weiterhin das Produkt nutzen zu können.',
                'noreply@example.com',
                ['anna@schmidt.de']
            )
            # Assert that the mock_send_mail function was called only twice
            self.assertEqual(mock_send_mail.call_count, 2)
