from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        u = User.objects.create(username='zomor', email='a@a.com', is_superuser=True, is_active=True,
                                is_staff=True)
        u.set_password('zomor')
        u.save()
        print('User created successfully')
