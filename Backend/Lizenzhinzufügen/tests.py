from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from Lizenzhinzufügen.models import Lizenz
from User_loggin.models import CustomUser
from unittest.mock import patch
from Dongle_hinzufügen.models import Dongle

class LizenzCreateViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('license-create')  # Replace 'lizenz-create' with the name of the URL in your urls.py

        # Create a sample CustomUser
        self.user = CustomUser.objects.create(
            email='user@example.com',
            name='Test User',
            firm_code='test_firm'
        )

        # Create a sample Dongle
        self.dongle = Dongle.objects.create(
            lfd_nr_field=99,
            serien_nr='12345',
            name='Test Dongle',
            gueltig_von='2021-01-01',
            gueltig_bis='2022-01-01',
            projekt_produkt='Test Project',
            kunde='Test Customer',
            standort='Test Location',
            haendler='Test Dealer',
            datum_letzte_aenderung='2021-01-01',
            datum_erstausgabe='2021-01-01',
            firmcode='test_firm'
        )

        self.valid_data = {
            'lizenzname': 'Test Lizenz',
            'gueltig_von': '2021-01-01',
            'gueltig_bis': '2022-01-01',
            'projekt': 'Test Projekt',
            'einheiten': 10,
            'productcode': 516,
            'mitarbeiter': 'Test Mitarbeiter',
            'firmcode': 'test_firm',
            'lizenzanzahl': 5,
            'dongle_serien_nr': '12345'
        }

    @patch('Lizenzhinzufügen.views.send_mail') 
    def test_create_lizenz_success(self, mock_send_mail):
        response = self.client.post(self.url, self.valid_data, format='json')

        # Check if the license was created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lizenz.objects.count(), 1)
        self.assertEqual(Lizenz.objects.get().lizenzname, 'Test Lizenz')

        # Check if an email was sent
        mock_send_mail.assert_called_once()