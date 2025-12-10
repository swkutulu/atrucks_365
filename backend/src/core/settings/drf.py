from .base import INSTALLED_APPS

INSTALLED_APPS += [
    # "dj_rest_auth",
    "rest_framework",
    "rest_framework.authtoken",
    # "drf_recaptcha",
    "drf_spectacular",
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle'
    # ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '100/day',
    #     'user': '1000/day'
    # },
}

# REST_AUTH = REST_AUTH_SERIALIZERS = {
#     'LOGIN_SERIALIZER': 'user.serializers.LoginSerializer',
#     'PASSWORD_RESET_SERIALIZER': 'user.serializers.PasswordResetSerializer',
#     'PASSWORD_RESET_CONFIRM_SERIALIZER': 'user.serializers.PasswordResetConfirmSerializer',
#     'USER_DETAILS_SERIALIZER': 'user.serializers.UserDetailsSerializer',
# }

# DRF_RECAPTCHA_SECRET_KEY = ''
# DRF_RECAPTCHA_ACTION_V3_SCORES = {
#     'site_form': 0.3,
#     'register': 0.5,
#     'default': 0.5
# }

SPECTACULAR_SETTINGS = {
    # https://drf-spectacular.readthedocs.io/en/latest/settings.html
    'TITLE': 'Atrucks API v1',
    'DESCRIPTION': '',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,

    # 'SERVE_PERMISSIONS': ['rest_framework.permissions.AllowAny'],
    'SERVE_PERMISSIONS': ['rest_framework.permissions.IsAdminUser',],
    # None will default to DRF's AUTHENTICATION_CLASSES
    # 'SERVE_AUTHENTICATION': None,
    'SERVE_AUTHENTICATION': ['rest_framework.authentication.SessionAuthentication'],
    # 'SERVE_AUTHENTICATION': 'rest_framework.authentication.RemoteUserAuthentication',
}
