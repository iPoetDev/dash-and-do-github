

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
    BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

class HTTP:
    """
    HTTP Messages
    """
    INVALID_HEADER = 'Invalid header found.'
    MSG_SENT = 'Message Sent'
    MSG_FAILED = 'Message Failed'

class Sending:
    """
    Sending Status
    """
    SUCCESS = 0
    FAIL = 1

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
    NAME = 'name'
    EMAIL = 'email'
    MESSAGE = 'message'
    COPY = 'copySent'
    SUBJECT = 'subject'

class Switch:
    """
    Switches
    """
    OFF = False
    ON = True

class Template:
    """
    Template Paths
    """
    CONTACT_EMAIL = 'email/contact.tpl'
    SUBJECT = 'subject'
    NAME = 'senders_name'
    PLAIN = 'body_message'
    HTML = 'html_message'
    SITE = 'site_name'
    URL = 'site_url'
    SENTON = 'datatime'
