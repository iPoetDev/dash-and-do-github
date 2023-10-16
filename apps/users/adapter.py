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
from allauth.account.adapter import DefaultAccountAdapter
from allauth.utils import build_absolute_uri
from django.urls import reverse


class FormViews:
    """FormViews class provides a Constants for Strings/Configurations as per
    12Factor App methodology.

    Attributes:
        EMAILCONFIRM_REVERSE (str): The reverse URL name for the
         email confirmation view, see apps.users.urls.py
    """
    EMAILCONFIRM_REVERSE = 'users:account_confirm_email'


class DashAccountAdapter(DefaultAccountAdapter):
    """DashAccountAdapter.

    This module contains the `DashAccountAdapter` class,
    Is a subclass of `DefaultAccountAdapter`.
    See ACCOUNT_ADAPTER in settings.py

    Classes:
        - DashAccountAdapter

    Methods:
        - get_email_confirmation_url
    """

    def get_email_confirmation_url(self, request, emailconfirmation):
        """Overides the `get_email_confirmation_url` method in the
        DefaultAccountAdapter class. Reverse() does not handle url namespaces.

        :param request: The HTTP request object.
        :param emailconfirmation: The email confirmation object.
        :return: The URL for email confirmation.
        :rtype: str

        Usage: In the CompleteSignup method in AllAuth,
                sending the link in the email.
        """
        url = reverse(FormViews.EMAILCONFIRM_REVERSE,
                      args=[emailconfirmation.key])
        return build_absolute_uri(request, url)
