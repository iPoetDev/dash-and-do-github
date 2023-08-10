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


DEBUG = False

# Add Heroku App names/URLs to ALLOWED_HOSTS.

ALLOWED_HOSTS = [
    'dash-and-do.herokuapp.com',
]

# ================== Debugging & Internal IP ==================
# https://docs.djangoproject.com/en/4.2/ref/settings/#test-runner

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# https://docs.djangoproject.com/en/4.2/ref/settings/#test-non-serialized-apps
TEST_NON_SERIALIZED_APPS = [
    'django.contrib.contenttypes',
]

# ================== Fitxures ==================
# https://docs.djangoproject.com/en/4.2/ref/settings/#fixture-dirs

FIXTURE_DIRS = []
