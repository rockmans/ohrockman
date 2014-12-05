"""
Django settings for ohrockman project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
APP_ENV = os.environ.get('APP_ENV', 'local')
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
REMOTE_ROOT = '/usr/local/ohrockman'

if APP_ENV == "local":
    DB_ROOT = PROJECT_DIR
else:
    DB_ROOT = os.path.join(REMOTE_ROOT, 'db_' + APP_ENV)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(PROJECT_DIR, 'key.txt')) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
if APP_ENV != "prod":
    DEBUG = True
    TEMPLATE_DEBUG = True
    
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'donotreply8386@gmail.com'
EMAIL_HOST_PASSWORD = 'password8386'
EMAIL_PORT = 587
EMAIL_USE_TLS = True    

ALLOWED_HOSTS = [
    'www.ohrockman.com',
    'ohrockman.com',
    'localhost',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    #'photologue',
    'sortedm2m',
    'debug_toolbar',
    'raven.contrib.django.raven_compat',
    
    #'familytree',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'ohrockman.urls'

WSGI_APPLICATION = 'ohrockman.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_ROOT, 'default.db'),
    },
    'familytree': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_ROOT, 'familytree.db'),
    },
    'photos': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_ROOT, 'photo.db'),
    },
}
DATABASE_ROUTERS = [
    'ohrockman.db_router.PhotologueRouter',
    'familytree.db_router.FamilytreeRouter',
]

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
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
#FIXTURE_DIRS = (
#    os.path.join(PROJECT_DIR, 'ohrockman', 'fixtures'),
#)

if APP_ENV == "prod":
    RAVEN_CONFIG = {
        'dsn': 'http://4c42444377c04669b7d5abd62405e99a:2fc1ca8df97d4fd6928e34b5f148051c@sentry.rocktavious.com/3',
    }
else:
    RAVEN_CONFIG = {
        'dsn': 'http://5145de66cd3545d1a5a780842d04c28b:87597f0723e14b2da52d4a1fc217d2ad@sentry.rocktavious.com/5',
    }

if APP_ENV == "prod":
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
else:
    DEBUG_TOOLBAR_PATCH_SETTINGS = True