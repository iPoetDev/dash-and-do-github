#!/user/bin/env python3
"""@File: <filename>.py .

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
# OopCompanion:suppressRename

from allauth.account.forms import LoginForm
from allauth.account.forms import PasswordField
from allauth.account.forms import SetPasswordField
from allauth.account.forms import SignupForm
from django import forms

#
from apps.users.helpers import set_remember_me_request as set_remember


class Forms:
    """The `Forms` class.

    Provides a set of nested classes that represent various
    form fields and their properties.
    Inspired by 12 Factor App: https://12factor.net/config.
    """

    class Fields:
        """The `Fields` class.

        Provides a set of nested classes that represent.
        """
        PUBLIC = 'public'
        TABINDEX = 5
        MAX_LENGTH = 50
        MIN_LENGTH = 8

        class Password:
            """The `Password` class.

            Provides a set of nested classes that
            represent various properties of a password field.
            """
            LABEL = "Password"
            CONFIRM = "Confirm Password"
            NEW = "New Password"
            TITLE = "Enter a Valid Password"
            TITLE_CONFIRM = "Confirm a Valid Password"
            TITLE_NEW = "Enter a New Password"
            PLACEHOLDER = "Password"
            HTML_LABEL = "password"
            HTML_CONFIRM = "password2"
            HTML_NEW = "password1"
            AUTO_COMPLETE = "password"
            AUTO_COMPLETE_NEW = "new-password"
            PATTERN = ("(?=.*\\d)(?=.*[a-z])(?=.*[A-Z])"
                       "(?=.*[@$!%*?&]).{12,50}")
            HELP_TEXT = ("Passwords use a-z, A-Z, 0-9 and "
                         "@,$,!,%,*,?,&, "
                         "min: 12, max: 50. Must match.")
            MIN_LENGTH = 12
            MAX_LENGTH = 50

        class Email:
            """The `Email` class.

            Provides a set of nested classes that
            represent various properties of an email field.
            """
            LABEL = "Email Address"
            TITLE = "Enter a Valid Email"
            PLACEHOLDER = "Email"
            HTML_LABEL = "email"
            AUTO_COMPLETE = "email"
            PATTERN = ("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]"
                       "+\.[a-zA-Z0-9-.]+$.{8,50}")
            HELP_TEXT = ("Choose a valid Email: a-z, A-Z, 0-9,"
                         " _ + - , min 8, max 50")

        class Username:
            """The `Username` class.

            Provides a set of nested classes that
            represent various properties of a username field.
            """
            LABEL = "Username"
            TITLE = "Enter a Valid Username"
            PLACEHOLDER = "Username"
            HTML_LABEL = "username"
            AUTO_COMPLETE = "username"
            PATTERN = ("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]"
                       "+\.[a-zA-Z0-9-.]+$.{6,30}")
            HELP_TEXT = ("Choose a valid Username: a-z, A-Z, 0-9,"
                         " _ + - , min 6, max 30")
            MIN_LENGTH = 6
            MAX_LENGTH = 30


class DashEmailAuthField(forms.EmailField):
    """The `DashEmailAuthField` class.

    A subclass of the `forms.EmailField`
    class from the Django library. It is used to represent an email input
    field in a form.

    Attributes:
        - label: A string representing the label for the email field.
        - help_text: A string representing the help text for the email field.
        - widget: An instance of `forms.EmailInput` representing the widget
        for the email field.

    Methods:
        - __init__(*args, **kwargs): Initializes the `DashEmailAuthField`
        instance. It sets the label, help_text, and widget attributes for
        the field.
        - update_attrs(**kwargs): Updates the attributes of the widget for
        the field.
        - field_attrs(): Returns a dictionary of attributes for the widget.
    """

    def __init__(self, *args, **kwargs):
        """:param args: variable-length argument list
        :param kwargs: keyword arguments

        This method initializes an instance of the DashEmailAuthField class.
        It inherits from the Django forms.EmailField class and
        adds customizations for a specific use case.

        The method first calls the __init__ method of the parent class to
         perform any necessary initializations.
         It then sets the label, help text, and widget properties of the field.

        The label is set to the value of Forms.Fields.Email.LABEL.
        The help_text is set to the value of Forms.Fields.Email.HELP_TEXT.
        The widget is set to an instance of forms.EmailInput
         with custom field attributes.
        """
        super().__init__(*args, **kwargs)
        self.label = Forms.Fields.Email.LABEL
        self.help_text = Forms.Fields.Email.HELP_TEXT
        self.widget = forms.EmailInput(attrs=self.field_attrs())

    def update_attrs(self, **kwargs):
        """Updates the attributes of the field's widget.
        :param kwargs:
        :return:
        """
        self.widget.attrs.update(kwargs)

    @classmethod
    def field_attrs(cls):
        """Default attributes for the field's widget.

        Returns a dictionary of attributes for the field's widget.

        :return:
        """
        return {
            'id': 'signup-email',
            'aria_description': Forms.Fields.Email.HELP_TEXT,
            'aria_label': Forms.Fields.Email.TITLE,
            'autocomplete': Forms.Fields.Email.AUTO_COMPLETE,
            'data_view': Forms.Fields.PUBLIC,
            'maxlength': f'{Forms.Fields.MAX_LENGTH}',
            'minlength': f'{Forms.Fields.MIN_LENGTH}',
            'name': Forms.Fields.Email.HTML_LABEL,
            'pattern': Forms.Fields.Email.PATTERN,
            'placeholder': Forms.Fields.Email.PLACEHOLDER,
            'tabindex': Forms.Fields.TABINDEX,
            'title': Forms.Fields.Email.TITLE,
        }


class DashUsernameField(forms.CharField):
    """The DashUsernameField class.

     Aubclass of forms.CharField from the
    Django forms module.

    Parameters:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Methods:
        __init__(self, *args, **kwargs):
            Initializes the DashUsernameField instance.

        update_attrs(self, **kwargs):
            Updates the attributes of the field's widget.

        field_attrs(cls):
            Returns a dictionary of attributes for the field's widget.

    Attributes:
        widget: An instance of forms.TextInput with the field's attributes.

    """

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the DashUsernameField class.
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.widget = forms.TextInput(attrs=self.field_attrs())

    def update_attrs(self, **kwargs):
        """Field attrs update

        Updates the attributes of the field's widget.
        :param kwargs:
        """
        self.widget.attrs.update(kwargs)

    @classmethod
    def field_attrs(cls):
        """Default attributes for the field's widget.

        The default attributes for the field's widget.
        :return:
        """
        return {
            'id': 'signup-username',
            'aria_description': Forms.Fields.Username.HELP_TEXT,
            'aria_label': Forms.Fields.Username.TITLE,
            'autocomplete': Forms.Fields.Username.AUTO_COMPLETE,
            'data_view': Forms.Fields.PUBLIC,
            'maxlength': f'{Forms.Fields.Username.MAX_LENGTH}',
            'minlength': f'{Forms.Fields.Username.MIN_LENGTH}',
            'name': Forms.Fields.Username.HTML_LABEL,
            'placeholder': Forms.Fields.Username.PLACEHOLDER,
            'tabindex': Forms.Fields.TABINDEX,
            'title': Forms.Fields.Username.TITLE,
        }


class DashPasswordField(PasswordField):
    """Subclass of `allauth.account.forms.PasswordField`.

    This class represents a password field with additional attributes
    and methods specific to a dashboard application.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Attributes:
        help_text (str): The help text for the field.
        required (bool): Whether the field is required.
        strip (bool): Whether leading and trailing whitespaces should be
        stripped from the input value.
        label (str): The label to display for the field.
        widget (django.forms.PasswordInput): The widget used for rendering
        the field.
        error_messages (dict): A dictionary containing error messages for
        different validation errors.

    Methods:
        update_attrs(**kwargs): Updates the attributes of the widget.
        field_attrs() -> dict: Returns a dictionary containing the default attributes for the field.
    """

    def __init__(self, *args, **kwargs):
        """Instance of the DashPasswordField class.

        Initializes a new instance of the DashPasswordField class.
        :param args:
        :param kwargs:
        """
        max_length = kwargs.pop('max_length', None)
        min_length = kwargs.pop('min_length', None)
        super().__init__(*args,
                         max_length=max_length,
                         min_length=min_length,
                         **kwargs)
        self.help_text = kwargs.get('help_text', None)
        self.required = kwargs.get('required', True)
        self.strip = kwargs.get('strip', True)
        self.label = kwargs.get('label', None)
        self.widget = forms.PasswordInput(attrs=self.field_attrs())
        self.error_messages = kwargs.get('error_messages', None)

    def update_attrs(self, **kwargs):
        """Updates the attributes of the widget."""
        self.widget.attrs.update(kwargs)

    @classmethod
    def field_attrs(cls):
        """Default attributes for the field's widget.

        Default attributes for the field's widget.
        :return: Dictionary of attributes for the field's widget.
        :rtype: dict
        """
        return {
            'id': '',
            'name': Forms.Fields.Password.HTML_LABEL,
            'autocomplete': Forms.Fields.Password.AUTO_COMPLETE,
            'placeholder': Forms.Fields.Password.PLACEHOLDER,
            'aria_label': Forms.Fields.Password.TITLE,
            'max_length': f'{Forms.Fields.Password.MAX_LENGTH}',
            'min_length': f'{Forms.Fields.Password.MIN_LENGTH}',
            'pattern': Forms.Fields.Password.PATTERN,
            'required': True,
            'data_view': Forms.Fields.PUBLIC,
            'title': Forms.Fields.Password.TITLE,
            'aria_description': Forms.Fields.Password.HELP_TEXT,
            'tabindex': Forms.Fields.TABINDEX
        }


class DashSetPasswordField(SetPasswordField, DashPasswordField):
    """The `DashSetPasswordField` class is a custom password field
    implementation in Django, which inherits from both `SetPasswordField`
    and `DashPasswordField`.
    It provides additional functionality and customization options
    for password field inputs.

    Attributes:
        - `attr_id`: The ID attribute for the password field input.
        - `attr_name`: The name attribute for the password field input.

    Methods:
        - `__init__(*args, attr_id=None, attr_name=None, **kwargs)`:
         Initializes a new instance of the `DashSetPasswordField` class.
         Accepts any additional arguments that may be passed to the parent,
          as well as optional `attr_id` and `attr_name` parameters for
          customizing the ID and name attributes of the password field input.

        - `field_attrs()`: Returns a dictionary of default attributes for
         the password field. These attributes can be customized to fit
         specific requirements and preferences.
    """

    def __init__(self, *args, attr_id=None, attr_name=None, **kwargs):
        """Initializes a new instance of the `DashSetPasswordField` class."""
        super().__init__(*args, **kwargs)
        self.widget.attrs.update(self.field_attrs())
        if attr_id or attr_name:
            self.widget.attrs.update({'id': attr_id, 'name': attr_name})

    @classmethod
    def field_attrs(cls):
        """Default attributes for the field's widget."""
        return {
            'id': '',
            'name': '',
            'autocomplete': Forms.Fields.Password.AUTO_COMPLETE_NEW,
            'placeholder': Forms.Fields.Password.PLACEHOLDER,
            'title': Forms.Fields.Password.TITLE_NEW, }


