# tests.py
import json
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

class UserLoginTests(APITestCase):
    def setUp(self):
        # Test-Client und Test-Benutzer erstellen
        self.client = APIClient()
        self.user = User.objects.create_user(email='test5@example.com', password='test_password', name='Test User', role='Kunde',is_superuser=False)
        self.login_url = reverse('user-login')

    def test_login_success(self):
        # Test, ob die Anmeldung erfolgreich ist
        response = self.client.post(self.login_url, {'email': 'test5@example.com', 'password': 'test_password'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@example.com')

    def test_login_failure(self):
        # Test, ob die Anmeldung bei falschem Passwort fehlschlägt
        response = self.client.post(self.login_url, {'email': 'test@example.com', 'password': 'wrong_password'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserViewSetTests(APITestCase):
    def setUp(self):
        # Test-Client und Test-Benutzer erstellen
        self.client = APIClient()
        self.admin_user = User.objects.create_user(email='admin@example.com', password='test_password', name='Admin User', role='Admin')
        self.verwalter_user = User.objects.create_user(email='verwalter@example.com', password='test_password', name='Verwalter User', role='Verwalter')
        self.kunde_user = User.objects.create_user(email='kunde@example.com', password='test_password', name='Kunde User', role='Kunde')
        self.users_url = reverse('create-user')

    def test_admin_can_view_all_users(self):
        # Test, ob ein Admin-Benutzer alle Benutzer anzeigen kann
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_verwalter_can_view_only_kunde_users(self):
        # Test, ob ein Verwalter-Benutzer nur Kunde-Benutzer anzeigen kann
        self.client.force_authenticate(user=self.verwalter_user)
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['role'], 'Kunde')

    def test_kunde_cannot_view_users(self):
        # Test, ob ein Kunde-Benutzer keine Benutzer anzeigen kann
        self.client.force_authenticate(user=self.kunde_user)
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)