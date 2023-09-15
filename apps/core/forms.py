#!/user/bin/env python3
"""
    @File: forms.py
    @Version: 0.3.0 to 0.3.0.?
    @Desc: apps | core |  forms
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/08/07
    @Date Modified: 23/09/12
    @Python Version: 3.11.04
    @Django Version: 4.2.3
    @Notes / Ideas v Implement:
    @Changelog:
    - Added:
        - 23/08/07: Created initial file
        - 23/09/12: added Contact ModelForms
    - Updated:
        - 23/09/12: Added docstrings
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
from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    """
    Form for creating or updating a contact.

    :constant FIELD_ALIASES: The aliases for the fields.
    :method clean: Cleans the form data.
    :attribute  META

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
        fields = ['name', 'email', 'message', 'copySent']

    FIELD_ALIASES = {
        'name': 'contact-fullname',
        'email': 'contact-email',
        'message': 'contact-message',
        # Optional fields
        'copy_sent': 'copy-sent',
    }

    # Define form fields with custom widget names
    name = forms.CharField(widget=forms.TextInput(attrs={'name': FIELD_ALIASES['name']}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name': FIELD_ALIASES['email']}))
    message = forms.CharField(widget=forms.Textarea(attrs={'name': FIELD_ALIASES['message']}))
    copy_sent = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'name': FIELD_ALIASES['copy_sent']}))