class DashLoginForm(LoginForm):
    """A custom login form for the Dash application.
    Extend and override the allauth.account.forms.LoginForm.

    This form extends the allauth.account.forms.LoginForm class for custom
     functionality.
    It adds a "Remember Me" checkbox field to the login form.

    Usage:
      form = DashLoginForm(data=request.POST)
      if form.is_valid():
          form.login(request)
      ...

    Attributes:
        remember_me (forms.BooleanField): A checkbox field to allow users to
         indicate if they want to be remembered.
    """
    # Add additional fields if necessary
    remember_me = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        """DashLoginForm class.

        Initialize a new instance of the DashLoginForm class.
        :param args:
        :param kwargs:

        Pops the request.Post data and passes it to the parent class.
        Sets the remember_me field label. to Remember Me
        If data is passed to the form, it is validated.
        """
        data = kwargs.pop('data', None)
        super().__init__(data, *args, **kwargs)
        self.fields[ 'remember_me' ].label = "Remember Me"
        if data:
            self.is_valid()

    def login(self, *args, **kwargs):
        """Handles the login process and sets the remember me cookie.
        :param args: (optional) Additional positional arguments
        :param kwargs: (optional) Additional keyword arguments.

        :return: The result of the original `login` method execution.
        https://django-allauth.readthedocs.io/en/latest/account/forms.html#login
        """
        # Add your own processing here.
        ret = super(DashLoginForm, self).login(*args, **kwargs)
        if self.is_valid():
            # Remember Me | Sessions Handling | Stay Logged In
            set_remember(self.request, self.cleaned_data.get('remember_me'))
        # You must return the original result.
        return ret


