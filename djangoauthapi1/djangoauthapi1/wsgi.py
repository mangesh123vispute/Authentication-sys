"""
WSGI config for djangoauthapi1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoauthapi1.settings')

application = get_wsgi_application()
<<<<<<< HEAD
app=application
=======

app = application
>>>>>>> 28de849f368015131b36b0e3f12165bbc537f386
