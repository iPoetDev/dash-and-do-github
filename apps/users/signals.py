#!/user/bin/env python3
# pylint: disable=R0901
"""@File: signals.py
@Version: 0.3.0 to 0.3.0.?
@Desc: apps | users |  signals.py
@Author: Charles Fowler
@Copyright: 2023
@Date Created: 23/10/?
@Date Modified: 23/10/??
@Python Version: 3.12.0
@Django Version: 4.2.3/.04/.05
@Notes / Ideas v Implement:
- .
@Changelog:
- Added:
- added: Created initial file: 23/mm/dd/
- Updated:
- updated:
@Plan:
- TODO:
- FIXME:
- CHECK:
    - DONE:
    - IGNORE:
EXAMPLES?:
1) Print to console the sign for email confirmation (debugging, testing)
   1) Define here
   2) Import via the apps.users.apps.py ready() method
"""
# Imports

# Globals
from allauth.account.signals import email_confirmation_sent
from django.dispatch import receiver

# Custom
from dash_and_do.settings import DEBUG, LOCAL_IP, RS_PORT


@receiver(email_confirmation_sent)
def console_print_comfirmurl(sender, confirmation, **kwargs):
    APPROUTE = "users"
    if DEBUG:
        confirmation_url = (f"http://{LOCAL_IP}:"
                            f"{RS_PORT}/confirm-email/%s/" %
                            confirmation.key)
        print(
            f"Email confirmation URL for {confirmation.email_address}: {confirmation_url}")
