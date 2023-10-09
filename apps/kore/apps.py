#!/user/bin/env python3
"""@File: <filename>.py
@Version: 0.3.0 to 0.3.0.?
@Desc: apps | <app> |  <module>
@Author: Charles Fowler
@Copyright: 2023
@Date Created: 23/09/?
@Date Modified: 23/09/??
@Python Version: 3.11.04
@Django Version: 4.2.3/.04/.05
@Notes / Ideas v Implement:
- .
@Changelog:
- Added:
- added: Created initial file: 23/09/??:
- Updated:
- updated:
@Plan:
- TODO:
- FIXME:
- CHECK:
"""

# OopCompanion:suppressRename
from django.apps import AppConfig
class KoreApp(AppConfig):
    """AppConfig for the kore app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.kore'  # The name of your Public application
