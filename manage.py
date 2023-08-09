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
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'dash_and_do.settings.development')
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
