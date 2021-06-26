# Generated by Django 3.2.4 on 2021-06-26 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('timesheets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='seen_by',
            field=models.ManyToManyField(blank=True, related_name='seen_by_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='column',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='statistics', to=settings.AUTH_USER_MODEL),
        ),
    ]
