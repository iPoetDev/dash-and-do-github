"""
Django Production settings for dash_and_do project.

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
- Added: DEBUG = False
- Added: ALLOWED_HOSTS for Heroku App names/URLs
"""

#  Copyright (c) 2023.
from .settings import *

DEBUG = env.bool('DEBUG', default=False)

# Add Heroku App names/URLs to ALLOWED_HOSTS.

ALLOWED_HOSTS = [
    'dash-and-do.herokuapp.com',
]

if DEBUG is False and 'debug_toolbar' not in INSTALLED_APPS:
    DATABASES = {
        'default': env.db('DATABASE_URL')
    }
