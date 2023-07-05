from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Customuser

class CustomUserAPITests(TestCase):
    def setUp(self):
        self.superuser = Customuser.objects.create_superuser(
            email='superuser@example.com',
            password='testpassword',
            name='Superuser',
            role='Admin',
            firm_code='1234'
        )

        self.admin = Customuser.objects.create_user(
            email='admin@example.com',
            password='testpassword',
            name='Admin',
            role='Admin',
            firm_code='1234'
        )

    def test_create_customuser(self):
        self.client.login(email='superuser@example.com', password='testpassword')

        response = self.client.post(reverse('adminseite-list'), {
            'email': 'newuser@example.com',
            'password': 'testpassword',
            'name': 'New User',
            'role': 'Admin',
            'firm_code': '1234',
            'is_superuser': 0
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customuser.objects.count(), 3)

# Add more test cases for other functionality as needed