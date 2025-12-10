import os
from celery.schedules import crontab
from .local import REDIS_DATABASE_NUM

CELERY_TIMEZONE = 'UTC'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60 * 100
BROKER = 'redis'

BROKER_URL = os.environ.get("CELERY_BROKER_URL", "")

if BROKER_URL:
    CELERY_BROKER_URL = BROKER_URL
    CELERY_RESULT_BACKEND = BROKER_URL
    CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
elif BROKER == 'redis':
    # REDIS_DATABASE_NUM = os.environ.get("REDIS_DATABASE_NUM", "0")
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = '6379'
    BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DATABASE_NUM}'
    CELERY_BROKER_URL = BROKER_URL
    CELERY_RESULT_BACKEND = BROKER_URL
    CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}


CELERY_BEAT_SCHEDULE = {
    'download-files-task': {
        'task': 'abcdef.tasks.download_files_task',
        # 'args': ('0',),
        'schedule': crontab(hour='1'),
        # 'schedule': crontab(minute='*/5'),
    },
}
