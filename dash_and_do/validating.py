#!/user/bin/env python3
"""@File: validating.py
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
        - Add docstrings to all classes, and methods
        - Add Constants for all strings for Validation
        - Added Validationfor Email, Name, Password
    - FIXME:
    - CHECK:
        - DONE: PyLint: 2023-09-30
    - NOTE:
"""

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class Validation:  # pylint: disable=too-few-public-methods
    """Validation Constants

    Validation class for common validation functions.
    """

    class PATTERNS:  # pylint: disable=too-few-public-methods
        """Patterns for validation.

        Regex patterns for validation.
        :NAME: 6 to 50 alphanumeric characters only, for international names
        :EMAIL: Email should match common emailing forms, and . - _
        """
        NAME = r'^[a-zA-ZÀ-ÖØ-öø-ÿ \'-]{6,50}$'
        EMAIL = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+.{8,50}$'
        PASSWORD = {  # Regular expressions for password validation components
            'LENGTH': r'^\S{12,50}$',
            'UPPER': r'[A-Z]',
            'LOWER': r'[a-z]',
            'DIGITS': r'\d',
            'SYMBOLS': r'[@$!%*#?&]'
        }

    class MESSAGES:  # pylint: disable=too-few-public-methods
        """Short Messages for validation.

        Validation messages for validation.
        :param: NAME: str: Invalid Name
        :param: EMAIL: str: Invalid Email
        :param: PASSWORD: dict: Invalid Password
        """
        NAME = 'Invalid Name'
        EMAIL = 'Invalid Email'
        PASSWORD = {
            'LENGTH': 'Have 12 and 50 characters.',
            'UPPER': 'At least 1 uppercase letter.',
            'LOWER': 'At least 1 lowercase letter.',
            'DIGITS': 'At least 1 digit required.',
            'SYMBOLS': 'Missing a symbol: @$!%*#?&',
        }

    class LENGTHS:  # pylint: disable=too-few-public-methods
        """Lengths for validation.

        Validation lengths settings for validation of various fields.
        """
        MIN_NAME = 6
        MAX_NAME = 50
        MIN_EMAIL = 8
        MAX_EMAIL = 50
        MAX_PASS = 50
        MIN_PASS = 12

    class ERRORS:  # pylint: disable=too-few-public-methods
        """Error messages for validation.

        Validation errors for validation.
        :NAME: Invalid Name: 6 to 50 alphanumeric characters only, for
        international names
        :EMAIL: Invalid Email: Email should match common emailing forms,
        and . - _
        """
        NAME = 'Invalid Name: 6 to 50 alphanumeric characters only, for ' \
               'international names'
        EMAIL = 'Invalid Email: Email should match common emailing forms, ' \
                'and . - _'
        PASSWORD = {
            'LENGTH': 'Password must be between 12 and 50 characters.',
            'UPPER': 'Password must contain at least 1 uppercase letter.',
            'LOWER': 'Password must contain at least 1 lowercase letter.',
            'DIGITS': 'Password must contain at least 1 digit.',
            'SYMBOLS': 'Password must contain at least 1 symbol: @$!%*#?&'
        }


def valid_name(value) -> None:
    """Validate Name / Username

    :param value: The name value to be validated.
    :return: None
    :raises: ValidationError if the value is not a valid name.

    This method is used to validate a name value against a predefined regex
    pattern for name validation.

    Usage:
    - Used on Models/Forms to validate name fields
    """
    name_validator = \
        RegexValidator(Validation.PATTERNS.NAME, Validation.MESSAGES.NAME)
    try:
        name_validator(value)
    except ValidationError as exc:
        raise ValidationError(Validation.ERRORS.NAME) from exc

def valid_email(value) -> None:
    """Validates whether the given value is a valid email.

    :param value: The value to be validated as an email.
    :return: None
    :raises: ValidationError if the value is not a valid email.

    This method is used to validate an email value against a predefined regex
    pattern for email validation.

    Usage:
    - Used on Models/Forms to validate email fields

    """
    email_validator = \
        RegexValidator(Validation.PATTERNS.EMAIL, Validation.MESSAGES.EMAIL)
    try:
        email_validator(value)
    except ValidationError as exc:
        raise ValidationError(Validation.ERRORS.EMAIL) from exc

def valid_password(value) -> None:
    """Validate Password

    :param value: The password value to be validated.
    :return: None
    :raises: ValidationError if the value is not a valid password.

    This method is used to validate a password value against predefined regex
    patterns for various password requirements.
    It raises a `ValidationError` if
    the password value does not meet any of the requirements.

    Example Usage:
    ```
    try:
        valid_password("password123")
        print("Password is valid.")
    except ValidationError as e:
        print("Password is invalid:", str(e))
    ```

    Usage:
    - Used on Models/Forms to validate password fields

    Alternatives:
    - Djnago comes with out password validations, see settings.py
    - AUTH_PASSWORD_VALIDATORS
    """
    error_messages = []

    for key, regex in Validation.PATTERNS.PASSWORD.items():
        validator = RegexValidator(regex, Validation.MESSAGES.PASSWORD[ key ])

        try:
            validator(value)
        except ValidationError:
            error_messages.append(Validation.ERRORS.PASSWORD[ key ])

    if error_messages:
        full_error_message = ', '.join(error_messages) + '. '
        raise ValidationError(full_error_message)
