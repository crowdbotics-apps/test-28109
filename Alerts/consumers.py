import json
from urllib.parse import parse_qs

from channels.generic.websocket import WebsocketConsumer
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from drf_queryfields import QueryFieldsMixin
from rest_framework import serializers

from Alerts.models import Alerts
from Functions.queryset_filtering import queryset_filtering
from calendars.models import Event
from patients.models import Patient
from users import models


class AlertsSer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Alerts
        fields = '__all__'
        # depth = 1


def return_notifcations(scope):
    user = scope.get('user')
    queries = scope['query_string']
    queries = parse_qs(queries.decode("utf8"))
    for i in queries.keys():
        queries[i] = queries[i][0]

    alerts = queryset_filtering(Alerts, queries)
    # if user:
    #     if not user.is_staff or not user.is_superuser:
    #         users = users.filter(id=user.id)
    serializer = AlertsSer(alerts, many=True)
    return json.dumps(serializer.data)



class Alerts(WebsocketConsumer):
    def connect(self):

        self.accept()
        user = self.scope.get('user')

        if not user:
            self.send('You are not authenticated')
            super().disconnect(self)

        @receiver(post_save, sender=Alerts)
        def __init__(sender, instance, **kwargs):
            self.send(return_notifcations(elf.scope))

    def receive(self, text_data):
        errors = []
        user = self.scope.get('user')
        # data = json.loads(text_data)
        # TODO date= Date.objects.get(id=data.id)
        # date = date.seen_by.add(user)
        # notifcation = return_notifcations(self.scope)
        # self.send(notifcation)

        # notifcation = return_notifcations(self.scope)

    def disconnect(self, close_code):
        print(close_code)
        print(self)
