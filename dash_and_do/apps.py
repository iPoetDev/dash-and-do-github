#!/user/bin/env python3
"""This module contains the views for the kore app.

@File: apps.py
@Version: 0.3.0 to 0.3.0.?
@Desc: project | dash_and_do |  apps.: Relabling 3rd party app
@Author: Charles Fowler
@Copyright: 2023
@Date Created: 23/08/07
@Date Modified: 23/09/12
@Python Version: 3.11.04
@Django Version: 4.2.3
@Notes / Ideas v Implement:
- Fixes for: 2 third party apps without same app label
- Renames 1: Pinax
@Changelog:
- noted: Use function based views for the kore app.
- added:
"""
# OopCompanion:suppressRename

from django.apps import AppConfig


class DashAndDoConfig(AppConfig):
    """Dash & Do Project/Central Configuration.

    This class is the configuration for the Dash & Do Project/Central.
    """
    name = 'dash_and_do'
    verbose_name = 'Dash & Do'

    def ready(self):
        """Ready - Dash & Do Project/Central

        This method is called when the Dash & Do Project/Central is ready.
        :return:
        """
        pass
