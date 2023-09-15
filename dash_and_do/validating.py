#!/user/bin/env python3
"""
    @File: validating.py
    @Version: 0.3.0 to 0.3.0.?
    @Desc: common | dash_and_do |  validating. helpers functions
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/08/07
    @Date Modified: 23/09/12
    @Python Version: 3.11.04
    @Django Version: 4.2.3
    @Notes / Ideas v Implement:
        - Helper Functions for HTMX
        - Standalone helpers for HTMX
        - Model to add middleware implementations for HTMX
    @Changelog:
    - Added:
        - 23/09/12: Added docstrings
        - 23/09/12: Created initial file
        - 23/09/12: added Common Email Functionalities
    - Updated:
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

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def valid_name(value):
    """
    Validates name field.
    :param value:
    :return:
    :raise: ValidationError: Invalid Name: 6 to 50 alphanumeric characters only for international names
    """
    name_validator = RegexValidator(r'^[a-zA-ZÀ-ÖØ-öø-ÿ \'-]{6,50}$',
                                    'Invalid Name')
    try:
        name_validator(value)
    except ValidationError:
        raise ValidationError("Invalid Name: 6 to 50 alphanumeric characters"
                              "only, for international names")


def valid_email(value):
    """
    Validates email field.
    :param value:
    :return:
    :raise: ValidationError: Invalid Email: Email should match common email forms, and . - _
    """
    email_validator = RegexValidator(
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+.{8,50}$',
        'Invalid Email')
    try:
        email_validator(value)
    except ValidationError:
        raise ValidationError(
            "Invalid Email: Email should match common email forms, and . - _")
