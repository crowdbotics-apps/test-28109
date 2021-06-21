from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Functions.debuging import Debugging
from Functions.tests_credentials import tests_setup_function
from email.message import EmailMessage

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'crowboticstest@gmail.com'
# EMAIL_HOST_PASSWORD = 'crowbotics123@1'
from users.models import User


class AuthTestings(APITestCase):
    # def setUp(self):
        # tests_setup_function(self)
    def test_verfy_email(self):
        pass
        # self.register_data['email'] = api.rondomeemail
        # response = self.client.post('users/register/', self.register_data, format='json')

        # response = self.client.post('users/verify_email/', self.register_data, format='json')

    # def test_api_jwt_and_permissions_and_users(self):
    #     assert User.objects.count() == 0
    #     self.client.post(self.register_url, self.register_data, format='json')
    #     assert User.objects.count() == 1
    #     u = User.objects.get(id=1)
    #     u.is_active = False
    #     u.save()
    #     #
    #     resp = self.client.post(
    #         self.login_url, self.login_data, format='json')
    #     self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
    #     #
    #     u.is_active = True
    #     u.is_email_verified = True
    #     u.is_role_verified = True
    #     u.save()
    #     #
    #     client = APIClient()
    #     resp = client.post(
    #         self.login_url, self.login_data, format='json')
    #     self.assertEqual(resp.status_code, status.HTTP_200_OK)
    #     self.assertTrue('access' in resp.data)
    #     token = resp.data['access']
    #     refresh_token = resp.data['refresh']
    #     #
    #     verification_url = '/users/token/verify/'
    #     resp = self.client.post(
    #         verification_url, {'token': token}, format='json')
    #     self.assertEqual(resp.status_code, status.HTTP_200_OK)
    #     #
    #     resp = self.client.post(
    #         verification_url, {'token': 'abc'}, format='json')
    #     self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
    #     #
    #     client = APIClient()
    #     client.credentials(HTTP_AUTHORIZATION='Bearer abc')
    #     resp = client.get('/users/', data={'format': 'json'})
    #     self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
    #     client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    #     resp = client.get('/users/')
    #     self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
    #     assert 'You are not permitted to view user' in str(resp.data['permission error'])
    #     u.is_superuser = False
    #     u.is_staff = False
    #     u.save()
    #     #
    #     resp = client.get('/users/')
    #     self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
    #
    #     res = client.get('/users/1/')
    #     assert u.id == 1
    #     self.assertEqual(res.status_code, status.HTTP_200_OK) # TODO
    #
    #     u.user_permissions.add(
    #         get_permission_id('Can view username', User))
    #     u.save()
    #     #
    #     u.user_permissions.add(
    #         get_permission_id('Can view user', User))
    #     u.save()
    #     resp = client.get('/users/')
    #     assert len(resp.data[0]) >= 20
    #     self.assertEqual(resp.status_code, status.HTTP_200_OK)
    #
    #     resp = client.get('/users/1/')
    #     self.assertEqual(resp.status_code, status.HTTP_200_OK)
    #     #
    #     u.user_permissions.add(24)
    #     u.save()
    #     resp = client.get('/users/')
    #     assert len(resp.data[0]) >= 20
