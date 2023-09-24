#!/user/bin/env python3
"""
    @File: models.py
    @Version: 0.3.0 to 0.3.0.?
    @Desc: apps | kore | models
    @Author: Charleston Fowler
    @Copyright: 2023
    @Date Created: 23/08/07
    @Date Modified: 23/09/12
    @Python Version: 3.11.04
    @Django Version: 4.2.3
    @Notes / Ideas v Implement:
        - Contact model for contact form submission.
        - UserSignup model for new user registration.
        - UserLogin model for user login.
        - UserLogout model for user logout.
        - UserDelete model for user deletion.
        - UserUpdate model for user update.
        - UserPasswordChange model for user password change.
        - UserPasswordReset model for user password reset.
        - UserPasswordResetConfirm model for user password reset confirmation.
        - UserPasswordResetComplete model for user password reset completion.
        - UserPasswordResetDone model for user password reset done.
        - UserPasswordResetEmail model for user password reset emailing.
        - UserPasswordResetEmailDone model for user password reset emailing done.
        - UserPasswordResetEmailConfirm model for user password reset emailing confirmation.
        - UserPasswordResetEmailComplete model for user password reset emailing completion.
        - UserPasswordResetEmailSent model for user password reset emailing sent.
        - UserPasswordResetEmailSentDone model for user password reset emailing sent done.
        - UserPasswordResetEmailSentConfirm model for user password reset emailing sent confirmation.
        - UserPasswordResetEmailSentComplete model for user password reset emailing sent completion.
        - UserPasswordResetEmailSentEmail model for user password reset emailing sent emailing.
    @Changelog:
    - Added:
        - 23/08/07: Created initial file
        - 23/09/12: added Contact model
    - Updated:
        - 23/09/12: Added docstrings
    - Deprecated:
        - 23/09/12: Deprecated
    - Removed:
        - 23/09/12: Removed
    @Plan:
        - TODO:
            - Create test cases for models.
              - Define Test Scenarios
                - Happy Path
                - Edge Cases
                - Other
"""
from django.db import models
from dash_and_do.settings import DEFAULT_FROM_EMAIL
from dash_and_do.validating import valid_name, valid_email


# OopCompanion:suppressRename

"""
    @Class: Contact
    @Form: ContactForm
    @Desc: Model for contact form submission, creates contact history log.
    @Fields:
        - name: CharField, max length of 50 characters.
        - emailing: EmailField, max length of 75 characters.
        - message: TextField
        - copySent: BooleanField, default False.
        - recipient: EmailField, max length of 75 characters,
                default: EMAIL_HOST_USER (Settings.py)
    @Methods:
        - __str__(self)
    @Notes:
        - Represents a contact form submission.
        - Stores the contact's name, emailing, and message.
        - Provides a string representation of the contact object
"""


class Contacts(models.Model):

    name = models.CharField(max_length=50,
                              name='contact_name')
    email = models.EmailField(max_length=50,
                              default=DEFAULT_FROM_EMAIL,
                              name='contact_email')
    message = models.TextField(name='contact_message')
    copySent = models.BooleanField(default=False,
                                   name='copy_sent')

    """
    :Return: A string representation of the object.
    """

    def __str__(self):
        return f'{self.name} ({self.email})'
