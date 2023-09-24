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
        - added: Added User Model: 23/09/?24
        - added: Added UserManager: 23/09/?24
    - Updated:
        - updated:
    @Plan:
        - TODO:
        - FIXME:
        - CHECK:
"""

# https://medium.com/
# @ksarthak4ever/django-custom-user-model-allauth-for(-oauth-20)c84888c3184
# OopCompanion:suppressRename

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.db import models
from django.utils import timezone

from apps.users.managers import DashUserManager


class DashUser(AbstractBaseUser, PermissionsMixin):
    """
    Credit:
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
    :rtype: User
    """

    class Meta:
        db_table = 'dashuser'  # optional, name of the table in db
        app_label = 'apps.users'



    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [ ]

    objects = DashUserManager()

    def get_absolute_url(self):
        """
        Return the absolute URL for the DashUser instance.

        :return: The absolute URL for the DashUser instance.
        """
        return "/users/%i/" % (self.pk)

    def __str__(self):
        return self.email
