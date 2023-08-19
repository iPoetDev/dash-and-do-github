#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

#  Copyright (c) 2023.

import os
import sys

# Date: 2023-08-09
# Source
# Adjusted from: dash_and_do.settings => dash_and_do.settings.development
# Objective to: Isolated the settings for each environment.
# The settings for manage.py is development.py:
#

BASE_SETTINGS = 'dash_and_do.settings'
DEVELOPMENT_SETTINGS = 'dash_and_do.settings.development'
PRODUCTION_SETTINGS = 'dash_and_do.settings.production'
TEST_SETTINGS = 'dash_and_do.settings.tests'

def main():
    """Run administrative tasks."""
    if os.environ.get('DJANGO_SETTINGS_MODULE') != BASE_SETTINGS:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              BASE_SETTINGS)
    else:  # noqa
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                                BASE_SETTINGS)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
