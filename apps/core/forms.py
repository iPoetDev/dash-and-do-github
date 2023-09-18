#!/user/bin/env python3
"""
    @File: forms.py
    @Version: 0.3.0 to 0.3.0.?
    @Desc: apps | core |  forms
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
from django import forms
from django.forms import ModelForm
from .models import Contact
from dash_and_do.validating import valid_name, valid_email

class ContactAttrs:
    """"
    Contact Form Attributes Values
    """
    FULL_NAME = 'Full Name'
    NAME_LABEL = 'name'
    NAME_HELP = 'A full name will be alphebetical characters only, - / \' '
    VALID_RANGE = '. min 8, max 50'
    NAME_REQ = 'Please enter your full name.'
    EMAIL = 'Email'
    EMAIL_LABEL = 'email'
    EMAIL_HELP = 'A valid email address is required with the: - / . / _ / '
    EMAIL_REQ = 'Please enter your email address.'
    AUTO_OFF = 'OFF'
    MIN = '8'
    MAX = '50'
    AREA = 'Message'
    AREA_MIN = '10'
    AREA_MAX = '350'
    AREA_RANGE = '. min 10, max 350'
    AREA_HELP = 'Compose your message here.'
    AREA_REQ = 'Please enter your message.'
    AREA_ROWS = '60'
    AREA_COLS = '50'
    SPELLON= 'True'
    INVALID = 'is not valid.'
    EMPTY = 'cannot be empty.'
    MSG_EMPTY = 'We need a message to send.'
    VIEW_ALL = 'all'
    VIEW_PUBLIC = 'public'
    VIEW_PRIVATE = 'private'
    COPY_NAME = 'copy-sent'
    COPY_SENT = 'Send me a copy'

class ContactForm(ModelForm):
    """
    Form for creating or updating a contact, for use with widget_tweeks.

    :attribute  META inner class
    :constant FIELD_ALIASES: The aliases for the fields.
    :method clean: Cleans the form data.
    :property  name: The name of the contact.
    :property  email: The email of the contact.
    :property  message: The message of the contact.
    :property  copySent: Whether to send a copy of the message to the sender.
    """

    class Meta:
        """
         ContactForm's Meta
        :model: Contact: The model to use for the form.
        :field: name: The name of the contact.
        :field: email: The email of the contact.
        :field: message: The message of the contact.
        :field: copySent: Whether to send a copy of the message to the sender.
        """
        model = Contact
        fields = ['name', 'email', 'message', 'copy_sent']

    FIELD_ALIASES = {
        'name': 'contact-fullname',
        'email': 'contact-email',
        'message': 'contact-message',
        # Optional fields
        'copy_sent': 'copy-sent',
    }

    # Define form fields with custom widget names/attrs
    # contact-fullname name Strip is true, empty value is default.
    name = forms.CharField(
        label=ContactAttrs.FULL_NAME,
        initial=ContactAttrs.FULL_NAME, # placeholder text, hidden: css
        required=True,
        min_length=int(ContactAttrs.MIN),
        max_length=int(ContactAttrs.MAX),
        widget=forms.TextInput(
            attrs={
                'name': FIELD_ALIASES['name'],
                'id': FIELD_ALIASES['name'],
                'automcomplete': ContactAttrs.AUTO_OFF,
                'minlength': ContactAttrs.MIN,
                'maxlength': ContactAttrs.MAX,
                'data-view': ContactAttrs.VIEW_ALL,
            }
        ),
        help_text=ContactAttrs.NAME_HELP + ContactAttrs.VALID_RANGE,
        validators=[valid_name],
        error_messages={
            'required': ContactAttrs.NAME_REQ,
            'invalid': f'The {ContactAttrs.NAME_LABEL} {ContactAttrs.INVALID}',
            'empty': f'The {ContactAttrs.NAME_LABEL} {ContactAttrs.EMPTY}',
            'min_length': f'The {ContactAttrs.NAME_LABEL} must more than {ContactAttrs.MIN}.',
            'max_length': f'The {ContactAttrs.NAME_LABEL} must be less than {ContactAttrs.MAX}.',
        }
    )
    # contact-email email Strip is true, empty value is default.
    email = forms.EmailField(
        label=ContactAttrs.EMAIL,
        initial=ContactAttrs.EMAIL, # placeholder text, hidden: css
        required=True,
        min_length=int(ContactAttrs.MIN),
        max_length=int(ContactAttrs.MAX),
        widget=forms.EmailInput(
            attrs={
                'name': FIELD_ALIASES['email'],
                'id': FIELD_ALIASES['email'],
                'automcomplete': ContactAttrs.AUTO_OFF,
                'minlength': ContactAttrs.MIN,
                'maxlength': ContactAttrs.MAX,
                'data-view': ContactAttrs.VIEW_ALL,
            }
        ),
        help_text=ContactAttrs.EMAIL_HELP + ContactAttrs.VALID_RANGE,
        validators=[valid_email],
        error_messages={
            'required': ContactAttrs.EMAIL_REQ,
            'invalid': f'The {ContactAttrs.EMAIL_LABEL} {ContactAttrs.INVALID}',
            'empty': f'The {ContactAttrs.EMAIL_LABEL} {ContactAttrs.EMPTY}',
            'min_length': f'The {ContactAttrs.EMAIL_LABEL} must more than {ContactAttrs.MIN}.',
            'max_length': f'The {ContactAttrs.EMAIL_LABEL}must be less than {ContactAttrs.MAX}.',
        }
    )
    # contact-message textarea Strip is true, empty value is default.
    message = forms.CharField(
        label=ContactAttrs.AREA,
        initial=ContactAttrs.AREA, # placeholder text, hidden: css
        required=True,
        min_length=int(ContactAttrs.AREA_MIN),
        max_length=int(ContactAttrs.AREA_MAX),
        widget=forms.Textarea(
            attrs={
                'name': FIELD_ALIASES['message'],
                'id': FIELD_ALIASES['message'],
                'minlength': ContactAttrs.AREA_MIN,
                'maxlength': ContactAttrs.AREA_MAX,
                'data-view': ContactAttrs.VIEW_ALL,
                'cols': ContactAttrs.AREA_COLS,
                'rows': ContactAttrs.AREA_ROWS,
                'spellcheck': ContactAttrs.SPELLON,
                'title': ContactAttrs.AREA_HELP + ContactAttrs.AREA_RANGE,
            },
        ),
        help_text='Compose your message here.',
        error_messages={
            'empty': ContactAttrs.MSG_EMPTY,
            'min_length': f'You have add more than {ContactAttrs.AREA_MIN} '
                          f'for a message.',
            'max_length': f'You have exceeded the max of'
                          f' {ContactAttrs.AREA_MAX}.'
        }
    )
    # copy-sent checkbox
    copy_sent = forms.BooleanField(
        label=ContactAttrs.COPY_SENT,
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': FIELD_ALIASES['copy_sent']
            }
        ),
        help_text=ContactAttrs.COPY_SENT,
    )
