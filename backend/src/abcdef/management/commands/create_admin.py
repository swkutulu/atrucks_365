from django.db import transaction
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def put_superuser(self):
        User = get_user_model()
        obj_user, created = User.objects.get_or_create(username='atrucks')
        if created:
            obj_user.set_password('atrucks')
            obj_user.is_superuser = True
            obj_user.is_staff = True
            obj_user.save()

    @transaction.atomic
    def handle(self, *args, **options):
        self.put_superuser()
