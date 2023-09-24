#!/user/bin/env python3
"""
    @File: helpers.py
    @Version: 0.3.0 to 0.3.1: Contact Form & Email Helpers
    @Desc: apps | kore |  emailing | helpers: Email Helper Functions
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/09/12
    @Date Modified: 23/09/13
    @Python Version: 3.11.04
    @Django Version: 4.2.3
    @Notes / Ideas v Implement:
        - apps > kore > emailing > emails: Form Email
                              > messages: Messaging Factories
                             > helpers: Email Helper Functions
        - Helpers for message body building in emailing app.
            - CC -
            - Sent By -
            - Send
    @Changelog:
    - Added:
        - 23/09/13: Added docstrings
        - 23/09/13: Created initial file
        - 23/09/13: Refactored into file from emailing app.py
        - 23/09/13: added Subject line helper
    - Updated:
        - 23/09/13: Refactored Imports ...
            to reduce file level cycolmatic complexity
    - Deprecated:
    @Plan:
        - TODO:
            - Create test cases for models.
              - Define Test Scenarios
                - Happy Path
                - Edge Cases
                - Other
"""
#  Copyright (c) 2023.
# Framework Libraries
from django.http import HttpResponse

# Local: App Libraries
from apps.kore.emailing.values import (HTTP, Sending, Switch)
# Local: Common Libraries
from dash_and_do.utils import get_date


# OopCompanion:suppressRename


def subject(site, name) -> str:
    """"""
    subj = ''
    subj += f'{site}: New Message from {name}'
    subj += f' - {get_date()}'
    return subj


def sender_cc(message: str, copy: bool) -> str:
    """
    Append copy flag to the message.

    :param message: The message to.
    :param copy: The copy flag.
    :return: The appended message.
    :rtype: str
    """
    return message + "\n\nWith a copy cc'd to sender." if copy else message


def sent_by(message: str, name: str) -> str:
    """
    Append sender details to the message.

    :param message: The message.
    :param name: The sender's name.
    :return: The appended message.
    :rtype: str
    """
    message += f"\n\nMessage Sent by {name}"
    message += f"\n\nSent at {get_date()}"
    return message


def send(message, fail) -> HttpResponse:
    """
    Send emailing to user/site contact when they submit a contact form.

    :param message: The message.
    :param fail: bool: Fail silently flag.
    :return: A `HttpResponse` object.
    :rtype: HttpResponse
    """
    return HttpResponse(HTTP.MSG_SENT) \
        if message.send(fail_silently=fail) == Sending.SUCCESS \
        else HttpResponse(HTTP.MSG_FAILED)


def any_status(message):
    """
    Sends emailing to user/site contact when they submit a contact form.
    :param message:
    :return:
    """
    return message.anymail_status  # available after sending


def any_config(message, sender, tracking=Switch.OFF):
    """
    Configures AnyMail message settings.
    :param message: AnymailMessage: AnymailMessage object
    :param sender: str: From Email Address, Return-Path header, Bounce Address.
    :param tracking: boolean: Enable/Disable Open Tracking at Message Level
    :return: message: AnyMailMessage: Configured AnymailMessage object
    """
    # Return-Path header (used for bounces) defaults to From header
    message.envelope_sender = sender
    # Open Tracking
    message.track_opens = tracking
    return message
