# Generated by Django 3.2.4 on 2021-06-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alerts', '0003_alter_alertsrules_filter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alerts',
            options={'get_latest_by': 'date_created'},
        ),
        migrations.AlterField(
            model_name='alertsrules',
            name='field',
            field=models.CharField(blank=True, help_text='if this blanck I will moniter all fields', max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='alertsrules',
            name='filter',
            field=models.CharField(blank=True, help_text='example: "oxgyn__lt=80"', max_length=30, null=True),
        ),
    ]
