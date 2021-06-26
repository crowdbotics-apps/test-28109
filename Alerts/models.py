import re
from datetime import datetime


from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models
from django.db.models.signals import pre_save, m2m_changed, post_save
from django.dispatch import receiver
from icecream import ic
from rest_framework import serializers
from safedelete.models import SafeDeleteModel
from safedelete.models import SafeDeleteModel

from calendars.models import Event
from users.models import User

now = datetime.now()


class SeenBy(SafeDeleteModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='alert_seen_by_user', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # def duration(self):
    #     return self.date_created - now


class AlertsRules(SafeDeleteModel):
    model = models.CharField(max_length=30, help_text='Spsfy a model to moniter it')
    object_id = models.PositiveIntegerField(blank=True, null=True,
                                            help_text='if this blanck I will moniter all objects')
    filter = models.CharField(max_length=30,help_text='example: "oxgyn__lt=80"')
    field = models.PositiveIntegerField(blank=True, null=True, help_text='if this blanck I will moniter all fields')
    field_value = models.CharField(max_length=30, null=True, blank=True,
                                   help_text='If field value equal/gte/contains... then I will alert you')
    users = models.ManyToManyField(User, related_name='rule_alert_target_users', blank=True)
    groups = models.ManyToManyField(Group, related_name='rule_alert_target_groups', blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Alerts(SafeDeleteModel):
    model = models.CharField(max_length=30)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    # messages = JsonField(max_length=30, null=True, blank=True)
    users = models.ManyToManyField(User, related_name='alert_target_users', blank=True)
    groups = models.ManyToManyField(Group, related_name='alert_target_groups', blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class SeeAlert(SafeDeleteModel):
    alert = models.ForeignKey(Alerts, on_delete=models.CASCADE, null=True)
    seen_by = models.ManyToManyField(SeenBy, related_name='alert_seen_by', blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

def __init__(sender, instance, **kwargs):
    class MySer(serializers.ModelSerializer):
        class Meta:
            model = sender
            fields = '__all__'

    # if m2m:
    #     sender_name = re.findall(r"(.+?)_(.+)", sender.__name__)
    #     model_name = sender_name[0][0]
    #     field_name = sender_name[0][1]
    #     pass
    messages = []
    if kwargs.get('created'):
        messages.append({'created': 'true'})
        serializer = MySer(instance, many=False)
        Alerts.objects.create(model=sender.__name__)
    else:
        # Model = apps.get_model(instance._meta.app_label, model_name)
        Model = apps.get_model(instance._meta.app_label, sender.__name__)
        # obj = Model.objects.get(id=instance.id)
        # data = MySer(obj, many=False).data
        olddata = MySer(instance, many=False).data
        # for key in olddata.keys():
            # if data[key] == olddata[key]:
            #     data.pop(key) if key != 'id' else None
    # for alert in AlertsRules.objects.all():
    #
    #     serializer = MySer(instance, many=False)
    #     messages.append({'updated': 'true'})
    #
    #     messages.append({'model_name': sender.__name__})
    #     Alerts.objects.create(model=sender.__name__,messages=messages)

models = []
try:
    from django.contrib.contenttypes.models import ContentType
    # then_item = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # from django.apps import apps
    for alert in AlertsRules.objects.all():
        sender_name = re.findall(r"(.+?)_(.+)", alert.model)
        app_name = sender_name[0][0]
        model_name = sender_name[0][1]
        # model = apps.get_model(app_name, model_name)
        # models.append(model)
except:
    ic('there are no migrations yet')

for i in models:
    post_save.connect(__init__, sender=i)
    pre_save.connect(__init__, sender=i)
    m2m_changed.connect(__init__, sender=i)
