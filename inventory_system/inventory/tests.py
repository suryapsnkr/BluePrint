from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Item


class JWTAuthTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.token_url = reverse('token_obtain_pair')

    def get_jwt_token(self):
        response = self.client.post(self.token_url, {'username': 'testuser', 'password': 'password123'}, format='json')
        return response.data['access']


def test_create_item_success(self):
    token = self.get_jwt_token()
    self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    url = reverse('item-list')  # Assuming you have a router setup for 'items'
    data = {
        'name': 'New Item',
        'description': 'A description for the new item'
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Item.objects.count(), 1)
    self.assertEqual(Item.objects.get().name, 'New Item')


def test_create_item_duplicate(self):
    token = self.get_jwt_token()
    self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    Item.objects.create(name='Existing Item', description='Existing description')
    url = reverse('item-list')
    data = {
        'name': 'Existing Item',  # Duplicate name
        'description': 'Trying to create the same item again'
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


def test_get_item_success(self):
    token = self.get_jwt_token()
    self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    item = Item.objects.create(name='Item1', description='Item 1 Description')
    url = reverse('item-detail', kwargs={'pk': item.id})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['name'], 'Item1')


def test_get_item_not_found(self):
    token = self.get_jwt_token()
    self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    url = reverse('item-detail', kwargs={'pk': 999})  # Non-existent item ID
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


def test_update_item_success(self):
    token = self.get_jwt_token()
    self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    item = Item.objects.create(name='Old Item', description='Old Description')
    url = reverse('item-detail', kwargs={'pk': item.id})
    data = {
        'name': 'Updated Item',
        'description': 'Updated Description'
    }
    response = self.client.put(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    item.refresh_from_db()
    self.assertEqual(item.name, 'Updated Item')
    self.assertEqual(item.description, 'Updated Description')


def test_update_item_not_found(self):
    token = self.get_jwt_token()
    self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    url = reverse('item-detail', kwargs={'pk': 999})  # Non-existent item ID
    data = {
        'name': 'Non-existent Item',
        'description': 'This item does not exist'
    }
    response = self.client.put(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


def test_delete_item_success(self):
    token = self.get_jwt_token()
    self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    item = Item.objects.create(name='Item to delete', description='To be deleted')
    url = reverse('item-detail', kwargs={'pk': item.id})
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertFalse(Item.objects.filter(id=item.id).exists())


def test_delete_item_not_found(self):
    token = self.get_jwt_token()
    self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    url = reverse('item-detail', kwargs={'pk': 999})  # Non-existent item ID
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


def test_token_auth_success(self):
    response = self.client.post(self.token_url, {'username': 'testuser', 'password': 'password123'}, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertIn('access', response.data)


def test_token_auth_invalid_credentials(self):
    response = self.client.post(self.token_url, {'username': 'testuser', 'password': 'wrongpassword'}, format='json')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

