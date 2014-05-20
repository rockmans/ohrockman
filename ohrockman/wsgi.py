"""
WSGI config for ohrockman_new project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os
import sys

try:
    activate_this = os.path.join('/Volumes', 'STORAGE', 'Web', 'ohrockman', '.virtualenv', 'bin', 'activate_this.py')
    execfile(activate_this, dict(__file__=activate_this))
    sys.path.append('/Volumes/STORAGE/Web/ohrockman')
except:
    activate_this = os.path.join(os.getcwd(), '.virtualenv', 'bin', 'activate_this.py')
    execfile(activate_this, dict(__file__=activate_this))
    sys.path.append(os.getcwd())
    

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ohrockman.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
