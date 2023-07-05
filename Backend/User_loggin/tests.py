from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from User_loggin.serializers import CustomTokenObtainPairSerializer

User = get_user_model()


class ObtainAccessTokenTests(APITestCase):

    def setUp(self):
        # Testbenutzer erstellen
        self.user = User.objects.create_user(email='test@example.com', password='testpassword', name='Test User', role='Kunde')

    def test_obtain_access_token(self):
        # URL für das Abrufen des Zugriffstokens
        url = reverse('user-access-token')
        data = {'email': 'test@example.com', 'password': 'testpassword'}
        response = self.client.post(url, data)

        # Überprüfen, ob das Zugriffstoken erfolgreich abgerufen wurde
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_obtain_access_token_wrong_password(self):
        # URL für das Abrufen des Zugriffstokens
        url = reverse('user-access-token')
        data = {'email': 'test@example.com', 'password': 'wrongpassword'}
        response = self.client.post(url, data)

        # Überprüfen, ob ein falsches Passwort eine nicht autorisierte Antwort zurückgibt
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)


class AdminAccessTokenViewTests(APITestCase):

    def setUp(self):
        # Test-Admin-Benutzer erstellen
        self.user = User.objects.create_user(email='test@example.com', password='testpassword', name='Test Admin', role='Admin')
        self.token = str(CustomTokenObtainPairSerializer.get_token(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_admin_access_token(self):
        # URL für das Abrufen des Admin-Zugriffstokens
        url = reverse('admin-access-token')
        response = self.client.get(url)

        # Überprüfen, ob das Admin-Zugriffstoken erfolgreich abgerufen wurde
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)

    def test_admin_access_token_non_admin(self):
        # Testbenutzerrolle auf Nicht-Admin ändern
        self.user.role = 'Kunde'
        self.user.save()
        url = reverse('admin-access-token')
        response = self.client.get(url)

        # Überprüfen, ob ein Nicht-Admin-Benutzer eine Fehlermeldung erhält
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