class DashSignupForm(SignupForm):
    """Custom Signup Form from Django Allauth.forms.SignupForm.

    A custom signup form for the Dash application.
    """
    email = DashEmailAuthField(
        label="Email Address",
        help_text="Enter a valid email address",
        required=True,
        min_length=8,
        max_length=50,
        error_messages={
        })
    newpassword = DashSetPasswordField(
        attr_id='new-password',
        attr_name='password1',
        label="New Password",
        help_text="Passwords use a-z, A-Z, 0-9 and @,$,!,%,*,?,&, "
                  "min: 12, max: 50. Must match.",
        required=True,
        min_length=12,
        max_length=50,
        error_messages={

        })
    confirmpassword = DashSetPasswordField(
        attr_id='confirm-password',
        attr_name='password2',
        label="Confirm Password",
        help_text="Confirm your Password",
        required=True,
        min_length=12,
        max_length=50,
        error_messages={},
    )

    def __init__(self, *args, **kwargs):
        """DashSignupForm class.

        Initialize a new instance of the DashSignupForm class.
        :param args:
        :param kwargs:
        """
        data = kwargs.pop('data', None)
        super().__init__(data, *args, **kwargs)
        if data:
            self.is_valid()

    def save(self, request):
        """Save Method.

        :param request: Django request object
        :return: User object

        This method is used to save a signup form and create a new user in the
         system. It takes in a Django request object and returns the created
         user object.
        """
        return super(DashSignupForm, self).save(request)

    def clean(self):
        """Clean the form data.

        This method validates the password fields `password1` and `password2`
        of the `DashSignupForm` form. It ensures that both passwords match
        each other.

        :return: The cleaned form data.

        """
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError(
                "Passwords don't match.") if password1 and password2 else None

        return self.cleaned_data
