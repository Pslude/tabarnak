"""Production settings."""

from ..settings.base import *

# Server ID
HOST_NAME = 'tabarnak.app'

# Email
EMAIL_BACKEND = 'postmark.django_backend.EmailBackend'
SERVER_EMAIL = f'no-reply@{HOST_NAME}'
DEFAULT_FROM_EMAIL = SERVER_EMAIL
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME
# EMAIL_USE_TLS = False

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

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#     }
# }

ALLOWED_HOSTS += [
    HOST_NAME,
]
