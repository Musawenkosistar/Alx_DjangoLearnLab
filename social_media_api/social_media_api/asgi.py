"""
ASGI config for social_media_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
>>>>>>> afb93ecba8bc6ee8f5e3490d59b66bcbe1f64375
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_api.settings')

application = get_asgi_application()
