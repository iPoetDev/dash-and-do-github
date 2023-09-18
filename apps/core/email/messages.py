#!/user/bin/env python3
"""
    @File: messages.py
    @Version: 0.3.0 to 0.3.1: Contact Form & Email
    @Desc: apps | core |  email | messages: Message Factories
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
        - Handles the all email sending for the core app.
        - Refactored into own library for reuse.
        - Use the 3 EmailMessage Sources: Core.Mail, AnyMail, MailTemplated
    @Changelog:
    - Added:
        - 23/09/12: Added docstrings
        - 23/09/12: Created initial file
        - 23/09/12: added Common/Shared Email Functionalities
        - 23/09/13: Refactored into file from email app.py
    - Updated:
        - 23/09/13: Refactored Imports ...
            to slightly reduce file level cycolmatic complexity
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
# Framework Libraries
from django.core.mail \
    import (send_mail, get_connection, EmailMessage, BadHeaderError)
from django.http import HttpResponse
# Third Party Libraries
from anymail.message import AnymailMessage
from mail_templated import send_mail, EmailMessage as TemplatedMessage

# Local: Common Libraries
from dash_and_do.utils import get_date
from dash_and_do.config.settings \
    import (DEFAULT_FROM_EMAIL as SITE_EMAIL, emailenv as EMAILENV)
# Local: App Libraries
from apps.core.email.values \
    import (Site, Services, SMTP, HTTP, Sending, MIME, Switch, Template)
from apps.core.email.helpers import (sender_cc, sent_by, send, any_config)


def site_mail(name: str, sender: str, message: str, recipients: list,
              copy: bool, service: str,
              fails: bool = Switch.OFF) -> HttpResponse:
    """
    Builds and sends email messages to user and site contact

    :param name: The mail sender's name.
    :param sender: The mail sender's email.
    :param message: The mail message body.
    :param recipients: The mail recipients.
    :param copy: The copy flag.
    :param service: The mail service.
    :param fails: The fails flag.
    :returns: A `HttpResponse` object.
    :rtype: HttpResponse
    """
    subject = 'New: Dash & Do Message from {}'.format(name)
    subject += ' - {}'.format(get_date())

    if len(recipients) == 1 and recipients[0] == SITE_EMAIL:
        recipients.append(sender) if copy else None
        message = sent_by(message, name)
        message = sender_cc(message, copy)
        # Returns a HTTP Response (with message) if successful/not.
        return send_control(subject, name, message,
                            sender, recipients,
                            service, fails)
    else:
        # Returns a HTTP Response (with message) when not successful/.
        return HttpResponse(HTTP.MSG_FAILED)


def send_control(subject: str, name: str, message: str,
                 sender: str, recipients: list,
                 service: str,
                 fails: bool = Switch.OFF) -> HttpResponse:
    """
    Send Control: Check email service and send mail.

    :param subject: The mail subject.
    :param name: The mail sender's name.
    :param message: The mail message body.
    :param sender: The mail sender.
    :param recipients: The mail recipients.
    :param service: The mail service.
    :param fails: The fails flag.
    :return: A `HttpResponse` object.
    :rtype: HttpResponse
    """
    basic_service = EMAILENV.str('BASIC_EMAIL', default=Services.BASIC)
    # Toggle between messaging services.
    # TODO: Add more message services.
    if basic_service == service:
        smtp = get_connection(SMTP.BACKEND)
        # Checks if the email was sent.
        if send_mail(subject, message, from_email=sender,
                     recipient_list=recipients, fail_silently=fails,
                     connection=smtp) == Sending.SUCCESS:
            # Returns a HTTP Response (with message) when successful.
            return HttpResponse(HTTP.MSG_SENT)
        else:
            # Returns a HTTP Response (with message) when not successful/.
            return HttpResponse(HTTP.MSG_FAILED)
    else:
        # Returns a HTTP Response (with message) if successful/not.
        return any_mail(subject, sender, recipients, message, message)


def send_default(subject, message,
                 sender, recipients,
                 copy=Switch.OFF, fail=Switch.OFF):
    """
    Sends email to user/site contact when they submit a contact form.

    :param subject:
    :param message:
    :param sender:
    :param recipients:
    :param copy:
    :param fail:
    :return: HTTP Response: Invalid header found.
    """
    # Send email & prevent header injection (Django Docs)
    if all([subject, message, sender, recipients]):
        try:
            # Determine the cc list based on whether the sender wants a copy of the message
            cc_list = [sender] if copy else None

            # Build the Email and Reply-To is sender.
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=sender,
                to=recipients,
                cc=cc_list,
                reply_to=[sender]
            )

            # SafeMIMEText is used to clean the message body.
            email.message()
            return send(email, fail)
        except BadHeaderError:
            # Illegal/Invalid headers found.
            return HttpResponse(HTTP.INVALID_HEADER)
    else:
        # Missing required fields. No need to be more specific
        # (except if for debugging).
        return HttpResponse(HTTP.MSG_FAILED)


def any_mail(subject, sender, recipients, text_content, name='',
             html_content='', fail=Switch.OFF) -> HttpResponse:
    """
    Sends email to user/site contact when they submit a contact form.

    :param subject:
    :param sender:
    :param recipients:
    :param text_content:
    :param name: Nasm of sender: Optional
    :param html_content: HTML Content: Optional
    :param fail:
    :return: HTTP Response: Invalid header or Message Success/Fail.
    :rtype: HttpResponse
    """
    # Send email & prevent header injection (Django Docs)
    if all([subject, name, sender, recipients, text_content]):
        # Detect Header Injection, if cleaned, proceed/
        try:
            # Send the mail: Default Service | Failback service if provider
            # is not available. Admins adjust an enviromental string variable to
            # enable, as a application setting. Following 12 Factor App Methodology.
            message = AnymailMessage(
                subject=subject,
                body=text_content,
                from_email=sender,
                to=recipients, )

            if html_content != '':
                message.attach_alternative(html_content, MIME.HTML)

            message = any_config(message, sender)
            return send(message, fail)
            # any_status(message)
        except BadHeaderError:
            # Illegal/Invalid headers found.
            return HttpResponse(HTTP.MSG_FAILED)
    else:
        # Missing required fields. No need to be more specific
        # (except if for debugging).
        return HttpResponse(HTTP.MSG_FAILED)


def templated_contact(subject, name, sender, recipients,
                      text_content, fail=Switch.OFF):
    """
    Sends email to user/site contact when they submit a contact form.

    :param subject: Default.
    :param name: Contact Form: id=contact-name-id, Sender's Full Name
    :param sender: Contact Form: id=contact-email, Senders Email
    :param recipients: SITE_EMAIL, sender cc'd if copy flag is set.
    :param text_content: Contact Form: id=contact-message.
    :param fail: bool: Fail silently flag.
    :return: HTTP Response: Invalid header found.
    """
    # Send email & prevent header injection (Django Docs)
    # if subject and sender and recipients and text_content and html_content:
    if all([subject, name, sender, recipients, text_content]):
        try:
            # Send the mail: Default Service | Failback service if provider
            # is not available. Admins adjust an enviromental string variable to
            # enable, as a application setting. Following 12 Factor App Methodology.
            message = TemplatedMessage()
            message.template_name = Template.CONTACT_EMAIL
            message.context = {
                Template.SUBJECT: subject,
                Template.NAME: name,
                Template.PLAIN: text_content,
                Template.HTML: text_content,
                Template.SITE: Site.NAME,
                Template.URL: Site.URL,
                Template.SENTON: get_date(),
            }
            # Returns a HTTP Response (with message) if successful/not.
            return send(message, fail)
        except BadHeaderError:
            # Illegal/Invalid headers found.
            return HttpResponse(HTTP.INVALID_HEADER)
    else:
        # Missing required fields. No need to be more specific
        # (except if for debugging).
        return HttpResponse(HTTP.MSG_FAILED)
