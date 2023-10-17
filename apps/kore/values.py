#!/user/bin/env python3
# OopCompanion:suppressRename
"""@File: forms.py
@Version: 0.3.0 to 0.3.0.?
@Desc: apps | kore |  forms
@Author: Charles Fowler
@Copyright: 2023
@Date Created: 23/08/07
@Date Modified: 23/09/17
@Python Version: 3.11.04
@Django Version: 4.2.3
@Notes / Ideas v Implement:
- Customising for widgets tweeks, individual fields rendering.
@Changelog:
- Added:
- added: Created initial file: 23/08/07:
- added: Contact ModelForms: 23/08/07:
- added: docstrings: 23/09/12:
- Updated:
- updated: Per Field (Char/Email/Textarea) attributes (23/09/17)
- updated: Per Widget attribute: Name, Email attrs (23/09/17)
- updated: ClassAttrs strings values (23/09/17)
- updated: Validators: Name, Email (23/09/17)
- updated: Error Messages: Required, Invalid, Mix/Max Length (23/09/17)
@Plan:
- TODO:
- Create test cases for models.
- Define Test Scenarios
- Happy Path
- Edge Cases
- Other
"""
# Django Imports
from django.contrib import messages


class HTTP:  # pylint: disable=too-few-public-methods
    """HTTP Methods."""
    GET = 'GET'
    POST = 'POST'

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

    class MESSAGES:
        """HTTP Status Messages."""
        NOT_FOUND = 'Page Not Found: Core: 404 Error'


class Template:  # pylint: disable=too-few-public-methods
    """Template Paths."""
    HOME = 'index.html'
    ABOUT = 'about.html'
    VERIFY = 'verify.html'
    CONFIRM = 'kore/confirm.html'
    CONTACT = './forms/form_contact.html'
    MENU_PUBLIC = 'menu_public.html'
    COREPAGE_NOT_FOUND = 'kore/404.html'

    class Form:  # pylint: disable=too-few-public-methods
        """Form Templates.

        # noqa: S105: No password or reset , just config value
        """
        GENERIC = 'forms/form_generic.html'
        CONTACT = 'forms/form_contact.html'
        LOGIN = 'forms/form_login.html'
        SIGNUP = 'forms/form_signup.html'
        PASSWORD_RESET = 'forms/form_password_reset.html'  # noqa: S105
        PASSWORD_CHANGE = 'forms/form_password_change.html'  # noqa: S105
        PROFILE = 'forms/form_profile.html'
        GITHUB = 'forms/form_github.html'
        SETTINGS = 'forms/form_settings.html'


class Forms:  # pylint: disable=too-few-public-methods
    """Core Form Names.

    # noqa: S105: No password or reset , just config value
    """
    GENERIC = 'form'
    CONTACT = 'contact_form'
    LOGIN = 'login_form'
    SIGNUP = 'signup_form'
    PASSWORD_RESET = 'password_reset_form'  # noqa: S105
    PASSWORD_CHANGE = 'password_change_form'  # noqa: S105
    PROFILE = 'profile_form'
    GITHUB = 'github_form'
    SETTINGS = 'settings_form'


class Ctx:  # pylint: disable=too-few-public-methods
    """Context Variables.

    # noqa: S105: No password or reset , just config value
    """
    GENERIC_FORM = 'form'
    CONTACT_FORM = 'contact'
    LOGIN_FORM = 'login'
    SIGNUP_FORM = 'signup'
    PASSWORD_RESET_FORM = 'password_reset'  # noqa: S105
    PASSWORD_CHANGE_FORM = 'password_change'  # noqa: S105
    PROFILE_FORM = 'profile'
    GITHUB_FORM = 'github'
    SETTINGS_FORM = 'settings'


class SiteMeta:  # pylint: disable=too-few-public-methods
    """Site Meta Data TITLE = 'title' URL = 'url' PERSON = 'person' DESCRIPTION
    = 'description' KEYWORDS = 'keywords' CONTACT = 'contact'."""
    NAME = 'Dashboard and Do GitHub Manager'
    URL = 'https://dash-and-do.herokuapp.com/'
    PERSON = 'Charles J Fowler, @iPoetDev.github.com'
    DESC = 'A GitHub Portfolio Manager for the Dashboard and Do '
    COPY = ('The Dash and Document GitHub is the '
            'copyright of Charles J Fowler, 2023-2028')
    KEYWORDS = 'GitHub, Portfolio, Manager, Dashboard, Do, '
    CONTACT = 'Github: @iPoetDev'


class Brand:  # pylint: disable=too-few-public-methods
    """Brand Names."""

    class Site:  # pylint: disable=too-few-public-methods
        """Site Brand Names."""
        NAME = 'Dashboard and Do GitHub Manager'
        SHORT_NAME = 'Dash and Do'
        LOGO = 'dash_and_do/logo.png'
        LOGO_ALT = 'Dash and Do Logo'
        LOGO_TITLE = 'Dash and Do Logo'
        FAVICON = 'dash_and_do/favicon.ico'
        FAVICON_ALT = 'Dash and Do Favicon'
        FAVICON_TITLE = 'Dash and Do Favicon'

    class FAVICON:
        """Favicon Configuration."""
        XMLNS = 'http://www.w3.org/2000/svg'
        VBOX = '0 0 100 100'
        VIEWY = '.9em'
        FONTSIZE = '90'
        ICON = '🦊'
        FORMAT = 'image/svg+xml'


