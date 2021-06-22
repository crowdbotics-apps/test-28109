# Generated by Django 3.2.4 on 2021-06-22 16:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, unique=True)),
                ('description', models.TextField(max_length=200, null=True, unique=True)),
                ('threshold', models.CharField(max_length=200, null=True, unique=True)),
                ('goal', models.CharField(max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CPTcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('code', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('phone_number', models.TextField(blank=True, max_length=500, null=True, validators=[django.core.validators.RegexValidator('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$', 'invalid phone number')])),
                ('second_phone_number', models.TextField(blank=True, max_length=500, null=True, validators=[django.core.validators.RegexValidator('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$', 'invalid phone number')])),
                ('relationship', models.CharField(blank=True, choices=[('family', 'family'), ('friend', 'friend'), ('cousin', 'cousin'), ('siblings', 'siblings'), ('parent', 'parent'), ('partner', 'partner')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('primary', models.CharField(blank=True, max_length=50)),
                ('secondary', models.CharField(blank=True, max_length=50)),
                ('subscriber', models.CharField(blank=True, max_length=50)),
                ('number', models.PositiveBigIntegerField(blank=True)),
                ('group_number', models.PositiveBigIntegerField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('score', models.PositiveIntegerField(blank=True, help_text='the score represent the how much is the patient need attentian or in danger', null=True)),
                ('gender_identity', models.CharField(blank=True, max_length=50)),
                ('marital_status', models.CharField(blank=True, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_adhering', models.BooleanField(default=False)),
            ],
            options={
                'get_latest_by': 'date_created',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('eligible', models.BooleanField(default=False)),
                ('report_generated', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_payed', models.BooleanField(default=False)),
                ('amount', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'get_latest_by': 'date_created',
            },
        ),
        migrations.CreateModel(
            name='PrimaryCarePhysician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('full_name', models.CharField(blank=True, max_length=50)),
                ('phone_number', models.TextField(blank=True, max_length=500, null=True, validators=[django.core.validators.RegexValidator('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$', 'invalid phone number')])),
                ('office_phone', models.TextField(blank=True, max_length=500, null=True, validators=[django.core.validators.RegexValidator('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$', 'invalid phone number')])),
                ('office_fax', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('title', models.CharField(max_length=30, unique=True)),
                ('priority', models.CharField(blank=True, choices=[('low', 'low'), ('averge', 'averge'), ('heigh', 'heigh')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('title', models.CharField(max_length=30, unique=True)),
                ('cost', models.PositiveIntegerField(blank=True, null=True)),
                ('serveces', models.CharField(blank=True, choices=[('(99201–99215)', 'Office/other outpatient services'), ('(99217–99220)', 'Hospital observation services'), ('(99221–99239)', 'Hospital inpatient services'), ('(99241–99255)', 'Consultations'), ('(99281–99288)', 'Emergency department services'), ('(99291–99292)', 'Critical care services'), ('(99304–99318)', 'Nursing facility services'), ('(99324–99337)', 'Domiciliary, rest home (boarding home) or custodial care services'), ('(99339–99340)', 'Domiciliary, rest home (assisted living facility), or home care plan oversight services'), ('(99341–99350)', 'Home health services'), ('(99354–99360)', 'Prolonged services'), ('(99363–99368)', 'Case management services'), ('(99374–99380)', 'Care plan oversight services'), ('(99381–99429)', 'Preventive medicine services'), ('(99441–99444)', 'Non-face-to-face physician services'), ('(99450–99456)', 'Special evaluation and management services'), ('(99460–99465)', 'Newborn care services'), ('(99466–99480)', 'Inpatient neonatal intensive, and pediatric/neonatal critical, care services'), ('(99487–99489)', 'Complex chronic care coordination services'), ('(99495–99496)', 'Transitional care management services'), ('(99499)', 'Other evaluation and management services')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(max_length=400)),
                ('score', models.PositiveIntegerField(blank=True, help_text='the score represent the danger of the symptom', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
