import re

import pytest
from django.db import IntegrityError
from icecream import ic
from rest_framework import status
from rest_framework.test import APITestCase

from Alerts.models import Alerts, AlertsRules
from Functions.tests_credentials import tests_setup_function
from calendars.models import Event


class TestSignals(APITestCase):
    def setUp(self):
        tests_setup_function(self)

    def test_creaet_alert(self):
        initial = Alerts.objects.all().count()
        Event.objects.create(created_by=self.user, title='event')
        # assert Alerts.objects.all().count() == initial + 1

    def test_creaet_alert_when_update(self):
        initial = Alerts.objects.all().count()
        event = Event.objects.create(created_by=self.user, title='event')
        event.title = 'new'
        event.save()

    def test_rules(self):
        AlertsRules.objects.create(model='calendars_Event')
        AlertsRules.objects.create(model='patients_Patient')

    def test_dont_monitor(self):
        initial = Alerts.objects.all().count()
        event = Event.objects.create(created_by=self.user, title='event')
        f = Alerts.objects.all().count()
        assert initial == f

class TestRules(APITestCase):
    def setUp(self):
        tests_setup_function(self)
        res = self.client.post('/alerts/rules/', {
            "model": "Calendar | Event",
            "filter": '',
            "field": '',
            "field_value": '',
            "users": [1],
            "groups": [],
        })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_monitor(self):

        initial = Alerts.objects.all().count()
        event = Event.objects.create(created_by=self.user, title='event')
        f = Alerts.objects.all().count()
        # assert f == initial + 1 #TODO

    def test_monitor_spsfic_field(self):
        res = self.client.put('/alerts/rules/1/', {
            "field_value": 'name',
        })

        event = Event.objects.create(created_by=self.user, title='event')
        # f = Alerts.objects.all().latest()
        # ic(f)
        # assert f == initial + 1 #TODO

    def test_alert_only_target_users_groups(self):
        res = self.client.post('/alerts/rules/', {
            "users": [1],
            "groups": [1,3],
        })

        event = Event.objects.create(created_by=self.user, title='event')
        # f = Alerts.objects.all().latest()
        # ic(f)
        # assert f == initial + 1 #TODO



