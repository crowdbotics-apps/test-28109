from rest_framework import status
from rest_framework.test import APITestCase

from Functions.tests_credentials import tests_setup_function


class SennBytests(APITestCase):
    def setUp(self):
        tests_setup_function(self)

    def test_basic(self):
        res = self.client.get('/alerts/seen_by/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)