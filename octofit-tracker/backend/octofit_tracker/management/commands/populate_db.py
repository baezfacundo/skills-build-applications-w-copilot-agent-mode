from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as octo_models

from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team = octo_models.Team
        Activity = octo_models.Activity
        Leaderboard = octo_models.Leaderboard
        Workout = octo_models.Workout
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create_user(username='tony', email='tony@stark.com', password='ironman', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@rogers.com', password='cap', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@wayne.com', password='batman', team=dc)
        clark = User.objects.create_user(username='clark', email='clark@kent.com', password='superman', team=dc)

        # Create activities
        Activity.objects.create(user=tony, type='run', duration=30)
        Activity.objects.create(user=steve, type='cycle', duration=45)
        Activity.objects.create(user=bruce, type='swim', duration=60)
        Activity.objects.create(user=clark, type='run', duration=50)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 50 pushups')
        Workout.objects.create(name='Situps', description='Do 100 situps')

        # Create leaderboard
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=95)
        Leaderboard.objects.create(user=clark, score=98)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
