"""
WSGI config for newproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newproject.settings')

<<<<<<< HEAD
app = get_wsgi_application()
=======
application = get_wsgi_application()
app=newapp
>>>>>>> 8c0dd8e8b724120e633de759ea8010c95d815f0e
