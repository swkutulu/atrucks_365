"""
Скопировать в src/core/settings/local.py
Поменять:3
- secret_key
- database
- redis_database_num (это если нет докера и на одном сервере несколько приложений используют redis)
- cors
"""

from pathlib import Path
import os

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-%m7v$hy#$gya)_#%=9lsbqn=0gep3@^m9#4#0py_b@li3ftro7"
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("POSTGRES_DB", "atruck_swk"),
        'USER': os.environ.get("POSTGRES_USER", "django"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD", "123"),
        'HOST': os.environ.get('POSTGRES_HOST', '127.0.0.1'),
        'PORT': os.environ.get("POSTGRES_PORT", "5432"),
        'CONN_MAX_AGE': 600,
    },
}

CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3100',
]

REDIS_DATABASE_NUM = os.environ.get("REDIS_DATABASE_NUM", "0")

LOG_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent.joinpath('logs')
LOG_DIR.mkdir(parents=True, exist_ok=True)
