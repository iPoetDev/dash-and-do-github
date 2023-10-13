#!/user/bin/env python3
"""@File: messages.py
@Version: 0.3.0 to 0.3.1: Contact Form & Email
@Desc: apps | kore |  emailing | messages: Message Factories
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
- Handles the all emailing sending for the kore app.
- Refactored into own library for reuse.
- Use the 3 EmailMessage Sources: Core.Mail, AnyMail, MailTemplated
@Changelog:
- Added:
- 23/09/12: Added docstrings
- 23/09/12: Created initial file
- 23/09/12: added Common/Shared Email Functionalities
- 23/09/13: Refactored into file from emailing app.py
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
from smtplib import SMTPException

# Third Party Libraries
from anymail.message import AnymailMessage
from django.core.mail import BadHeaderError
from django.core.mail import EmailMessage
from django.core.mail import get_connection
#  Copyright (c) 2023.
# Framework Libraries
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseServerError
from mail_templated import EmailMessage as TemplatedMessage
from mail_templated import send_mail as templatemailer

from apps.kore.emailing.helpers import any_config
from apps.kore.emailing.helpers import send
from apps.kore.emailing.helpers import sender_cc
from apps.kore.emailing.helpers import sent_by
from apps.kore.emailing.helpers import subject
from apps.kore.emailing.values import HTTP
from apps.kore.emailing.values import MIME
from apps.kore.emailing.values import SMTP
from apps.kore.emailing.values import Sending
from apps.kore.emailing.values import Services
# Local: App Libraries
# from apps.kore.helpers import (pp_form, pp_email, pp_response, pp_console)
from apps.kore.emailing.values import Site
from apps.kore.emailing.values import Switch
from apps.kore.emailing.values import Template
from apps.kore.helpers import pp_message
from dash_and_do.settings import DEFAULT_FROM_EMAIL as SITE_EMAIL
from dash_and_do.settings import emailenv as env
# Local: Common Libraries
from dash_and_do.utils import get_date


def contact_mail(sub_ject: str,
    message: str,
    sender: str,
    recipients: list,
    fails: bool = Switch.ON) -> HttpResponse:
    """Sends emailing to user/site contact when they submit a contact form.
    :param sub_ject:
    :param message:
    :param sender:
    :param recipients:
    :param fails:
    :return:
    """
    smtp = get_connection(SMTP.BACKEND)
    pp_message(subject, recipients, sender, message, fail=fails)
    # Checks if the emailing was sent.  # pylint: disable=fixme
    try:
        result = send_mail(sub_ject, message, from_email=sender,
            recipient_list=recipients, fail_silently=fails,
            connection=smtp) == Sending.SUCCESS
        # pp_response(result, label='contact_mail: send_mail()')

        # Returns a HTTP Response (with message) if successful/not.
        if result:  # == 1 successful mail Sending.SUCCESS
            # Returns a HTTP Response (with message) if successful/not.
            # pp_console(HTTP.MSG_SENT, label='contact_mail: send_mail() OK')
            return HttpResponse(HTTP.MSG_SENT, status=HTTP.STATUS.OK,
                reason=HTTP.MSG_SENT)
        # == 0 failed mail Sending.FAILURE
        # Returns a HTTP Response (with message) when not successful/.
        # pp_console(HTTP.MSG_FAILED, label='contact_mail: send_mail() FAIL')
        return HttpResponse(HTTP.MSG_FAILED,
            status=HTTP.STATUS.BAD_REQUEST,
            reason=HTTP.MSG_FAILED)
    # Exception
    except SMTPException as server_error:
        print(server_error)
        return HttpResponseServerError(
            HTTP.INTERNAL_SERVER_ERROR,
            status=HTTP.STATUS.INTERNAL_SERVER_ERROR)


def site_mail(name: str, sender: str, message: str, recipients: list,
    # pylint: disable=too-many-arguments
    copy: bool, service: str,
    fails: bool = Switch.OFF) -> HttpResponse:
    """Builds and sends emailing messages to user and site contact

    :param name: The mail sender's name.
    :param sender: The mail sender's emailing.
    :param message: The mail message body.
    :param recipients: The mail recipients.
    :param copy: The copy flag.
    :param service: The mail service.
    :param fails: The fails flag.
    :returns: A `HttpResponse` object.
    :rtype: HttpResponse
    """
    if len(recipients) == 1 and recipients[0] == SITE_EMAIL:
        if copy:
            recipients.append(sender)
        message = sent_by(message, name)
        message = sender_cc(message, copy)
        pp_message(subject, recipients, sender, message, fail=fails)
        # Returns a HTTP Response (with message) if successful/not.
        return send_control(subject(Site.NAME, name),
            message,
            sender,
            recipients,
            service,
            fails)
        # pp_console(result, label='site_mail: send_control()')

    # pp_response(HTTP.MSG_FAILED, label='site_mail: send_control()')
    # Returns a HTTP Response (with message) when not successful/.
    return HttpResponse(HTTP.MSG_FAILED)


# noinspection PyUnusedFunction
def template_mail(template: str, sub_ject: str, sender: str, recipients: list,
    context: dict, fails: bool = Switch.OFF) -> int:
    """Sends templated emailing to user/site contact when they
    submit a contact form.
    :param template:
    :param sub_ject:
    :param sender:
    :param recipients:
    :param context:
    :param fails:
    :return: 0 - No email sent, 1 - email sent
    :rtype: int
    """
    ctx = {
        'subject':sub_ject,
        'sender':sender,
    }
    context |= ctx
    return templatemailer(template, context, sender, recipients, fails)


def send_control(sub_ject: str,
    message: str,
    sender: str,
    recipients: list,
    service: str,
    fails: bool = Switch.OFF) -> HttpResponse:
    """Send Control: Check emailing service and send mail.

    :param sub_ject: The mail subject.
    :param message: The mail message body.
    :param sender: The mail sender.
    :param recipients: The mail recipients.
    :param service: The mail service.
    :param fails: The fails flag.
    :return: A `HttpResponse` object.
    :rtype: HttpResponse
    """
    basic_service = env.str('BASIC_EMAIL', default=Services.BASIC)
    # Toggle between messaging services.
    if basic_service == service:
        smtp = get_connection(SMTP.BACKEND)
        # Checks if the emailing was sent.  # pylint: disable=fixme
        # pp_label('BASIC EMAIL')
        # pp_message(subject, recipients, sender, message, fail=fails,
        #            label='== send_control: message ==')
        if send_mail(subject, message, from_email=sender,
            recipient_list=recipients, fail_silently=fails,
            connection=smtp) == Sending.SUCCESS:
            # Returns a HTTP Response (with message) when successful.
            # pp_console(HTTP.MSG_SENT,
            #            label=f'send_control: send_mail() {HTTP.MSG_SENT}')
            return HttpResponse(HTTP.MSG_SENT)

        # Returns a HTTP Response (with message) when not successful/.
        # pp_console(HTTP.MSG_FAILED,
        #            label=f'send_control: {HTTP.MSG_FAILED}')
        return HttpResponse(HTTP.MSG_FAILED)

    # Returns a HTTP Response (with message) if successful/not.
    # pp_console(HTTP.MSG_SENT, label='send_control: any_mail()')
    return any_mail(sub_ject, sender, recipients, message, message)


# noinspection PyUnusedFunction
def send_default(subj, message,
    sender, recipients,
    copy=Switch.OFF, fail=Switch.OFF):
    """Sends emailing to user/site contact when they submit a contact form.

    :param subj:
    :param message:
    :param sender:
    :param recipients:
    :param copy:
    :param fail:
    :return: HTTP Response: Invalid header found.
    """
    # Send emailing & prevent header injection (Django Docs)
    if all([subject, message, sender, recipients]):
        try:
            # Determine the cc list based on whether the sender
            # wants a copy of the message
            cc_list = [sender] if copy else None

            # Build the Email and Reply-To is sender.
            email = EmailMessage(
                subject=subj,
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
            # pp_console(HTTP.INVALID_HEADER, label='send_default:
            # BadHeaderError')
            return HttpResponse(HTTP.INVALID_HEADER)
    else:
        # Missing required fields. No need to be more specific
        # (except if for debugging).
        # pp_console(HTTP.MSG_FAILED,
        #            label='send_default: Missing required fields')
        return HttpResponse(HTTP.MSG_FAILED)


def any_mail(subj, sender, recipients, text_content, name='',
    # pylint: disable=too-many-arguments
    html_content='', fail=Switch.OFF) -> HttpResponse:
    """Sends emailing to user/site contact when they submit a contact form.

    :param subj:
    :param sender:
    :param recipients:
    :param text_content:
    :param name: Nasm of sender: Optional
    :param html_content: HTML Content: Optional
    :param fail:
    :return: HTTP Response: Invalid header or Message Success/Fail.
    :rtype: HttpResponse
    """
    # Send emailing & prevent header injection (Django Docs)
    if all([subj, name, sender, recipients, text_content]):
        # Detect Header Injection, if cleaned, proceed/
        try:
            # Send the mail: Default Service | Failback service if provider
            # is not available. Admins adjust an enviromental string variable
            # to enable, as a application setting.
            # Following 12 Factor App Methodology.
            message = AnymailMessage(
                subject=subj,
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


# noinspection PyUnusedFunction
def templated_contact(subj, name, sender, recipients,
    text_content, fail=Switch.OFF):
    """Sends emailing to user/site contact when they submit a contact form.

    :param subj: Default.
    :param name: Contact Form: id=contact-name-id, Sender's Full Name
    :param sender: Contact Form: id=contact-emailing, Senders Email
    :param recipients: SITE_EMAIL, sender cc'd if copy flag is set.
    :param text_content: Contact Form: id=contact-message.
    :param fail: bool: Fail silently flag.
    :return: HTTP Response: Invalid header found.
    """
    # Send emailing & prevent header injection (Django Docs)
    # if subject and sender and recipients and text_content and html_content:
    if all([subject, name, sender, recipients, text_content]):
        try:
            # Send the mail: Default Service | Failback service if provider
            # is not available. Admins adjust an enviromental string
            # variable to enable, as a application setting. Following 12
            # Factor App Methodology.
            message = TemplatedMessage()
            message.template_name = Template.CONTACT_EMAIL
            message.context = {
                Template.SUBJECT:subj,
                Template.NAME:name,
                Template.PLAIN:text_content,
                Template.HTML:text_content,
                Template.SITE:Site.NAME,
                Template.URL:Site.URL,
                Template.SENTON:get_date(),
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
