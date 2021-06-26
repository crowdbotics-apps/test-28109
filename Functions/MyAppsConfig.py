
from django.apps import AppConfig
from django.db import models

from Functions.make_fields_permissions import make_fields_permissions


class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'  # Don't modify, keep it as it is in your code
    name = 'Functions.MyAppsConfig'
    def ready(self):
        from django.contrib.auth.models import Permission
        from django.contrib.contenttypes.models import ContentType
        from django import apps
        from users.models import User

        try:
            # Dummy data
            User.objects.get_or_create(username='ali',email='x@x.com',password='password',is_staff=True,is_active=True,is_superuser=True,is_email_verified=True,is_role_verified=True)
        except:
            print('=================== no migratoins yet ===================')
            pass

        try:

            for Model in apps.apps.get_models():
                make_fields_permissions(Permission, ContentType, Model)
        except:
            pass