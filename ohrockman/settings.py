"""
Django settings for ohrockman project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(BASE_DIR, 'ohrockman')
DB_ROOT = '/www/database/ohrockman'

DEBUG = True
TEMPLATE_DEBUG = False
DEBUG_TOOLBAR_PATCH_SETTINGS = False

with open(os.path.join(BASE_DIR, 'key.txt')) as f:
    SECRET_KEY = f.read().strip()


ALLOWED_HOSTS = ['www.ohrockman.com',
                 'ohrockman.com',
                 'localhost',
                 'localhost:9091']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_ROOT, 'family.db'),
    }
}


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'photologue',
    'south',
    'sortedm2m',    
    'debug_toolbar',
    'familytree',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ohrockman.urls'

WSGI_APPLICATION = 'ohrockman.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'http://media.ohrockman.com/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates')
)
from photologue import PHOTOLOGUE_APP_DIR
TEMPLATE_DIRS = (
    PHOTOLOGUE_APP_DIR,
)

try:
    from ohrockman.local_settings import *
except ImportError:
    pass
