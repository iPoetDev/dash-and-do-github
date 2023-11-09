#!/user/bin/env python3
"""@File: emails.py
@Version: 0.3.0 to 0.3.1: Contact Form & Email
@Desc: apps | kore |  emailing | emails
@Author: Charles Fowler
@Copyright: 2023
@Date Created: 23/09/12
@Date Modified: 23/09/12
@Python Version: 3.11.04
@Django Version: 4.2.3
@Notes / Ideas v Implement:
- apps > kore > emailing > emails: Form Email
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
from django.http import HttpResponseRedirect

from apps.kore.emailing.messages import contact_mail
from apps.kore.emailing.messages import site_mail
from apps.kore.emailing.values import Field
from apps.kore.emailing.values import HTTP
# Local: App Libraries
from apps.kore.emailing.values import Services
from apps.kore.emailing.values import Switch
from apps.kore.helpers import pp_email
from apps.kore.helpers import pp_label
# Local: Common Libraries
from dash_and_do.settings import DEFAULT_FROM_EMAIL as SITE_EMAIL


# Third parttom


# noinspection PyUnusedFunction
def send_mail_contact(form) -> HttpResponse:
    """Sends emailing to user/site contact when they submit a contact form.

    :param form:
    :return: HTTP Response: Invalid header found.
    :rtype: HttpResponse
    """
    # Contact Form particulars, valdiated and cleaned.
    name = form.cleaned_data[Field.NAME]
    email = form.cleaned_data[Field.EMAIL]
    message = form.cleaned_data[Field.MESSAGE]
    copy = form.cleaned_data.get(Field.COPY)
    pp_label(f'send_mail_contact: top: {form.cleaned_data}')
    # Send emailing & prevent header injection (Django Docs)
    if all([name, email, message]):
        try:
            # pp_email(form.cleaned_data, label='send_mail_contact: IF: ')
            # To enable Fail Silently: fails=ON, default is OFF.
            site_mail(name, email, message,
                [SITE_EMAIL], copy,
                service=Services.BASIC)
            # pp_form(form,
            #         label='send_mail_contact: true: HTTPResponse: Ok 200')
        except BadHeaderError:
            # pp_form(form,
            #         label='send_mail_contact: exception: BadHeaderError')
            return HttpResponse(HTTP.INVALID_HEADER)

        return HttpResponseRedirect(HTTP.REDIRECT_URL_PATH)

    # pp_form(form, label='send_mail_contact : '
    #                     'fields any not true: '
    #                     'HTTPResponse: Message Failed')
    return HttpResponse(HTTP.MSG_FAILED)


def send_mail_contact2(form) -> HttpResponse:
    """Sends emailing to user/site contact when they submit a contact form.

    :param form:
    :return: HTTP Response: Invalid header found.
    :rtype: HttpResponse
    """
    # Contact Form particulars, valdiated and cleaned.
    name = form.cleaned_data[Field.NAME]
    email = form.cleaned_data[Field.EMAIL]
    message = form.cleaned_data[Field.MESSAGE]
    # print(f'form.cleaned_data: {form.cleaned_data}')
    # copy = form.cleaned_data.get(Field.COPY)
    email_data = {
        Field.NAME:name,
        Field.EMAIL:email,
        Field.MESSAGE:message
    }
    # Send emailing & prevent header injection (Django Docs)
    if all([name, email, message]):
        pp_email(form.cleaned_data, label='send_mail_contact2: IF: ')
        # To enable Fail Silently: fails=ON, default is OFF.
        email_response = contact_mail(name,
            email,
            message,
            recipients=[SITE_EMAIL],
            fails=Switch.SHOW)
        pp_email(email_data, label='send_mail_contact_2: HTTPResponse: Ok '
                '200')
        return email_response

    pp_email(email_data, label='send_mail_contact_2: HTTPResponse: Failed '
            '???')
    return HttpResponse(HTTP.MSG_FAILED)
