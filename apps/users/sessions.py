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
from django.contrib.auth import logout
from django.contrib.sessions.backends.db import (
    SessionStore as DjangoSessionStore,
)


class DashSessions:
    """DashSessions Documentation.

    This module contains the DashSessions class, which provides a convenient
     wrapper around Django's session management.

    :class:`DashSessions` provides methods to create, read, update, and delete
     session variables using Django's `SessionStore` class.

    Example Usage:
        # Create a DashSessions object
        session = DashSessions()

        # Set a session variable
        session.set('username', 'john')

        # Retrieve a session variable
        username = session.get('username')

        # Update session data
        session.session_data = {
            'username': 'mary',
            'is_admin': True
        }

        # Delete a session variable
        session.delete('is_admin')

    Attributes:
        _session_store (SessionStore): An instance of Django's
        SessionStore class.

    Methods:
        __init__(): Initializes a DashSessions object.
        __getattr__(): Use Django's SessionStore methods to manage the
        session life cycle.
        set(key, value): Set the value of a session variable.
        get(key, default=None): Retrieve the value of a session variable.
        session_data: Property to access the session data as a dictionary.
        session_data(data): Setter to set session data for the current user.
    """
    def __init__(self):
        """Initializes a DashSessions object.

        This method initializes a DashSessions object by creating a
        session store using Django's SessionStore class.
        """
        self._session_store = DjangoSessionStore()

    def __getattr__(self, name):
        """Use Django's DjangoSessionStore method to manage session life cycle
        We create, read and delete by invoking save, load and delete method of
        DjangoSessionStore.
        """
        if name in ['save', 'create', 'load', 'delete']:
            return getattr(self._session_store, name)
        return None

    def set(self, key, value):
        """Set method for DashSessions class.

        :param key: The key for the session variable.
        :param value: The value to be assigned to the session variable.
        """
        self._session_store[key] = value

    def get(self, key, default=None):
        """Retrieve the value of a session variable with the given key.

        :param key: The key of the session variable.
        :param default: The default value to return if the session
            variable is not found.
        :return: The value of the session variable with the given key,
            or the default value if not found.
        """
        return self._session_store.get(key, default)

    @property
    def session_data(self):
        """:return: The session data as a dictionary"""
        return dict(self._session_store.items())

    @session_data.setter
    def session_data(self, data):
        """Sets session data for the current user.

        :param data: A dictionary containing the session data to be set.
            The keys represent the session storage keys, and the values
            represent the corresponding values to be stored.

        Example:
            {
                'key1': 'value1',
                'key2': 'value2',
                ...
            }
        :return: None
        :raises ValueError: If the provided data parameter is not a dictionary.
        """
        if isinstance(data, dict):
            for key, value in data.items():
                self.set(key, value)
        else:
            raise ValueError('Please provide a dict.')


class DashUserSession(DashSessions):
    """Class to handle user sessions in Dash application.

    This class provides methods to manage user sessions, including setting
     up a user session,
    closing a user session, and storing and retrieving session data.

    Methods:
        set_unverified_email: Sets the unverified email in the user
        session.
        get_unverified_email: Retrieves the unverified email from the
        user session.
        set_verification_flags: Sets the verification flags in the user
         session.
        get_verification_flags: Retrieves the verification flags from the
        user session.
    """
    def __init__(self, request):
        """Initializes a DashUserSessions object.

        :param request: The HTTP request object.
        """
        super().__init__()  # Initialize parent DashSessions class
        self.request = request

    def close_user_session(self, forget_me):
        """Close User Session.

        :param forget_me: Indicates whether to forget the user or not.
            (bool)
        :return: True if the user session is closed, False otherwise.
            (bool)
        """
        if forget_me:
            logout(self.request)
            return True
        return False

    def get_current_user(self):
        """Get the current logged in user from the request.
        Note: This uses Django's built-in authentication framework
         to get the current user.

        :return: The current user object.
        :rtype: django.contrib.auth.models.User
        """
        return self.request.user

    def get_session_key(self):
        """Get the current session key from Django's session management.

        :return: the session key
        :rtype: str
        """
        return self.request.session.session_key


    def set_email(self, email):
        """Set the email for the current user session.

        :param email: The email address to be set as unverified.
        :return: None
        """
        self.request.session['email'] = email

    def get_unverified_email(self):
        """Get the email from the session.

        :return: The email if it exists in the session, None otherwise.
        """
        return self.request.session.get('email', None)

    def set_verification_flags(self, is_valid=False, is_confirmed=False,
                               is_verified=False):
        """Set the verification flags for the user session.

        :param is_valid: A boolean signals whether the user is valid.
        :param is_verified: A boolean signals whether the user is
            verified.
        :param is_confirmed: A boolean signals whether the user is
            confirmed.
        :return: None
        """
        flags = {
            'is_valid':is_valid,
            'is_confirmed':is_confirmed,
            'is_verified':is_verified,
        }

        for key, value in flags.items():
            if value is True or value is False:
                self.request.session[key] = value
            else:
                self.request.session.pop(key, None)


    def get_verification_flags(self):
        """Get the verification flags from the session.

        :return: A tuple: the values of 'is_verified' & 'is_confirmed'.
        :rtype: tuple
        """
        is_valid = self.request.session.get('is_valid', False)
        is_confirmed = self.request.session.get('is_confirmed', False)
        is_verified = self.request.session.get('is_verified', False)
        return is_valid, is_confirmed, is_verified


    def fetch_session_items(self):
        """Fetches all items stored in the session.

        :return: A list of key-value pairs representing the items stored
            in the session.
        """
        return self.request.session.items()
