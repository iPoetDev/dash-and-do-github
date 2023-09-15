#!/user/bin/env python3
"""
    @File: emailmixin.py
    @Version: 0.3.0 to 0.3.1: Core Mixins
    @Desc: apps | core | mixins |  emailmixin
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/08/07
    @Date Modified: 23/09/12
    @Python Version: 3.11.04
    @Django Version: 4.2.3
    @Notes / Ideas v Implement:
        - Handles the all email sending for the core app.
        - Sends email to user when they submit a contact form.
    @Changelog:
    - Added:
        - 23/09/12: Added docstrings
        - 23/09/12: Created initial file
        - 23/09/12: added Common Email Functionalities
    - Updated:
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
from django.core.mail import EmailMessage as CoreMessage
from anymail.message import AnymailMessageMixin
from mail_templated import EmailMessage as TemplatedMessage


class CoreTemplatedMixin(CoreMessage, TemplatedMessage):
    """
    A mixin class that combines CoreMessage (from Django's mailing system)
    and TemplatedMessage (from mail_templated package), providing functionalities
    from both in a single class.
    """
    pass


class TemplatedAnymailMixin(AnymailMessageMixin, TemplatedMessage):
    """
    An EmailMessage that supports both Mail-Templated
    and Anymail features
    """
    pass
