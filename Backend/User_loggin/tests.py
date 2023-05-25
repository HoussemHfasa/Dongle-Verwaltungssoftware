from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import AdminVerwalter, Kunde
from django.db import IntegrityError 


class UserLoginTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = AdminVerwalter.objects.create(email="admin1@example.com", name="Admin User1", role="Admin", password="admin123")
        self.admin.set_password("admin123")
        self.admin.save()

        self.admin = AdminVerwalter.objects.create(email="Verwalter@example.com", name="Verwalter User", role="Verwalter", password="admin123")
        self.admin.set_password("admin123")
        self.admin.save()

        self.admin = AdminVerwalter.objects.create(email="admin11@example.com", name="Admin User11", role="Admin", password="admin123")
        self.admin.set_password("admin123")
        self.admin.save()
        
        self.kunde = Kunde.objects.create(email="kunde1@example.com", name="Kunde User", firmcode="kunde123", password="kunde123")
        self.kunde.set_password("kunde123")
        self.kunde.save()
        
    def test_admin_login(self):
        response = self.client.post(reverse('user_role'), {'email': 'admin1@example.com', 'password': 'admin123'})
        self.assertEqual(response.status_code, 200)
        print("Roleadmin: ", response.data['role'])
        self.assertEqual(response.data['email'], 'admin1@example.com')
        self.assertIn(response.data['role'], ['Admin', 'Verwalter'])

    def test_admin1_login(self):
        response = self.client.post(reverse('user_role'), {'email': 'admin11@example.com', 'password': 'admin123'})
        self.assertEqual(response.status_code, 200)
        print("Roleadmin2: ", response.data['role'])
        self.assertEqual(response.data['email'], 'admin11@example.com')
        self.assertIn(response.data['role'], ['Admin', 'Verwalter'])

    def test_Verwalter_login(self):
        response = self.client.post(reverse('user_role'), {'email': 'Verwalter@example.com', 'password': 'admin123'})
        self.assertEqual(response.status_code, 200)
        print("Roleverwalter:", response.data['role'])
        self.assertEqual(response.data['email'], 'Verwalter@example.com')
        self.assertIn(response.data['role'], ['Admin', 'Verwalter'])
    def test_kunde_login(self):
        response = self.client.post(reverse('user_role'), {'email': 'kunde1@example.com', 'password': 'kunde1234'})
       
        self.assertEqual(response.status_code, 404)
        print("Rolekunde:", response.data['role'])
        self.assertEqual(response.data['email'], 'kunde1@example.com')
        self.assertEqual(response.data['role'], 'Kunde')

    def test_invalid_login(self):
        response = self.client.post(reverse('user_role'), {'email': 'invalid@example.com', 'password': 'invalid123'})
        self.assertEqual(response.status_code, 404)