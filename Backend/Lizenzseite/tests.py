from django.test import TestCase
from rest_framework.test import APIClient
from Dongle_hinzufügen.models import Dongle
from User_loggin.models import CustomUser
from .models import Lizenz

# LizenzViewTestCase ist eine Klasse, die Tests für die LizenzView-API durchführt.
class LizenzViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Testbenutzer für jede Rolle erstellen
        self.admin_user = CustomUser.objects.create_user(email='admin@example.com', password='testpassword', role='Admin', firm_code='FirmCode1')
        self.verwalter_user = CustomUser.objects.create_user(email='verwalter@example.com', password='testpassword', role='Verwalter', firm_code='FirmCode1')
        self.kunde_user = CustomUser.objects.create_user(email='kunde@example.com', password='testpassword', role='Kunde', firm_code='FirmCode1')

        # Testinstanzen für Dongle und Lizenz erstellen
        self.test_dongle = Dongle.objects.create(
            lfd_nr_field=1,
            serien_nr="12345",
            name="Test Dongle",
            gueltig_von="2023-01-01",
            gueltig_bis="2023-12-31",
            projekt_produkt="Test Project",
            kunde="Test Kunde",
            standort="Test Location",
            haendler="Test Dealer",
            datum_letzte_aenderung="2023-01-01",
            datum_erstausgabe="2023-01-01",
            firmcode="FirmCode1"
        )
        self.test_lizenz = Lizenz.objects.create(
            lfd_nr_field=1,
            firmcode="FirmCode1",
            productcode=1001,
            lizenzname="Test Lizenz",
            einheiten=10,
            gueltig_von="2023-01-01",
            gueltig_bis="2023-12-31",
            lizenzanzahl=1,
            mitarbeiter="Test Mitarbeiter",
            projekt="Test Projekt",
            kunde="Test Kunde",
            dongle_serien_nr=self.test_dongle.serien_nr
        )

    def test_lizenz_view_response(self):
        # Test als Admin-Benutzer
        self.client.login(email='admin@example.com', password='testpassword')
        response = self.client.get('/Lizenzseite/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Test als Verwalter-Benutzer
        self.client.login(email='verwalter@example.com', password='testpassword')
        response = self.client.get('/Lizenzseite/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Test als Kunde-Benutzer
        self.client.login(email='kunde@example.com', password='testpassword')
        response = self.client.get('/Lizenzseite/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()