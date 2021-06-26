import re

import pytest
from django.db import IntegrityError
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



