from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from users.models import UserDRF
from mixer.backend.django import mixer
from todo.models import Project


class TestProjectClientAPI(TestCase):
    def setUp(self) -> None:
        self.user = UserDRF.objects.create_superuser(username='admin', email='a@dmin.com', password='qwerty')
        self.projects = mixer.cycle(5).blend(Project, created_by=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    # Написать минимум один тест для API, используя APIClient.
    def test_get_list_authorized(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Данные для тестов удобно создавать, используя mixer.
    def test_get_len_of_projects(self):
        response = self.client.get('/api/projects/')
        print(response.data)
        self.assertEqual(len(response.data), 5)


# Написать минимум один тест для API, используя APITestCase.
class TestTaskApi(APITestCase):
    def setUp(self) -> None:
        self.user = UserDRF.objects.create_superuser(username='admin', email='a@dmin.com', password='qwerty')
        self.client.force_authenticate(user=self.user)

    def test_get_list_authorized(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
