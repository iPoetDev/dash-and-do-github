#  Copyright (c) 2023.



# OopCompanion:suppressRename

class Site:
    """
    Site name and URL
    """
    NAME = 'Dash and Do: A Personal GitHub Portfolio Manager'
    URL = 'https://dash-and-do.herokuapp.com/'


class Services:
    """
    Service Options
    """
    BASIC = 'send_mail'
    CUSTOM = 'any_mail'


class SMTP:
    """
    SMTP Settings
    """
    BACKEND = 'django.core.mail.backends.console.EmailBackend'


class HTTP:
    """
    HTTP Messages
    """
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

    class STATUS:
        """
        HTTP Status Codes
        """
        OK = 200
        BAD_REQUEST = 400
        NOT_FOUND = 404
        INTERNAL_SERVER_ERROR = 500
        SERVICE_UNAVAILABLE = 503
        GATEWAY_TIMEOUT = 504

    class EMAILERRORS:
        """
        Email Status Codes
        """
        SERVICE_UNAVAILABLE = \
            'Service Unavailable: Email service is currently unavailable'
        GATEWAY_TIMEOUT = \
            'Gateway Timeout: Email service is currently unavailable'
        UNKNOWN_ERROR = \
            'Unknown Error: Email service is currently unavailable'

class Sending:
    """
    Sending Status
    """
    SUCCESS = 1
    FAIL = 0


class MIME:
    """
    MIME Types
    """
    PLAIN = 'text/plain'
    HTML = 'text/html'


class Field:
    """
    Form Fields
    """
    NAME = 'contact_name'
    EMAIL = 'contact_email'
    MESSAGE = 'contact_message'
    COPY = 'copy_sent'
    SUBJECT = 'subject'


class Switch:
    """
    Switches
    """
    OFF = False
    ON = True
    SHOW = False
    HIDE = True


class Template:
    """
    Template Paths
    """
    CONTACT_EMAIL = 'emailing/contact.tpl'
    SUBJECT = 'subject'
    NAME = 'senders_name'
    PLAIN = 'body_message'
    HTML = 'html_message'
    SITE = 'site_name'
    URL = 'site_url'
    SENTON = 'datatime'
