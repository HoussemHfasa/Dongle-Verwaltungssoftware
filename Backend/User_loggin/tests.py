# User_loggin/tests.py
# Nutzermodell importieren 
from django.contrib.auth import get_user_model  

# Status codes importieren 
from rest_framework import status

# Test Case importieren 
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

# Eigene Models und Views importieren
from . import serializers  
from . import views

# Nutzermodell definieren
User = get_user_model()

# Testfall-Klasse 
class CustomUserTestCase(APITestCase):
    # Setup-Methode
    def setUp(self):
        # Admin-Nutzer erstellen 
        self.admin_user = User.objects.create_user(email='admin@example.com', password='testpassword', name='Admin User', role='Admin')
        # APIRequestFactory zum Erstellen von Requests 
        self.factory = APIRequestFactory()

    # Test des Nutzer Serializers 
    def test_user_serializer(self):
     serializer = serializers.UserSerializer(instance=self.admin_user)
     print("Serialisierte Daten:", serializer.data)
     self.assertEqual(serializer.data, {
        'id': self.admin_user.id,
        'email': 'admin@example.com',
        'name': 'Admin User',
        'role': 'Admin',
        'firm_code': None,
    })

    # Test zum Erstellen eines Nutzers 
    def test_create_user(self):
     request = self.factory.post('/users/', {
        'email': 'newuser@example.com',
        'name': 'New User',
        'role': 'Verwalter',
        'password': 'testpassword',
    })
     # Admin-Nutzer authentifizieren
     force_authenticate(request, user=self.admin_user)
     view = views.UserListView.as_view()
     response = view(request)
     print("Statuscode der Antwort:", response.status_code)
     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
 
     # Erstellten Nutzer abrufen 
     created_user = User.objects.filter(email='newuser@example.com').first()
     print("Erstellter Nutzer:", created_user)
     self.assertIsNotNone(created_user)
     self.assertEqual(created_user.name, 'New User')
     self.assertEqual(created_user.role, 'Verwalter')

    # Test zum Erstellen eines Kunden-Nutzers mit Firmencode
    def test_create_kunde_user_with_firm_code(self):
        ...