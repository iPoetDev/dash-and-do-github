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
-  Option 3: A Custom User Model
Subsisitute the default User model by subclassing AbstractBaseUser
Defaul fields not preserved by subclassing:
Impacts existing methods
Entire new User Model, Update of settings .py
App has specif requirements (like using AllAuth)
Flex to use email as id token, not username,
Pro: most freedome, cons: most work
@Changelog:
- Added:
- added: Created initial file: 23/09/?24
- added: Added User Model: 23/09/24
- added: Added UserManager: 23/09/24
- Updated: User Model additional methods: 23/11/01
- updated:
@Plan:
- TODO:
- FIXME:
- CHECK:
  - DONE: Pylint: 10/10, 23/09/30
"""

# https://medium.com/
# @ksarthak4ever/django-custom-user-model-allauth-for(-oauth-20)c84888c3184
# OopCompanion:suppressRename

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from apps.users.managers import DashUserManager


class DashUser(AbstractBaseUser, PermissionsMixin):
    """Credit:
    - Author: Sarthak Kumar(@ksarthak4ever)
    - Title: Django Custom User Model + Allauth for OAuth
    - Date Created: 2019-04-02
    - URL: https://medium.com/
    - USER: @ksarthak4ever/
    - SLUG: django-custom-user-model-allauth-for-oauth-20c84888c3184
    - Last Accessed: 2023-09-24
    :class: DashUser: Custom User Model, subclasses: AbstractBaseUser
    :param email:
    :param name:
    :param is_staff: required by admin
    :param is_superuser: PermissionsMixin to grant all permissions
    :param is_active: user active?
    :param last_login:
    :param date_joined:
    :param USERNAME_FIELD: unique id, i.e email
    :param EMAIL_FIELD: re get_email_field_name()
    :param REQUIRED_FIELDS: list of required fields on sigh up
    :param objects: User Manager
    :return: User
    :rtype: User.
    """

    class Meta:  # pylint: disable=R0903
        """Meta definition for DashUser."""
        db_table = 'dashuser'  # optional, name of the table in db
        app_label = 'users'
        verbose_name = 'DashUser'

    email = models.EmailField(max_length=50,
                              null=False,
                              blank=False,
                              unique=True,
                              default='')
    name = models.CharField(max_length=50,
                            null=True,
                            blank=True,
                            default='')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True,
                                      blank=True,
                                      default=timezone.now)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = DashUserManager()

    def get_absolute_url(self):
        """Return the absolute URL for the DashUser instance.

        :return: The absolute URL for the DashUser instance.
        """
        return f'/users/{self.pk}/'

    def __str__(self):
        """Return the string representation of the DashUser instance."""
        return f'{self.name} ({self.email})' \
            if self.name else self.email or 'No email'

    def get_full_name(self):
        """ Returns the full name (email) of the user.

        :param self: DashUser: The instance of the `DashUser` class.
        :return: The full name of the user.
        :rtype: str
        """
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        """ Return the short name (email) of the user.

            :param self: DashUser: The instance of the `DashUser` class.
            :return: The short name of the user.
            :rtype: str
        """
        # The user is identified by their email address
        return self.email

    # noinspection PyUnusedFunction
    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    # noinspection PyUnusedFunction
    @property
    def is_a_staff(self):
        """Is the user a member of staff?"""
        return self.is_staff

    # noinspection PyUnusedFunction
    @property
    def is_a_super(self):
        """Is the user a admin member?"""
        return self.is_superuser
