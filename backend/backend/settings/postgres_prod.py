from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
            'NAME': 'drf_db',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'drf_user',
            'PASSWORD': 'DRF_pass123!',
            'HOST': 'db',
            'PORT': '5432'
    }
}

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.BrowsableAPIRenderer')
