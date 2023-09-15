#!/user/bin/env python3
"""
    @File: models.py
    @Version: 0.3.0 to 0.3.0.?
    @Desc: apps | core | models
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
        - UserPasswordResetEmail model for user password reset email.
        - UserPasswordResetEmailDone model for user password reset email done.
        - UserPasswordResetEmailConfirm model for user password reset email confirmation.
        - UserPasswordResetEmailComplete model for user password reset email completion.
        - UserPasswordResetEmailSent model for user password reset email sent.
        - UserPasswordResetEmailSentDone model for user password reset email sent done.
        - UserPasswordResetEmailSentConfirm model for user password reset email sent confirmation.
        - UserPasswordResetEmailSentComplete model for user password reset email sent completion.
        - UserPasswordResetEmailSentEmail model for user password reset email sent email.
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
from dash_and_do.settings.settings import DEFAULT_FROM_EMAIL
from dash_and_do.validating import valid_name, valid_email

"""
    @Class: Contact
    @Form: ContactForm
    @Desc: Model for contact form submission, creates contact history log.
    @Fields:
        - name: CharField, max length of 50 characters.
        - email: EmailField, max length of 75 characters.
        - message: TextField
        - copySent: BooleanField, default False.
        - recipient: EmailField, max length of 75 characters,
                default: EMAIL_HOST_USER (Settings.py)
    @Methods:
        - __str__(self)
    @Notes:
        - Represents a contact form submission.
        - Stores the contact's name, email, and message.
        - Provides a string representation of the contact object
"""

class Contact(models.Model):
    name = models.CharField(max_length=50,
                            validators=[valid_name])
    email = models.EmailField(max_length=100,
                              validators=[valid_email])
    message = models.TextField()
    copySent = models.BooleanField(default=False)
    # recipient = models.EmailField(max_length=75,
    #                               default=DEFAULT_FROM_EMAIL,
    #                               validators=[valid_name])

    """
    :Return: A string representation of the object.
    """
    def __str__(self):
        return f'{self.name} ({self.email})'
