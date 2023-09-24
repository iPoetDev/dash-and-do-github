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
        -  Option 3: A Custom User Manager for Custom User Model
        Subsisitute the default User model by subclassing AbstractBaseUser
        Defaul fields not preserved by subclassing:
        Impacts existing methods
        Entire new User Model, Update of settings .py
        App has specif requirements (like using AllAuth)
        Flex to use email as id token, not username,
        Pro: most freedome, cons: most work
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
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


# https://medium.com/
# @ksarthak4ever/django-custom-user-model-allauth-for(-oauth-20)c84888c3184
# OopCompanion:suppressRename


class DashUserManager(BaseUserManager):
    """
    Credit:
      - Author: Sarthak Kumar(@ksarthak4ever)
      - Title: Django Custom User Model + Allauth for OAuth
      - Date Created: 2019-04-01
      - URL: https://medium.com/
      - USER: @ksarthak4ever/
      - SLUG: django-custom-user-model-allauth-for-oauth-20c84888c3184
      - Last Accessed: 2023-09-24
    :method _create_user:
    :method create_user: Overrides, for email over user name implementation
    :method create_superuser: Overrides, email over user name implementation
    """

    def _create_user(self, email, password, is_staff, is_superuser,
                     **extra_fields):
        """
        :param email: The email address of the user.
        :param password: The password for the user.
        :param is_staff: Boolean indicating if the user is a staff member.
        :param is_superuser: Boolean indicating if the user is a superuser.
        :param extra_fields: Additional fields to be saved for the user.
        :return: The created user object.

        Method for creating a new user.
         Creates a new user with the given email,password, staff status,
         superuser status, and any additional fields provided.

         The email must be provided, otherwise a ValueError is raised.
         The user is saved using the 'create' method of the model, which
         automatically sets the last_login and date_joined fields to the
         current time. The user's password is hashed using
         the 'set_password' method. The created user object is returned.
        """
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        """
        Create a user with the given email and password.

        :param email: The email of the user.
        :param password: The password for the user.
        :param extra_fields:
            Additional fields to be included when creating the user.
        :return: The created user.
        """
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create a superuser with the given parameters.

        :param email: The email of the superuser.
        :param password: The password of the superuser.
        :param extra_fields: Extra fields for the superuser model.
        :return: The created superuser.

        """
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user
