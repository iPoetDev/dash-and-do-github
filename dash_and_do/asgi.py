"""ASGI config for dash_and_do project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/

Changelog:
2023-08-09:
- Updated: DJANGO_SETTINGS_MODULE's value to 'dash_and_do.settings.production'
"""

#  Copyright (c) 2023.

import os

from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'dash_and_do.settings')

application = get_asgi_application()
