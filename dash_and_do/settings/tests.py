"""Django Test settings for dash_and_do project.

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
- Added:
"""

#  Copyright (c) 2023.

from .settings import *

DEBUG = False

# Add Heroku App names/URLs to ALLOWED_HOSTS.

ALLOWED_HOSTS = [
    'dash-and-do.herokuapp.com',
]
