#!/user/bin/env python3
"""
    @File: emails.py
    @Version: 0.3.0 to 0.3.1: Contact Form & Email
    @Desc: apps | core |  email | emails
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/09/12
    @Date Modified: 23/09/12
    @Python Version: 3.11.04
    @Django Version: 4.2.3
    @Notes / Ideas v Implement:
        - apps > core > email > emails: Form Email
                              > messages: Messaging Factories
                              > helpers: Email Helper Functions
        - Reserved for the function linked to the forms and, used by the views.
            -Uses common site_mail when contact form is submitted.
    @Changelog:
    - Added:
        - 23/09/12: Added docstrings
        - 23/09/12: Created initial file
        - 23/09/12: added Common Email Functionalities
    - Updated:
        - 23/09/12: Refactored Functions into messages.py and helpers.py
        - 23/09/13: Refactored Imports ...
            to reduce file level cycolmatic complexity
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
#  Copyright (c) 2023.

from django.core.mail import BadHeaderError
from django.http import HttpResponse

# Local: Common Libraries
from dash_and_do.settings.settings\
    import (DEFAULT_FROM_EMAIL as SITE_EMAIL)
# Local: App Libraries
from apps.core.email.values import (Services, HTTP, Field)
from apps.core.email.messages import site_mail

def send_mail_contact(form) -> HttpResponse:
    """
    Sends email to user/site contact when they submit a contact form.

    :param form:
    :return: HTTP Response: Invalid header found.
    :rtype: HttpResponse
    """
    # Contact Form particulars, valdiated and cleaned.
    name = form.cleaned_data[Field.NAME]
    email = form.cleaned_data[Field.EMAIL]
    message = form.cleaned_data[Field.MESSAGE]
    copy = form.cleaned_data[Field.COPY]

    # Send email & prevent header injection (Django Docs)
    if all([name,email, message]):
        try:
            # To enable Fail Silently: fails=ON, default is OFF.
            return site_mail(name, email, message,
                      [SITE_EMAIL], copy,
                      service=Services.BASIC)
        except BadHeaderError:
            return HttpResponse(HTTP.INVALID_HEADER)
    else:
        return HttpResponse(HTTP.MSG_FAILED)





