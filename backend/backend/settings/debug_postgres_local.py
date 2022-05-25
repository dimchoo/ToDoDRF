from .base import *

DEBUG = True

ALLOWED_HOSTS = []
STATIC_ROOT = ''

DATABASES = {
    'default': {
            'NAME': 'drf_db',
            'ENGINE': 'django.db.backends.postgresql',
            'USER': 'drf_user',
            'PASSWORD': 'DRF_pass123!',
            'HOST': '127.0.0.1',
            'PORT': 5433
    }
}

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.BrowsableAPIRenderer')
