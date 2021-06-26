from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
import factory
from factory.django import DjangoModelFactory

# from polls.models import Question as Poll
from icecream import ic

from calendars.models import Event, DateType
from users.models import User

import random

from django.db import transaction
from django.core.management.base import BaseCommand


NUM_USERS = 50
NUM_CLUBS = 10
NUM_THREADS = 12
COMMENTS_PER_THREAD = 25
USERS_PER_CLUB = 8


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    email = factory.Faker("email")
    password = factory.Faker("password")


class DateTypeFacotry(DjangoModelFactory):
    class Meta:
        model = DateType

    name = factory.Faker("name")
    description = factory.Faker("sentence")



class EventFacotry(DjangoModelFactory):
    class Meta:
        model = Event

    title = factory.Faker("sentence")
    description = factory.Faker("sentence")
    date_type = factory.SubFactory(DateTypeFacotry)
    created_by = factory.SubFactory(UserFactory)


def makeSuper(admin):
    admin.is_active = True
    admin.is_admin = True
    admin.is_admin = True
    admin.is_email_verified = True
    admin.is_role_verified = True
    admin.save()


class Command(BaseCommand):
    help = 'create dummy data'

    @transaction.atomic
    def handle(self, *args, **options):


        self.stdout.write("Deleting old data...")
        models = [User,Event,DateType]

        for m in models:
            m.objects.all().delete()

        admin = User.objects.create_superuser(email='ali@g.com', username='ali', password='password')
        makeSuper(admin)

        self.stdout.write("Creating new data...")
        # Create all the users
        people = []
        for _ in range(NUM_USERS):
            person = UserFactory()
            people.append(person)

        # Add some users to clubs
        for _ in range(NUM_CLUBS):
            club = DateTypeFacotry()

            # Create all the threads
        for _ in range(NUM_THREADS):
            creator = random.choice(people)
            thread = EventFacotry(created_by=creator)
            # Create comments for each thread
            # for _ in range(COMMENTS_PER_THREAD):
            #     commentor = random.choice(people)
            #     CommentFactory(
            #         user=commentor,
            #         thread=thread
            #     )






