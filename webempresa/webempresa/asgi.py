"""
ASGI config for webempresa project.

It exposes the ASGI callable as a module-level variable named ``application``.

For blog information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webempresa.settings")

application = get_asgi_application()
