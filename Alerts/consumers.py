import json
from urllib.parse import parse_qs

from channels.generic.websocket import WebsocketConsumer
from django.db.models.signals import pre_save
from django.dispatch import receiver
from drf_queryfields import QueryFieldsMixin
from rest_framework import serializers

from Functions.debuging import Debugging
from Functions.queryset_filtering import queryset_filtering
from calendars.models import Event
from patients.models import Patient
from users import models


class UserSer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'id', 'events']
        depth = 1


def return_notifcations(scope):
    # context = {'request': scope, 'method': 'view'}
    ids = []
    user = scope.get('user')
    queries = scope['query_string']
    queries = parse_qs(queries.decode("utf8"))
    for i in queries.keys():
        queries[i] = queries[i][0]

    users = queryset_filtering(models.User, queries)
    if user:
        if not user.is_staff or not user.is_superuser:
            users = users.filter(id=user.id)
    serializer = UserSer(users, many=True)
    return json.dumps(serializer.data)



class Alerts(WebsocketConsumer):
    def connect(self):
        Debugging(models.User.objects.all().count(), color='blue')

        self.accept()
        user = self.scope.get('user')

        if not user:
            self.send('You are not authenticated')
            super().disconnect(self)

        @receiver(pre_save, sender=Patient)
        @receiver(pre_save, sender=Event)
        def __init__(sender, instance, **kwargs):
            model = None
            fields = None
            messages = []
            # SeeAlert.objects.create(model=sender.__name__,object_id=instance.id)
            from django.apps import apps
            Model = apps.get_model(instance._meta.app_label, sender.__name__)

            class MySer(serializers.ModelSerializer):
                class Meta:
                    model = Model
                    fields = '__all__'

            try:
                model = Model.objects.get(id=instance.id)
            except:
                pass
            serializer = MySer(instance, many=False)
            data = serializer.data
            if model:
                olddata = MySer(model, many=False).data
                for key in olddata.keys():
                    if key != 'id' and data[key] == olddata[key]:
                        #TODO why ralatoinal data like users, seen_by changes dn't apera?
                        data.pop(key)
                messages.append({'updated': 'true'})
            else:
                messages.append({'created': 'true'})
            messages.append({'model_name': sender.__name__})
            messages = {"data":data, "messages": messages}
            data = json.dumps(messages)
            self.send(data)

        self.send(return_notifcations(self.scope))

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
