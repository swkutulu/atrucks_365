from .base import *  # noqa: F403, F401

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SESSION_COOKIE_SECURE = False  # https only


try:
    from .local import *  # noqa: F403, F401
except ImportError:
    pass
