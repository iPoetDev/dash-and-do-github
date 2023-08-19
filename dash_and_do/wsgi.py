"""WSGI config for dash_and_do project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/

Changelog:
2023-08-09:
- Updated: DJANGO_SETTINGS_MODULE's value to 'dash_and_do.settings.production'
"""

#  Copyright (c) 2023.

import os

from django.core.wsgi import get_wsgi_application

# Adjusted: dash_and_do.settings => dash_and_do.settings.production

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'dash_and_do.settings.production')

application = get_wsgi_application()
