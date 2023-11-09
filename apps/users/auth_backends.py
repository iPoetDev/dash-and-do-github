#!/user/bin/env python3
# pylint: disable=R0901
"""@File: auth_backend.py
@Version: 0.3.0 to 0.3.0.?
@Desc: apps | users | auth_backend
@Author: Charles Fowler
@Copyright: 2023
@Date Created: 23/11/09
@Date Modified: 23/11/09
@Python Version: 3.12.0
@Django Version: 4.2.6
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
"""
# Imports
import logging

# AllAuth
from allauth.account.auth_backends import AuthenticationBackend
# Django
from django.contrib.auth import get_user_model

# Custom
from dash_and_do.settings import DEBUG


class LoggingAuthenticationBackend(AuthenticationBackend):

    def __init__(self):
        """ . """
        ### CUSTOM LOGGING Changelog: added: 2023-10-29
        if DEBUG:
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = None

    def authenticate(self, request, **credentials):
        """ Logging authentication backend

        :param request:
        :param credentials:
        :return: User instance if authenticated successfully, or None otherwise.
        :rtype: User | None
        """
        user = super().authenticate(request, **credentials)
        if DEBUG:
            username = credentials.get("username")
            password = credentials.get("password")
            email = credentials.get("email")
            debug_message = (
                "LoggingAuthenticationBackend: authentication: User {}: \n"
                "Credentials: {}\n"
                "Username: {}: Email: {}: Password: {}"
            )
            self.logger.debug(debug_message.format(user, credentials,
                                                   username, email, password))
        return user

    # def get_user(self, user_id):
    #     """ . """
    #     user = super().get_user(user_id)
    #     if DEBUG:
    #         debug_message = (
    #               "LoggingAuthenticationBackend: get_user: User {}"
    #             )
    #         self.logger.debug(debug_message.format(user))
    #     return user

    def user_can_authenticate(self, user):
        """ Checks if the user is active, can authenticate

        - getattr() function is trying to get the value of the is_active
         attribute from the user object.
        :param user: The user object.
        :type user: User
        :return: True if the user is active, or if omitted, False otherwise.
        :rtype: bool
        """
        can_authenticate = super().user_can_authenticate(user)
        if DEBUG:
            debug_message = (
                "LoggingAuthenticationBackend: user_can_authenticate: "
                "User Is Active: {}: \n"
            )
            self.logger.debug(debug_message.format(can_authenticate))
        return can_authenticate

    def get_user(self, user_id):
        """ Get current user by user id.

        :param user_id:
        :type user_id:
        :return:
        :rtype:
        """
        # noinspection PyPep8Naming
        User = get_user_model()
        try:
            user = User.objects.get(pk=user_id)
            if DEBUG:
                debug_message = (
                    "LoggingAuthenticationBackend: get_user: Id: {}"
                    "User Is : {}: \n"
                )
                self.logger.debug(debug_message.format(user_id, user))
        except User.DoesNotExist:
            self.logger.debug("User does not exist") if DEBUG else None
            return None
        return user if self.user_can_authenticate(user) else None
