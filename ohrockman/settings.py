"""
Django settings for ohrockman project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
APP_ENV = os.environ.get('APP_ENV', 'local')
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
REMOTE_ROOT = '/usr/local/kyleandemily'

if APP_ENV == "local":
    DB_ROOT = PROJECT_DIR
else:
    DB_ROOT = os.path.join(REMOTE_ROOT, 'db_' + APP_ENV)

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(PROJECT_DIR, 'key.txt')) as f:
    SECRET_KEY = f.read().strip()


# SECURITY WARNING: don't run with debug turned on in production!
if APP_ENV != "prod":
    DEBUG = True
    TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'www.ohrockman.com',
    'ohrockman.com',
    'localhost',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_ROOT, 'default.db'),
    },
    'admin': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_ROOT, 'admin.db'),
    },
    'familytree': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_ROOT, 'familytree.db'),
    },
    'photos': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_ROOT, 'photo.db'),
    }
}
# DATABASE_ROUTERS = [
#     'kyleandemily.wedding.db_router.PhotologueRouter',
# ]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'raven.contrib.django.raven_compat',
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
    'debug_toolbar.middleware.DebugToolbarMiddleware',
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
if APP_ENV == "local":
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
    MEDIA_URL = '/media/'
else:
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
    MEDIA_ROOT = os.path.join(REMOTE_ROOT, 'media_' + APP_ENV)
    STATIC_URL = 'http://' + APP_ENV + '.static.ohrockman.com/'
    MEDIA_URL = 'http://' + APP_ENV + '.media.ohrockman.com/'


STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'ohrockman', 'static'),
)
from photologue import PHOTOLOGUE_APP_DIR
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'ohrockman', 'templates'),
    PHOTOLOGUE_APP_DIR,
)

RAVEN_CONFIG = {
    'dsn': 'http://4c42444377c04669b7d5abd62405e99a:2fc1ca8df97d4fd6928e34b5f148051c@sentry.rocktavious.com/3',
}

DEBUG_TOOLBAR_PATCH_SETTINGS = False

try:
    from ohrockman.local_settings import *
except ImportError:
    pass
