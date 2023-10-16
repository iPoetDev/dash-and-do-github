#!/user/bin/env python3
"""@File: values.py
@Version: 0.3.0 to 0.3.1: Email Values
@Desc: apps | kore |  emailing | values: Email Constants
@Author: Charles Fowler
@Copyright: 2023
@Date Created: 23/09/12
@Date Modified: 23/09/13
@Python Version: 3.11.04
@Django Version: 4.2.3
@Notes / Ideas v Implement:
    -
@Changelog:
"""
# OopCompanion:suppressRename

class Site:  # pylint: disable=too-few-public-methods
    """Site name and URL."""
    NAME = 'Dash and Do: A Personal GitHub Portfolio Manager'
    URL = 'https://dash-and-do.herokuapp.com/'



class Services:  # pylint: disable=too-few-public-methods
    """Service Options."""
    BASIC = 'send_mail'
    CUSTOM = 'any_mail'


class SMTP:  # pylint: disable=too-few-public-methods
    """SMTP Settings."""
    BACKEND = 'django.core.mail.backends.console.EmailBackend'


class HTTP:  # pylint: disable=too-few-public-methods
    """HTTP Messages."""
    INVALID_HEADER = 'Invalid header found.'
    BAD_REQUEST = 'Bad Request'
    BAD_REQUEST_MSG = 'Bad Reuqest: Message Failed'
    MSG_SENT = 'Message Sent'
    MSG_FAILED = 'Message Failed'
    NOT_FOUND = 'Not Found'
    INTERNAL_SERVER_ERROR = 'Internal Server Error'
    SERVICE_UNAVAILABLE = 'Service Unavailable'
    GATEWAY_TIMEOUT = 'Gateway Timeout'
    UNKNOW_ERROR = 'Unknown Error'
    REDIRECT_URL_PATH = '/'

    class STATUS:  # pylint: disable=too-few-public-methods
        """HTTP Status Codes."""
        OK = 200
        BAD_REQUEST = 400
        FORBIDDEN = 403
        NOT_FOUND = 404
        METHOD_NOT_ALLOWED = 405
        GONE = 410
        INTERNAL_SERVER_ERROR = 500
        SERVICE_UNAVAILABLE = 503
        GATEWAY_TIMEOUT = 504

    class EMAILERRORS:  # pylint: disable=too-few-public-methods
        """Email Status Codes."""
        SERVICE_UNAVAILABLE = \
            'Service Unavailable: Email service is currently unavailable'
        GATEWAY_TIMEOUT = \
            'Gateway Timeout: Email service is currently unavailable'
        UNKNOWN_ERROR = \
            'Unknown Error: Email service is currently unavailable'


class Sending:  # pylint: disable=too-few-public-methods
    """Sending Status."""
    SUCCESS = 1
    FAIL = 0


class MIME:  # pylint: disable=too-few-public-methods
    """MIME Types."""
    PLAIN = 'text/plain'
    HTML = 'text/html'


class Field:  # pylint: disable=too-few-public-methods
    """Form Fields."""
    NAME = 'contact_name'
    EMAIL = 'contact_email'
    MESSAGE = 'contact_message'
    COPY = 'copy_sent'
    SUBJECT = 'subject'


class Switch:  # pylint: disable=too-few-public-methods
    """Switches."""
    OFF = False
    ON = True
    SHOW = False
    HIDE = True


class Template:  # pylint: disable=too-few-public-methods
    """Template Paths."""
    CONTACT_EMAIL = 'emailing/contact.tpl'
    SUBJECT = 'subject'
    NAME = 'senders_name'
    PLAIN = 'body_message'
    HTML = 'html_message'
    SITE = 'site_name'
    URL = 'site_url'
    SENTON = 'datatime'
