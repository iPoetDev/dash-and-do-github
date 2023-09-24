#!/user/bin/env python3
# OopCompanion:suppressRename
"""
    @File: modelvalues.py
    @Version: 0.3.0 to 0.3.0.?
    @Desc: apps | <app> |  <module>
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/09/?
    @Date Modified: 23/09/??
    @Python Version: 3.11.04
    @Django Version: 4.2.3/.04/.05
    @Notes / Ideas v Implement:
        - .
    @Changelog:
    - Added:
        - added: Created initial file: 23/09/??:
    - Updated:
        - updated:
    @Plan:
        - TODO:
        - FIXME:
        - CHECK:
"""


class Forms:
    """
    Core Form Names
    """
    GENERIC = 'form'
    CONTACT = 'contact_form'
    LOGIN = 'login_form'
    SIGNUP = 'signup_form'
    PASSWORD_RESET = 'password_reset_form'
    PASSWORD_CHANGE = 'password_change_form'
    PROFILE = 'profile_form'
    GITHUB = 'github_form'
    SETTINGS = 'settings_form'


class ContactFields:
    """
    Contact Form Fields
    """
    CONTACT_NAME = 'contact_name'
    CONTACT_EMAIL = 'contact_email'
    CONTACT_MESSAGE = 'contact_message'
    CONTACT_COPY = 'copy_sent'


class ContactAttrs:
    """"
    Contact Form Attributes Values
    """
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
