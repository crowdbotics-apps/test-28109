from icecream import ic
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from Functions.tests_credentials import tests_setup_function
import mailslurp_client

from users.models import User
from users.utils import Util


class AuthTestings(APITestCase):
    def setUp(self):
        configuration = mailslurp_client.Configuration()
        configuration.api_key['x-api-key'] = '50ffea3b36eb23b18f7dd159881bb2e2556ce2ccbc2fde7b9cf78dc2555fcc2a'
        self.conf = configuration

        with mailslurp_client.ApiClient(self.conf) as api_client:
            # create an inbox using the inbox controller
            api_instance = mailslurp_client.InboxControllerApi(api_client)
            inbox = api_instance.create_inbox()
            inboxes = api_instance.get_all_inboxes()
            self.api_instance = api_instance
            self.api_client = api_client
            self.inboxes = inboxes
            self.inbox = inbox
            assert len(inbox.id) > 0
            assert "mailslurp.com" in inbox.email_address

        # tests_setup_function(self)

    def test_verfy_email(self):
        res = self.client.post('/users/register/', {
            "email": 'fake@g.com',
            "username": 'mynewusername',
            "password": 'password',
        })

        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        user = User.objects.get(email='fake@g.com')

        self.assertFalse(user.is_email_verified)
        token = RefreshToken.for_user(user).access_token
        token = str(token)
        res = self.client.get(f'/users/verify_email/?token={token}')
        user = User.objects.get(email='fake@g.com')
        self.assertTrue(user.is_email_verified)

    def test_sending_email(self):
        data = {'email_body': 'email_body', 'to_email': 'weplutus@gmail.com','email_subject': 'Reset your password.'}
        Util.send_email(data)
    #     TODO

    # def test_verfy_email2(self):
    # TODO
    # email = requests.get('http://emailsgernator.com')
    #     res = self.client.post('/users/register/', {
    #         "email": email.adress,
    #         "username": 'mynewusername',
    #         "password": 'password',
    #     })
    #
    #     self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    #     token = email.inbox.body.toekn
    #     res = self.client.get(f'/users/verify_email/?token={token}')
    #     user = User.objects.get(email='fake@g.com')
    #     self.assertTrue(user.is_email_verified)
