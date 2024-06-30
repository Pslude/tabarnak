"""Development settings."""

from ..settings.base import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = '/var/log/django-mail/'

# DATABASES = {
#     'default': {
#         'NAME': 'tabarnak',
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'USER': '',
#         'HOST': '',
#         'PASSWORD': '',
#         'CONN_MAX_AGE': None,
#     }
# }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

TEMPLATE_DEBUG = True

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
]

if 'debug_toolbar' in INSTALLED_APPS:
    MIDDLEWARE = [
         'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + MIDDLEWARE

INTERNAL_IPS = ('127.0.0.1', )

ALLOWED_HOSTS += [
    '127.0.0.1',
    'tabarnak',
]
