#!/user/bin/env python3
"""
This module contains the views for the core app.

    @File: views.py
    @Version: 0.3.0 to 0.3.0.?
    @Desc: apps | core |  apps: AppConfig
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/08/07
    @Date Modified: 23/09/12
    @Python Version: 3.11.04
    @Django Version: 4.2.3
    @Notes / Ideas v Implement:
    @Changelog:
    - added: AppConfig for Core / Public App
"""
from django.apps import AppConfig
from dash_and_do.settings import DEFAULT_AUTO_FIELD as AUTO_FIELD
class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = 'Dash and Domain Public App'
    label = 'dash_and_do_apps_public'
    default = True
    default_auto_field = AUTO_FIELD

