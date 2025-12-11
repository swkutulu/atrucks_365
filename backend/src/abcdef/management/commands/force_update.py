from django.core.management.base import BaseCommand
from abcdef.tasks import download_files_task


class Command(BaseCommand):
    def handle(self, *args, **options):
        download_files_task.apply_async([0])
