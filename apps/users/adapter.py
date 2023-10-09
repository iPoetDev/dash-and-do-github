#!/user/bin/env python3
"""
    @File: <filename>.py
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

    EMAILCONFIRM_REVERSE = 'users:account_confirm_email'

class DashAccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_url(self, request, emailconfirmation):
        """Constructs the email confirmation (activation) url."""
        url = reverse(FormViews.EMAILCONFIRM_REVERSE,
                      args=[emailconfirmation.key])
        ret = build_absolute_uri(request, url)
        return ret
