#!/user/bin/env python3
"""
    @File: helpers.py
    @Version: 0.3.0 to 0.3.1: Contact Form & Email Helpers
    @Desc: apps | core |  email | helpers: Email Helper Functions
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/09/12
    @Date Modified: 23/09/13
    @Python Version: 3.11.04
    @Django Version: 4.2.3
    @Notes / Ideas v Implement:
        - apps > core > email > emails: Form Email
                              > messages: Messaging Factories
                             > helpers: Email Helper Functions
        - Helpers for message body building in email app.
            - CC -
            - Sent By -
            - Send
    @Changelog:
    - Added:
        - 23/09/13: Added docstrings
        - 23/09/13: Created initial file
        - 23/09/13: Refactored into file from email app.py
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

# Local: Common Libraries
from dash_and_do.utils import get_date
# Local: App Libraries
from .values import (HTTP, Sending, Switch)


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
    message += "\n\nMessage Sent by {}".format(name)
    message += "\n\nSent at {}".format(get_date())
    return message


def send(message, fail) -> HttpResponse:
    """
    Send email to user/site contact when they submit a contact form.

    :param message: The message.
    :param fail: bool: Fail silently flag.
    :return: A `HttpResponse` object.
    :rtype: HttpResponse
    """
    return HttpResponse(HTTP.MSG_SENT) \
        if message.send(fail_silently=fail) == Sending.SUCCESS \
        else HttpResponse(HTTP.MSG_FAILED)  # Copyright (c) 2023.


def any_status(message):
    """
    Sends email to user/site contact when they submit a contact form.
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
