from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User
from .serializers import UserSerializer

class UserAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create(
            first_name="James", last_name="Butt", company_name="Benton, John B Jr",
            age=70, city="New Orleans", state="LA", zip=70116,
            email="jbutt@gmail.com", web="http://www.bentonjohnbjr.com"
        )
        self.user2 = User.objects.create(
            first_name="Josephine", last_name="Darakjy", company_name="Chanay, Jeffrey A Esq",
            age=48, city="Brighton", state="MI", zip=48116,
            email="josephine_darakjy@darakjy.org", web="http://www.chanayjeffreyaesq.com"
        )

    def test_get_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_user(self):
        url = reverse('user-list')
        data = {
            "first_name": "John", "last_name": "Doe", "company_name": "JD Inc",
            "age": 30, "city": "Dallas", "state": "TX", "zip": 75201,
            "email": "john.doe@example.com", "web": "http://www.jdinc.com"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="john.doe@example.com").exists())

    def test_get_user_by_id(self):
        url = reverse('user-detail', args=[self.user1.id])
        response = self.client.get(url)
        user = User.objects.get(id=self.user1.id)
        serializer = UserSerializer(user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_user(self):
        url = reverse('user-detail', args=[self.user1.id])
        data = {"first_name": "JamesUpdated", "last_name": "ButtUpdated", "age": 71}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.first_name, "JamesUpdated")
        self.assertEqual(self.user1.last_name, "ButtUpdated")
        self.assertEqual(self.user1.age, 71)

    def test_delete_user(self):
        url = reverse('user-detail', args=[self.user1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(User.objects.filter(id=self.user1.id).exists())

    def test_create_user_with_existing_email(self):
        url = reverse('user-list')
        data = {
            "first_name": "Jane", "last_name": "Smith", "company_name": "JS Corp",
            "age": 40, "city": "Austin", "state": "TX", "zip": 73301,
            "email": "jbutt@gmail.com", "web": "http://www.jscorp.com"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['non_field_errors'][0], "Another user with this email already exists.")
