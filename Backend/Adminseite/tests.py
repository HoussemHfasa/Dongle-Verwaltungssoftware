from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from User_loggin.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

class CustomuserViewTests(APITestCase):

    # Test setup, creates a test user
    def setUp(self):
        self.CustomUser = CustomUser.objects.create_superuser(
            email='test@example.com',
            name='Test User',
            password='testpassword',
            role='Kunde',
            firm_code='12345',
        )

        # Create a JWT token for the test user and set the test client's credentials
        refresh = RefreshToken.for_user(self.CustomUser)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')

    # Tests listing all users
    def test_list_customusers(self):
        url = reverse('Adminseite:Adminseite')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
        self.assertEqual(response.data['data'][0]['email'], self.CustomUser.email)

    # Tests creating a new user
    def test_create_customuser(self):
        url = reverse('Adminseite:Adminseite') 
        data = {
            'is_superuser': 1,
            'email': 'new@example.com',
            'name': 'New User',
            'password': 'newpassword',
            'role': 'Kunde',
            'firm_code': '67890',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 2)
        self.assertEqual(CustomUser.objects.get(email='new@example.com').name, 'New User')

    # Tests updating an existing user
    def test_update_customuser(self):
        url = reverse('Adminseite:customuser-update-delete', args=[self.CustomUser.pk])  
        data = {
            'is_superuser': 1,
            'email': 'updated@example.com',
            'name': 'Updated User',
            'password': 'updatedpassword',
            'role': 'Kunde',
            'firm_code': '54321',
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get(pk=self.CustomUser.pk).email, 'updated@example.com')

    