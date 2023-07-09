from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Dongle
from User_loggin.models import CustomUser
from .serializers import DongleSerializer

# Testfälle für das Dongle-Modell
class DongleTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a test user
        self.test_user = CustomUser.objects.create(
            email="test@example.com",
            name="Test User",
            password="test_password",
            role="test_role",
            firm_code="test_firm_code"
        )

        self.valid_dongle_data = {
            "serien_nr": "12345",
            "name": "Test Dongle",
            "gueltig_von": "2023-01-01",
            "gueltig_bis": "2023-12-31",
            "projekt_produkt": "Test Product",
            "standort": "Test Location",
            "haendler": "Test Dealer",
            "datum_letzte_aenderung": "2023-01-01",
            "datum_erstausgabe": "2023-01-01",
            "firmcode": self.test_user.firm_code
        }

    def test_create_dongle(self):
        response = self.client.post(reverse('dongle-create'), data=self.valid_dongle_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dongle.objects.count(), 1)
        self.assertEqual(Dongle.objects.get().serien_nr, self.valid_dongle_data["serien_nr"])

    def test_create_dongle_missing_data(self):
        invalid_dongle_data = self.valid_dongle_data.copy()
        del invalid_dongle_data["serien_nr"]

        response = self.client.post(reverse('dongle-create'), data=invalid_dongle_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Dongle.objects.count(), 0)

    def test_serializer_validation(self):
        serializer = DongleSerializer(data=self.valid_dongle_data)
        self.assertTrue(serializer.is_valid())

        invalid_dongle_data = self.valid_dongle_data.copy()
        del invalid_dongle_data["serien_nr"]

        serializer = DongleSerializer(data=invalid_dongle_data)
        self.assertFalse(serializer.is_valid())