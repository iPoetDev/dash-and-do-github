"""Django Production settings for dash_and_do project.

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

# ================== Imports ==================

from .settings import *

# ================== Keys & Mode ==================

if DEBUG is not True:
    DEBUG = env.bool('DEBUG', default=False)

# ================== Server & Hosting ==================
# - added: ALLOWED_HOSTS for localhost resources.

if DEBUG is False:
    ALLOWED_HOSTS = [
        'dash-and-do.herokuapp.com',
    ]

# ================== Application ==================

# ================== Database ==================

if DEBUG is False:
    DATABASES = {
        'default': env.db('DATABASE_URL')
    }
