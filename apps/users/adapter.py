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
import logging  ### CUSTOM LOGGING Changelog: added: 2023-10-29
from allauth.account.adapter import DefaultAccountAdapter
from allauth.utils import build_absolute_uri
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from dash_and_do.settings import DEBUG


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

    def __init__(self, request=None):
        super().__init__(request)
        ### CUSTOM LOGGING Changelog: added: 2023-10-29
        if DEBUG:
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = None

    def authenticate(self, request, **credentials):
        """
        :param request: The HTTP request object.
        :type request: HttpRequest
        :param credentials: Dictionary containing the user credentials.
        :type credentials: dict
        :return: The authenticated user object or None if authentication fails.
        :rtype: User

        This method is used to authenticate a user using the provided
        credentials.
        It takes in an HTTP request object and a dictionary of user credentials.
        It returns the authenticated user object if the authentication
            is successful, otherwise it returns None.

        Example usage:
            request = HttpRequest()
            credentials = {'username': 'admin', 'password': 'password'}
            user = authenticate(request, **credentials)

        Note: This method extends the DefaultAccountAdapter class from
        allauth.account.adapter module and overrides its authenticate method.

        .. note::
            This method also logs the authentication request using the custom
            logging module.
            If DEBUG mode is enabled in the settings, the debug log will
            contain the details of the authentication request.

        Changelog:
            - 2023-10-29: Added custom logging for authentication requests.
        """
        user = super().authenticate(request, **credentials)

        ### CUSTOM LOGGING Changelog: added: 2023-10-29
        def user_details(user):
            """

            :param user:
            :type user:
            :return:
            :rtype:
            """
            try:
                # Store user details for logging
                user_detail = (f"User: "
                               f"{user.username if hasattr(user, 'username') else '(No username)'}, authenticated: {user.is_authenticated if hasattr(user, 'is_authenticated') else '(Not checked)'}")
            except Exception as e:
                # Catch exception if any error occurs during user details
                # extraction
                user_detail = (f"Error occurred during user details "
                               f"extraction: {str(e)}")
            return user_detail

        if self.logger is not None:
            user_deets = user_details(user)
            self.logger.debug(
                "DashAccountAdapter.authenticate: "
                f"Request: "
                f"{request if request is not None else 'Inspect Method'}\n"
                f"Credentials: {credentials}\n"
                f"User Details: {user_deets}"
                f"User: {user}",
                extra={'User': user,
                       'Credentials': credentials,
                       'User Details': user_deets}
            )
        return user

    def pre_authenticate(self, request, **credentials):
        """
        Pre-authenticates the user before login or signup.
        ### CUSTOM LOGGING Changelog: added: 2023-10-29
        - added only to trace the issue with the DashLoginView: request=none
        :param request: The request object.
        :type request: HttpRequest
        :param credentials: The user credentials.
        :type credentials: dict
        :return: None
        :rtype: None

        """
        super().pre_authenticate(request, **credentials)
        ### CUSTOM LOGGING Changelog: added: 2023-10-29
        if self.logger is not None:
            self.logger.debug(
                "DashAccountAdapter.pre_authenticate: "
                f"Request: "
                f"{request if request is not None else 'Inspect Method'}\n"
                f'Credentials: {credentials}',
                extra={'Credentials': credentials}
            )

    def _get_login_attempts_cache_key(self, request, **credentials):
        """
        Get the cache key for storing login attempts.

        :param request: The request object.
        :type request: HttpRequest
        :param credentials: The login credentials.
        :type credentials: dict
        :return: The cache key.
        :rtype: str

        """
        cache_key = super()._get_login_attempts_cache_key(request,
                                                          **credentials)
        if self.logger is not None:
            self.logger.debug(
                "DashAccountAdapter._get_login_attempts_cache_key: "
                f"Request: "
                f"{request if request is not None else 'Inspect Method'}",
                extra={'Credentials': credentials, 'Cache Key': cache_key}
            )

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

    def send_account_already_exists_mail(self, email):
        signup_url = build_absolute_uri(self.request, reverse(
            'users:account_signup'))
        # password_reset_url = build_absolute_uri(self.request, reverse(
        #     "account_reset_password"))

        ctx = {
            'request': self.request,
            'current_site': get_current_site(self.request),
            'email': email,
            'signup_url': signup_url,
            # 'password_reset_url': password_reset_url,
        }

        self.send_mail('account/email/account_already_exists', email, ctx)


dash_adapter = DashAccountAdapter()
