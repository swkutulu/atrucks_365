from .base import *   # noqa: F403, F401

ALLOWED_HOSTS = ["*"]
DEBUG = False

SESSION_COOKIE_SECURE = True  # https only


try:
    from .local import *   # noqa: F403, F401
except ImportError:
    pass
