#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

#  Copyright © 2023.

import os
import sys
import warnings
# Date: 2023-08-09
# Source
# Adjusted from: dash_and_do.settings → dash_and_do.settings.development
# Objective to: Isolated the settings for each environment.
# The settings for manage.py is development.py:
#

BASE_SETTINGS = 'dash_and_do.settings'

def main():
    """Run administrative tasks."""
    settings = BASE_SETTINGS
    # Choose this according to your environment.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    # Supress warnings
     # djt_nvu\panel.py:20, pkg_resources is deprecated as an API.
    # https://setuptools.pypa.io/en/latest/pkg_resources.html
    warnings.filterwarnings("ignore",
                            category=DeprecationWarning,
                            module='pkg_resources')

if __name__ == '__main__':\
    main()
