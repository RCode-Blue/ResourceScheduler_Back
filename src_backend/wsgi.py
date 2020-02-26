"""
WSGI config for resourcescheduler project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise
from whitenoise import WhiteNoise

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resourcescheduler.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src_backend.config.common_settings')

application = get_wsgi_application()
# application = DjangoWhiteNoise(application)
application = WhiteNoise(application)