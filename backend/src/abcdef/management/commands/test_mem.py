from django.core.management.base import BaseCommand
from abcdef import helpers
import requests
# from memory_profiler import profile


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.3029.110 Safari/537.36'
}


class Command(BaseCommand):

    # @profile
    def handle(self, *args, **options):
        helpers.process_files_all_sql()
        # helpers.process_files_all_pandas()

        # url = 'https://opendata.digital.gov.ru/downloads/ABC-3xx.csv'
        # res = requests.get(url, headers=headers)
        # print(res.status_code, res.headers)


# uv run python -m memory_profiler ./src/manage.py test_mem