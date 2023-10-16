#!/user/bin/env python3
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

#  Copyright (c) 2023.

# Django
from django import forms
from django.forms import ModelForm

# Local
from apps.kore.models import Contacts
from apps.kore.modelsvalues import ContactAttrs
from apps.kore.modelsvalues import ContactFields
from apps.kore.modelsvalues import Forms

# OopCompanion:suppressRename

contactattrs = ContactAttrs()
contactfields = ContactFields()


class ContactForm(ModelForm):
    """Form for creating or updating a contact.

    :attribute  META inner class :constant FIELD_ALIASES: The aliases
    for the fields. :method clean: Cleans the form data. :property
    name: The name of the contact. :property  emailing: The emailing of
    the contact. :property  message: The message of the contact.
    :property  copySent: Whether to send a copy of the message to the
    sender.
    """

    def __init__(self, *args, **kwargs):
        """Initialise the form.

        :param self:
        :param args:
        :param kwargs: :property label: The label for the form.
        """
        super().__init__(*args, **kwargs)
        self.label = Forms.CONTACT

    class Meta:  # pylint: disable=too-few-public-methods
        """ContactForm's Meta."""
        model = Contacts
        fields = [
            ContactFields.CONTACT_NAME,
            ContactFields.CONTACT_EMAIL,
            ContactFields.CONTACT_MESSAGE,
            ContactFields.CONTACT_COPY]

    # Define form fields with custom widget names/attrs
    # contact-fullname name Strip is true, empty value is default.
    name = forms.CharField(
        label=contactattrs.FULL_NAME,
        initial=contactattrs.FULL_NAME,  # placeholder text, hidden: css
        required=contactattrs.REQUIRED,
        min_length=int(contactattrs.MIN),
        max_length=int(contactattrs.MAX),
        widget=forms.TextInput(
            attrs={
                'name':ContactFields.CONTACT_NAME,
                'id':ContactFields.CONTACT_NAME,
                'autocomplete':contactattrs.AUTO_OFF,
                'minlength':contactattrs.MIN,
                # 'maxlength': contactattrs.MAX,
                'data_view':contactattrs.VIEW_ALL,
                # 'pattern': contactattrs.NAME_PATTERN,
                'tabindex':'6',
            }
        ),
        help_text=contactattrs.NAME_HELP + \
                  contactattrs.VALID_RANGE,
        # validators=[valid_name],
        error_messages={
            'required':contactattrs.NAME_REQ,
            'invalid':f'The {contactattrs.NAME_LABEL} '
                      f'{contactattrs.INVALID}',
            'empty':f'The {contactattrs.NAME_LABEL} '
                    f'{contactattrs.EMPTY}',
            'min_length':f'The {contactattrs.NAME_LABEL} '
                         f'must more than {contactattrs.MIN}.',
            'max_length':f'The {contactattrs.NAME_LABEL} '
                         f'must be less than {contactattrs.MAX}.',
        }
    )

    # contact-emailing emailing Strip is true, empty value is default.
    email = forms.EmailField(
        label=contactattrs.EMAIL,
        initial=contactattrs.EMAIL,  # placeholder text, hidden: css
        required=contactattrs.REQUIRED,
        min_length=int(contactattrs.MIN),
        max_length=int(contactattrs.MAX),
        widget=forms.EmailInput(
            attrs={
                'name':ContactFields.CONTACT_EMAIL,
                'id':ContactFields.CONTACT_EMAIL,
                'autocomplete':contactattrs.AUTO_OFF,
                'minlength':contactattrs.MIN,
                # 'maxlength': contactattrs.MAX,
                'data_view':contactattrs.VIEW_ALL,
                # 'pattern': contactattrs.EMAIL_PATTERN,
                'tabindex':'6'
            }
        ),
        help_text=contactattrs.EMAIL_HELP + contactattrs.VALID_RANGE,
        # validators=[valid_email],
        error_messages={
            'required':contactattrs.EMAIL_REQ,
            'invalid':f'The {contactattrs.EMAIL_LABEL}'
                      f' {contactattrs.INVALID}',
            'empty':f'The {contactattrs.EMAIL_LABEL} '
                    f'{contactattrs.EMPTY}',
            'min_length':f'The {contactattrs.EMAIL_LABEL} '
                         f'must more than {contactattrs.MIN}.',
            'max_length':f'The {contactattrs.EMAIL_LABEL}'
                         f'must be less than {contactattrs.MAX}.',
        }
    )

    # contact-message textarea Strip is true, empty value is default.
    message = forms.CharField(
        label=contactattrs.AREA,
        initial=contactattrs.AREA,  # placeholder text, hidden: css
        required=contactattrs.REQUIRED,
        min_length=int(contactattrs.AREA_MIN),
        max_length=int(contactattrs.AREA_MAX),
        widget=forms.Textarea(
            attrs={
                'name':ContactFields.CONTACT_MESSAGE,
                'id':ContactFields.CONTACT_MESSAGE,
                'minlength':contactattrs.AREA_MIN,
                # 'maxlength': contactattrs.AREA_MAX,
                'data-view':contactattrs.VIEW_ALL,
                'cols':contactattrs.AREA_COLS,
                'rows':contactattrs.AREA_ROWS,
                'spell':contactattrs.SPELLON,
                'title':contactattrs.AREA_HELP + \
                        contactattrs.AREA_RANGE,
                'tabindex':'6',
            },
        ),
        help_text='Compose your message here.',
        error_messages={
            'empty':contactattrs.MSG_EMPTY,
            'min_length':'You have add more than '
                         f'{contactattrs.AREA_MIN} '
                         'for a message.',
            'max_length':'You have exceeded the max of'
                         f' {contactattrs.AREA_MAX}.'
        }
    )

    # copy-sent checkbox
    copy_sent = forms.BooleanField(
        label=contactattrs.COPY_SENT,
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name':ContactFields.CONTACT_COPY,
            }
        ),
        help_text=contactattrs.COPY_SENT,
    )
