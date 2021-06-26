from rest_framework.test import APITestCase

from Functions.tests_credentials import tests_setup_function
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'crowboticstest@gmail.com'
# EMAIL_HOST_PASSWORD = 'crowbotics123@1'
from timesheets.models import Column, Value


class AuthTestings(APITestCase):
    def setUp(self):
        tests_setup_function(self)

    def test_get_statstics(self):
        col = Column.objects.create(name='Oxygen',user=self.user)
        Value.objects.create(object_id='1',field_value='96%',column=col)
        Value.objects.create(object_id='2', column=col)
        res = self.client.get('/users/')
        assert res.data[0]['statistics'][0]['name'] == 'Oxygen'
        assert res.data[0]['statistics'][0]['values'][0]['object_id'] == '1'
        assert res.data[0]['statistics'][0]['values'][0]['field_value'] == '96%'

    # def test_get_patients(self):
    #     res = self.client.get('/users/?groups__containse=patient', data={'format': 'json'})
        # self.register_data['email'] = api.rondomeemail
        # resonse = self.client.post('users/register/', self.register_data, format='json')

        # resonse = self.client.post('users/verify_email/', self.register_data, format='json')


    # def test_api_jwt_and_permissions_and_users(self):
    #     assert User.objects.count() == 0
    #     self.client.post(self.register_url, self.register_data, format='json')
    #     assert User.objects.count() == 1
    #     u = User.objects.get(id=1)
    #     u.is_active = False
    #     u.save()
    #     #
    #     res = self.client.post(
    #         self.login_url, self.login_data, format='json')
    #     self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    #     #
    #     u.is_active = True
    #     u.is_email_verified = True
    #     u.is_role_verified = True
    #     u.save()
    #     #
    #     client = APIClient()
    #     res = client.post(
    #         self.login_url, self.login_data, format='json')
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     self.assertTrue('access' in res.data)
    #     token = res.data['access']
    #     refresh_token = res.data['refresh']
    #     #
    #     verification_url = '/users/token/verify/'
    #     res = self.client.post(
    #         verification_url, {'token': token}, format='json')
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     #
    #     res = self.client.post(
    #         verification_url, {'token': 'abc'}, format='json')
    #     self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    #     #
    #     client = APIClient()
    #     client.credentials(HTTP_AUTHORIZATION='Bearer abc')
    #     res = client.get('/users/', data={'format': 'json'})
    #     self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    #     client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    #     res = client.get('/users/')
    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    #     assert 'You are not permitted to view user' in str(res.data['permission error'])
    #     u.is_superuser = False
    #     u.is_staff = False
    #     u.save()
    #     #
    #     res = client.get('/users/')
    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
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
    #     res = client.get('/users/')
    #     assert len(res.data[0]) >= 20
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #
    #     res = client.get('/users/1/')
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     #
    #     u.user_permissions.add(24)
    #     u.save()
    #     res = client.get('/users/')
    #     assert len(res.data[0]) >= 20