class Page:  # pylint: disable=too-few-public-methods
    """Page Titles."""

    class Index:  # pylint: disable=too-few-public-methods
        """Index Page Details."""
        USE = 'all'
        TITLE = 'Home: Dashboard and Do GitHub Manager'
        ATITLE = 'Home: Dashboard and Do GitHub Manager'
        ATEXT = 'Home'

    class About:  # pylint: disable=too-few-public-methods
        """About Page Details | Static."""
        USE = 'menu_public'
        TITLE = 'About: Dashboard and Do GitHub Manager'
        ATITLE = 'About: Dashboard and Do GitHub Manager'
        ATEXT = 'About'

    class Verify:  # pylint: disable=too-few-public-methods
        """About Page Details | Static."""
        USE = 'services_public'
        IA = 'orphan'
        NAV = 'excluded'
        ROLE = 'services'
        FLOW = 'signup -> email_confirm -> verify -> index -> login'
        DESC: str = 'user confirmations and verification statuses'
        TITLE = 'Verify: Dashboard and Do GitHub Manager'
        ATITLE = 'Verify: Dashboard and Do GitHub Manager'
        ATEXT = 'Verify'

    class Contact:  # pylint: disable=too-few-public-methods
        """Contact Section Partial/Fragment Details."""
        USE = 'menu_public'
        TITLE = 'Contact: Dashboard and Do GitHub Manager'
        ATITLE = 'Contact Us: Send an Message to Dash and Do'
        ATEXT = 'Contact'

    class AccountMenu:  # pylint: disable=too-few-public-methods
        """Account Menu Details."""
        USE = 'menu_private'
        MENU_TITLE = 'Accounts Menu'
        ACCOUNT_BUTTEXT = 'Account'
        PROFILE_ATITLE = 'Accounts: View your account profile'
        PROFILE_ATEXT = 'Profile'
        GITHUB_ATITLE = 'GitHub: Connect GitHub to your profile'
        GITHUB_ATEXT = 'Connect'
        SETTINGS_ATITLE = 'Settings: Manwge your profile'
        SETTINGS_ATEXT = 'Settings'
        LOGOUT_ATITLE = 'Logout: Sign Out of your profile'
        LOGOUT_ATEXT = 'Logout'


class Feedback:  # pylint: disable=too-few-public-methods
    """Feedback Messages."""
    EMAILSUCCESS = 'Your message has been sent.'
    BADREQUEST = 'Bad request, please verify your message and try again.'
    SERVERERROR = 'Server error, your message could not be sent.'
    EMAILERROR = 'An error occurred, your message could not be sent.'


class Signal:  # pylint: disable=too-few-public-methods
    """Message Levels."""
    INFO = 'info'
    SUCCESS = 'success'
    ERROR = 'error'
    FAIL = False

    class MSG:  # pylint: disable=too-few-public-methods
        """Message Levels."""
        DEBUG = messages.DEBUG
        INFO = messages.INFO
        SUCCESS = messages.SUCCESS
        WARNING = messages.WARNING
        ERROR = messages.ERROR
        FAIL = False


class Log:  # pylint: disable=too-few-public-methods
    """Log Messages."""
    INDEX = 'Index'
    CONTACT_FORM = 'Contact Form'
    MENU_PUBLIC = 'Public Menu'

    class Desc:  # pylint: disable=too-few-public-methods
        """Log Descriptions."""
        COMPLETED_FORM = 'Completed Form: Valid & POST'
        BOUNDED_FORM = 'Bounded: Invalid Form & POST'
        UNBOUND_FORM = 'Unbounded: Empty Form: Method != POST'


class ContactFields:  # pylint: disable=too-few-public-methods
    """Contact Form Fields."""
    CONTACT_NAME = 'contact_name'
    CONTACT_EMAIL = 'contact_email'
    CONTACT_MESSAGE = 'contact_message'
    CONTACT_COPY = 'copy_sent'


class ContactAttrs:  # pylint: disable=too-few-public-methods
    """" Contact Form Attributes Values."""
    FULL_NAME = 'Full Name'
    NAME_LABEL = 'name'
    NAME_HELP = 'A full name will be alphebetical characters only, - / \' '
    VALID_RANGE = '. min 8, max 50'
    NAME_REQ = 'Please enter your full name.'
    NAME_PATTERN = r'^[a-zA-ZÀ-ÖØ-öø-ÿ \'-]{8,50}$'
    EMAIL = 'Email'
    EMAIL_LABEL = 'emailing'
    EMAIL_HELP = 'A valid emailing address is required with the: - / . / _ / '
    EMAIL_REQ = 'Please enter your emailing address.'
    EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    AUTO_OFF = 'on'
    MIN = '8'
    MAX = '50'
    AREA = 'Message'
    AREA_MIN = '10'
    AREA_MAX = '350'
    AREA_RANGE = '. min 10, max 350'
    AREA_HELP = 'Compose your message here.'
    AREA_REQ = 'Please enter your message.'
    AREA_ROWS = 60
    AREA_COLS = 50
    SPELLON = 'True'
    INVALID = 'is not valid.'
    EMPTY = 'cannot be empty.'
    MSG_EMPTY = 'We need a message to send.'
    TAB = '6'
    VIEW_ALL = 'all'
    VIEW_PUBLIC = 'public'
    VIEW_PRIVATE = 'private'
    COPY_NAME = 'copy-sent'
    COPY_SENT = 'Send me a copy'
    REQUIRED = False
