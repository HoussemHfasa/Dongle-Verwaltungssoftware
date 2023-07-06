from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from User_loggin.models import CustomUser
from Adminseite.serializers import CustomuserSerializer

class CustomuserViewTests(APITestCase):

    def setUp(self):
        self.CustomUser = CustomUser.objects.create(
            is_superuser=1,
            email='test@example.com',
            name='Test User',
            password='testpassword',
            role='Kunde',
            firm_code='12345',
        )

    def test_list_customusers(self):
        url = reverse('Adminseite:Adminseite')  
        response = self.client.get(url)

        # Check if the response status is OK and contains the created user
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
        self.assertEqual(response.data['data'][0]['email'], self.CustomUser.email)

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

        # Check if the response status is created and the new user exists
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 2)
        self.assertEqual(CustomUser.objects.get(email='new@example.com').name, 'New User')

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

        # Check if the response status is OK and the user is updated
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get(pk=self.CustomUser.pk).email, 'updated@example.com')

    def test_delete_customuser(self):
        url = reverse('Adminseite:delete-row', args=[self.CustomUser.pk])  
        response = self.client.delete(url)

        # Check if the response status is BAD_REQUEST because the user is a superuser
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 1)

        # Change superuser status and delete again
        self.CustomUser.is_superuser = 0
        self.CustomUser.save()
        response = self.client.delete(url)

        # Check if the response status is NO_CONTENT and the user is deleted
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CustomUser.objects.count(), 0)