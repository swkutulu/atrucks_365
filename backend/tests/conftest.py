import pytest
# import logging

pytest_plugins = ("celery.contrib.pytest", )


@pytest.fixture(scope='session', autouse=True)
def django_db_setup():
    from django.conf import settings

    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_atrucks_swk',
        'USER': 'django',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'CONN_MAX_AGE': 1600,
        'PORT': 5432,
        'ATOMIC_REQUESTS': True,
    }
