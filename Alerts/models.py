from django.contrib.auth.models import Group
from safedelete.models import SafeDeleteModel
from django.conf import settings
from django.db import models
from safedelete.models import SafeDeleteModel

from calendars.models import Event
from datetime import datetime

from users.models import User

now = datetime.now()


class SeenBy(SafeDeleteModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='alert_seen_by_user',on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # def duration(self):
    #     return self.date_created - now


class SeeAlert(SafeDeleteModel):
    model = models.CharField(max_length=30, unique=True, help_text='Spsfy a model to moniter it')
    object_id = models.PositiveIntegerField(blank=True, null=True,help_text='if this blanck I will moniter all objects')
    seen_by = models.ManyToManyField(SeenBy, related_name='alert_seen_by', blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class AlertsRules(SafeDeleteModel):
    model = models.CharField(max_length=30, unique=True, help_text='Spsfy a model to moniter it')
    object_id = models.PositiveIntegerField(blank=True, null=True,
                                            help_text='if this blanck I will moniter all objects')
    filter = models.CharField(max_length=30)
    field = models.PositiveIntegerField(blank=True, null=True, help_text='if this blanck I will moniter all fields')
    field_value = models.CharField(max_length=30,null=True,blank=True, help_text='If field value equal/gte/contains... then I will alert you')
    users = models.ManyToManyField(User, related_name='alert_target_users', blank=True)
    groups = models.ManyToManyField(Group, related_name='alert_target_groups', blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
