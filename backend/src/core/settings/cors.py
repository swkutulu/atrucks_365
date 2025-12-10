from .base import INSTALLED_APPS, MIDDLEWARE

INSTALLED_APPS.append('corsheaders')

MIDDLEWARE.append('corsheaders.middleware.CorsMiddleware')

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    # "sessionid",
    # "authentication",
    # "x-session",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_EXPOSE_HEADERS = [
    "content-disposition",
    "x-suggested-filename",
]