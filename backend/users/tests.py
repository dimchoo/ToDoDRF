from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from users.views import UserViewSet


class TestUserAPI(TestCase):
    # Написать минимум один тест для API, используя APIRequestFactory.
    def test_get_list_unauthorized(self):
        factory = APIRequestFactory()
        request = factory.get('api/users/')
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
