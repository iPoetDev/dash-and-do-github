"""Django Development settings for dash_and_do project.

Source by https://youtu.be/uetyOZeVrOE
Author: Johannes Spielmann
Title: DjangoCon 2021 WorkShop | Suggestions for common challenges in your
projects
Last Accessed: 2023-08-09

Intention: Include any settings overrides for the development environment here.
- Django Developer Tools (Apps)
- Django Local Allowed Hosts

Impacts: manage.py, settings.py

Changelog:
2023-08-09:
- Added: ALLOWED_HOSTS for localhost resources
- Added: Developer Tools (Apps)
"""

#  Copyright (c) 2023.

from .settings import *

# Include any installed apps for development here.

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.0.43']

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
]

if DEBUG and 'debug_toolbar' in INSTALLED_APPS:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
