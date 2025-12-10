import os
from .local import LOG_DIR

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(pathname)s '
                      '%(funcName)s %(lineno)d  %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        # 'skip_static': {
        #     '()': 'core.helpers.SkipStaticFilter',
        # }
    },
    'handlers': {
        # level - обрабатываются сообщения указанные в level и выше
        # CRITICAL 	50
        # ERROR 	40
        # WARNING 	30
        # INFO 	    20
        # DEBUG 	10
        # NOTSET 	0
        'null': {
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true']
        },
        'django': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'django.log'),
            'formatter': 'verbose',
            'maxBytes': 1024 * (1024 * 4),
            'backupCount': 3,
        },
        'celery_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'celery.log'),
            'formatter': 'verbose',
            'maxBytes': 1024 * (1024 * 4),
            'backupCount': 3,
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['django', 'console'],
        },
        'django': {
            'level': 'INFO',
            'handlers': ['django', 'console'],
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
        'celery': {
            'level': 'INFO',
            'handlers': ['celery_handler', 'console'],
            'propagate': False,
        },
    }
}
