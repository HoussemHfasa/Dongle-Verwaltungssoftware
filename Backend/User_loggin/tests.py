from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from . import models
from . import serializers
from . import views

User = get_user_model()

class CustomUserTestCase(APITestCase):

    def setUp(self):
        self.admin_user = User.objects.create_user(email='admin@example.com', password='testpassword', name='Admin User', role='Admin')
        self.factory = APIRequestFactory()

    def test_user_serializer(self):
     serializer = serializers.UserSerializer(instance=self.admin_user)
     print("Serialized data:", serializer.data)
     self.assertEqual(serializer.data, {
        'id': self.admin_user.id,
        'email': 'admin@example.com',
        'name': 'Admin User',
        'role': 'Admin',
        'firm_code': None,
    })

    def test_create_user(self):
     request = self.factory.post('/users/', {
        'email': 'newuser@example.com',
        'name': 'New User',
        'role': 'Verwalter',
        'password': 'testpassword',
    })
     force_authenticate(request, user=self.admin_user)
     view = views.UserListView.as_view()
     response = view(request)
     print("Response status code:", response.status_code)
     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
 
     created_user = User.objects.filter(email='newuser@example.com').first()
     print("Created user:", created_user)
     self.assertIsNotNone(created_user)
     self.assertEqual(created_user.name, 'New User')
     self.assertEqual(created_user.role, 'Verwalter')

     print("Created user name:", created_user.name)
     print("Created user role:", created_user.role)

    def test_create_kunde_user_with_firm_code(self):
        request = self.factory.post('/users/', {
            'email': 'kundeuser@example.com',
            'name': 'Kunde User',
            'role': 'Kunde',
            'password': 'testpassword',
            'firm_code': 'FIRM123',
        })
        force_authenticate(request, user=self.admin_user)
        view = views.UserListView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_user = User.objects.filter(email='kundeuser@example.com').first()
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.name, 'Kunde User')
        self.assertEqual(created_user.role, 'Kunde')
        self.assertEqual(created_user.firm_code, 'FIRM123')