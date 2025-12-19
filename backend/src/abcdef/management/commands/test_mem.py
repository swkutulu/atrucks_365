from django.core.management.base import BaseCommand
from abcdef import helpers
# from memory_profiler import profile


class Command(BaseCommand):

    # @profile
    def handle(self, *args, **options):
        helpers.process_files_all_sql()
        # helpers.process_files_all_pandas()


# uv run python -m memory_profiler ./src/manage.py test_mem