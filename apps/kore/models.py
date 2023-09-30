#!/user/bin/env python3
"""@File: models.py
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
# OopCompanion:suppressRename

from dash_and_do.settings import DEFAULT_FROM_EMAIL
from django.db import models


class Contacts(models.Model):
    """Represents a contact from a user.

    Attributes:
        name (str): The name of the contact.
        email (str): The email address of the contact.
        message (str): The message from the contact.
        copySent (bool): Indicates whether a copy of the message has been sent.

    Methods:
        __str__: Returns a string representation of the contact.

    """
    name = models.CharField(max_length=50,
                            name='contact_name',
                            blank=False,
                            null=False)
    email = models.EmailField(max_length=50,
                              default=DEFAULT_FROM_EMAIL,
                              name='contact_email',
                              blank=False,
                              null=False)
    message = models.TextField(name='contact_message',
                               blank=False)
    copySent = models.BooleanField(default=False,
                                   name='copy_sent')


    def __str__(self):
        """:Return: A string representation of the object."""
        return f'{self.name} ({self.email})'
