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
    - DONE: PyLint: 2023-10-05
    - DONE: Ruff: 2023-10-??
    - IGNORE: PyLint:?
"""
# OopCompanion:suppressRename

# from allauth.account import forms as aa_forms
# import allauth.account.forms as aa_forms
from allauth.account.forms import LoginForm
from allauth.account.forms import PasswordField
from allauth.account.forms import SetPasswordField
from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _

#
from apps.users.helpers import set_remember_me_request as set_remember


class FormVals:  # pylint: disable=too-few-public-methods
    """The `Forms` class.

    Provides a set of nested classes that represent various
    form fields and their properties.
    Inspired by 12 Factor App: https://12factor.net/config.
    """

    class Fields:  # pylint: disable=too-few-public-methods
        """The `Fields` class.

        Provides a set of nested classes that represent.
        """
        PUBLIC = 'public'
        TABINDEX = 5
        MAX_LENGTH = 50
        MIN_LENGTH = 8
        STRIP = True

        class Attrs:
            NAME = 'name'
            ID = 'id'

        class Email:  # pylint: disable=too-few-public-methods
            """The `Email` class.

            Provides a set of nested classes that
            represent various properties of an email field.
            """
            LABEL = 'Email Address'
            TITLE = 'Enter a Valid Email'
            PLACEHOLDER = 'Email'
            FIELD = 'email'
            HTML_LABEL = 'email'
            AUTO_COMPLETE = 'email'
            PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{8,50}'
            HELP_TEXT = ('Choose a valid Email: a-z, A-Z, 0-9,'
                         ' _ + - , min 8, max 50')
            MIN_LENGTH = 8
            MAX_LENGTH = 75
            REQUIRED = False
            WHITESPACE = True
            ERROR_INVALID = 'Invalid: Enter a valid email address.'
            ERROR_MIN_LENGTH = 'Invalid: Emails must be at least 8 characters.'
            ERROR_MAX_LENGTH = 'Invalid: Emails must be less than 50 characters.'
            ERROR_REQUIRED = 'Invalid: Email is required.'
            ERROR_WHITESPACE = 'Invalid: Email cannot contain whitespace.'
            ERROR_PATTERN = 'Invalid: Email must have <@domain.tld>'
            ERROR_UNIQUE = 'Invalid: Email already exists.'
            ERROR_REQUIRED = 'Invalid: Email is required.'

        class Username:  # pylint: disable=too-few-public-methods
            """The `Username` class.

            Provides a set of nested classes that
            represent various properties of a username field.
            """
            LABEL = 'Username'
            TITLE = 'Enter a Valid Username'
            PLACEHOLDER = 'Username'
            HTML_LABEL = 'username'
            AUTO_COMPLETE = 'username'
            PATTERN = r"[a-zA-Z0-9_'-]{6,30}"
            HELP_TEXT = ('Choose a valid Username: a-z, A-Z, 0-9,'
                         ' _ + - , min 6, max 30')
            MIN_LENGTH = 6
            MAX_LENGTH = 30
            REQUIRED = False
            WHITESPACE = True
            ERROR_INVALID = 'Invalid: Enter a valid username.'
            ERROR_MIN_LENGTH = 'Invalid: Usernames must be at least 6 characters.'
            ERROR_MAX_LENGTH = 'Invalid: Usernames must be less than 30 characters.'
            ERROR_REQUIRED = 'Invalid: Username is required.'
            ERROR_WHITESPACE = 'Invalid: Username cannot contain whitespace.'
            ERROR_PATTERN = 'Invalid: Username must be a-z, A-Z, 0-9, _, +, -.'
            ERROR_UNIQUE = 'Invalid: Username already exists.'
            ERROR_REQUIRED = 'Invalid: Username is required.'

        class Password:  # pylint: disable=too-few-public-methods
            """The `Password` class.

            Provides a set of nested classes that
            represent various properties of a password field.
            """
            LABEL = 'Password'
            NEW = 'New Password'
            CONFIRM = 'Confirm Password'
            FIELD_1 = 'password1'
            FIELD_2 = 'password2'
            TITLE = 'Enter a Valid Password'
            TITLE_NEW = 'Enter a New Password'
            TITLE_CONFIRM = 'Confirm a Valid Password'
            PLACEHOLDER = 'Password'
            PLACEHOLDER_NEW = 'New Password'
            PLACEHOLDER_CONFIRM = 'Confirm Password'
            HTML_LABEL = 'password'
            HTML_NEW = 'password1'
            HTML_CONFIRM = 'password2'
            ERROR_MATCH = 'You must type the same password each time.'
            AUTO_COMPLETE = 'password'
            AUTO_COMPLETE_NEW = 'new-password'
            PATTERN = r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&]).{12,50}'
            HELP_TEXT = ('Passwords use a-z, A-Z, 0-9 and '
                         '@,$,!,%,*,?,&, '
                         'min: 12, max: 50. Must match.')
            MIN_LENGTH = 12
            MAX_LENGTH = 50
            TABINDEX_NEW = 6
            TABINDEX_ENTER = 7
            REQUIRED = False
            WHITESPACE = True
            ERROR_INVALID = 'Invalid: Enter a valid password.'
            ERROR_MATCH = 'Invalid: Passwords must match.'
            ERROR_MIN_LENGTH = 'Invalid: Passwords must be at least 12 characters.'
            ERROR_MAX_LENGTH = 'Invalid: Passwords must be less than 50 characters.'
            ERROR_REQUIRED = 'Invalid: Passwords are required.'

    class Errors:
        """"""

        @property
        def Email_Error_Messages(self):
            return {
                'required':_(FormVals.Fields.Email.ERROR_REQUIRED),
                'invalid':_(FormVals.Fields.Email.ERROR_INVALID),
                'min_length':_(FormVals.Fields.Email.ERROR_MIN_LENGTH),
                'max_length':_(FormVals.Fields.Email.ERROR_MAX_LENGTH),
                'whitespace':_(FormVals.Fields.Email.ERROR_WHITESPACE),
                'pattern':_(FormVals.Fields.Email.ERROR_PATTERN),
                'unique':_(FormVals.Fields.Email.ERROR_UNIQUE),
            }

        @property
        def Username_Error_Messages(self):
            return {
                'required':_(FormVals.Fields.Username.ERROR_REQUIRED),
                'invalid':_(FormVals.Fields.Username.ERROR_INVALID),
                'min_length':_(FormVals.Fields.Username.ERROR_MIN_LENGTH),
                'max_length':_(FormVals.Fields.Username.ERROR_MAX_LENGTH),
                'whitespace':_(FormVals.Fields.Username.ERROR_WHITESPACE),
                'pattern':_(FormVals.Fields.Username.ERROR_PATTERN),
                'unique':_(FormVals.Fields.Username.ERROR_UNIQUE),
            }

        @property
        def Password_Error_Messages(self):
            return {
                'required':_(FormVals.Fields.Password.ERROR_REQUIRED),
                'invalid':_(FormVals.Fields.Password.ERROR_INVALID),
                'min_length':_(FormVals.Fields.Password.ERROR_MIN_LENGTH),
                'max_length':_(FormVals.Fields.Password.ERROR_MAX_LENGTH),
                'whitespace':_(FormVals.Fields.Password.ERROR_WHITESPACE),
                'pattern':_(FormVals.Fields.Password.ERROR_PATTERN),
                'unique':_(FormVals.Fields.Password.ERROR_UNIQUE),
            }


message_errors = FormVals.Errors()


# noinspection PyArgumentList
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
    attr_id = None
    attr_name = None

    def __init__(self, *args, attr_id=None, attr_name=None, **kwargs):
        """:param args: variable-length argument list
        :param kwargs: keyword arguments

        This method initializes an instance of the DashEmailAuthField class.
        It inherits from the Django forms.EmailField class and
        adds customizations for a specific use case.

        The method first calls the __init__ method of the parent class to
         perform any necessary initializations.
         It then sets the label, help text, and widget properties of the field.

        The label is set to the value of FormVals.Fields.Email.LABEL.
        The help_text is set to the value of FormVals.Fields.Email.HELP_TEXT.
        The widget is set to an instance of forms.EmailInput
         with custom field attributes.
        """
        # Unset the max_length and min_length attributes
        max_length = kwargs.pop('max_length',
                                FormVals.Fields.Email.MAX_LENGTH)
        min_length = kwargs.pop('min_length',
                                FormVals.Fields.Email.MIN_LENGTH)
        # Normalise model/application length validation = friendly error msgs
        # Matches underlying model validation
        super().__init__(*args,
                         max_length=max_length,
                         min_length=min_length,
                         **kwargs)
        self.attr_id = attr_id if not None \
            else FormVals.Fields.Email.HTML_LABEL
        self.attr_name = attr_name if not None \
            else FormVals.Fields.Email.HTML_LABEL
        self.help_text = kwargs.get('help_text',
                                    FormVals.Fields.Email.HELP_TEXT)
        self.label = kwargs.get('label',
                                FormVals.Fields.Email.LABEL)
        self.required = kwargs.get('required', FormVals.Fields.Email.REQUIRED)
        self.strip = kwargs.get('strip', FormVals.Fields.Email.WHITESPACE)
        self.widget = forms.EmailInput(attrs=self.field_attrs())

    def init_attrs(self):
        if isinstance(self.widget, forms.PasswordInput) and self.widget.attrs:
            self.widget.attrs.update(self.field_attrs())
            self.update_attrs()
        else:
            self.widget = forms.PasswordInput(attrs=self.field_attrs())
            self.update_attrs()

    def update_attrs(self):
        custom_attrs = {  # Construct custom attributes
            'id':self.attr_id,
            'name':self.attr_name,
        }

        self.widget.attrs.update(custom_attrs)

    @classmethod
    def field_attrs(cls):
        """Default attributes for the field's widget.

        Returns a dictionary of attributes for the field's widget.

        :return:
        """
        return {
            'id':'signup-email',
            'name':FormVals.Fields.Email.HTML_LABEL,
            'aria_description':FormVals.Fields.Email.HELP_TEXT,
            'aria_label':FormVals.Fields.Email.TITLE,
            'autocomplete':FormVals.Fields.Email.AUTO_COMPLETE,
            'placeholder':FormVals.Fields.Email.PLACEHOLDER,
            'data_view':FormVals.Fields.PUBLIC,
            'maxlength':f'{FormVals.Fields.MAX_LENGTH}',
            'minlength':f'{FormVals.Fields.MIN_LENGTH}',
            'pattern':FormVals.Fields.Email.PATTERN,
            'tabindex':FormVals.Fields.TABINDEX,
            'title':FormVals.Fields.Email.TITLE,
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
        field_attrs() -> dict: Returns a dictionary containing the default
        attributes for the field.
    """
    attr_id = None
    attr_name = None

    def __init__(self, *args, attr_id=None, attr_name=None, **kwargs):
        """Instance of the DashPasswordField class.

        Initializes a new instance of the DashPasswordField class.
        :param args:
        :param kwargs:
        """
        # Unset the max_length and min_length attributes
        max_length = kwargs.pop('max_length', None)
        min_length = kwargs.pop('min_length',
                                FormVals.Fields.Password.MIN_LENGTH)
        # Normalise model/application length validation = friendly error msgs
        # Matches underlying model validation
        super().__init__(*args,
                         max_length=max_length,
                         min_length=min_length,
                         **kwargs)
        print(f'DashPassField: __init__(): max_length: {self.max_length}')
        print(f'DashPassField: __init__(): min_length: {self.min_length}')
        self.attr_id = attr_id if not None \
            else FormVals.Fields.Password.HTML_LABEL
        self.attr_name = attr_name if not None \
            else FormVals.Fields.Password.HTML_LABEL
        # Sets Field defaults from custom constants
        self.help_text = kwargs.get('help_text',
                                    FormVals.Fields.Password.HELP_TEXT)
        self.label = kwargs.get('label',
                                FormVals.Fields.Password.LABEL)
        self.required = kwargs.get('required',
                                   FormVals.Fields.Password.REQUIRED)
        self.strip = kwargs.get('strip',
                                FormVals.Fields.Password.WHITESPACE)
        self.init_attrs()

    def init_attrs(self):
        """Initializes the attributes of the field's widget.

        Initializes the attributes of the field's widget.
        :param kwargs:
        """
        # If the widget and its attributes already exist, update them
        if isinstance(self.widget, forms.PasswordInput) and self.widget.attrs:
            # DashPasswordField defaults
            self.widget.attrs.update(self.field_attrs())
        else:
            # assign new widget if it doesn't exist yet
            self.widget = forms.PasswordInput(attrs=self.field_attrs())

    def update_attrs(self, **kwargs):
        # Call update_attrs of super classes, if it exists
        # And continue with your specific logic
        self.widget.attrs.update(kwargs)

    @classmethod
    def field_attrs(cls):
        """Default attributes for the field's widget.

        Default attributes for the field's widget.
        :return: Dictionary of attributes for the field's widget.
        :rtype: dict
        """
        return {
            'id':'',
            'name':FormVals.Fields.Password.HTML_LABEL,
            'aria_description':FormVals.Fields.Password.HELP_TEXT,
            'aria_label':FormVals.Fields.Password.TITLE,
            'autocomplete':FormVals.Fields.Password.AUTO_COMPLETE,
            'placeholder':FormVals.Fields.Password.PLACEHOLDER,
            'data_view':FormVals.Fields.PUBLIC,
            'maxlength':f'{FormVals.Fields.Password.MAX_LENGTH}',
            'minlength':f'{FormVals.Fields.Password.MIN_LENGTH}',
            # 'pattern': FormVals.Fields.Password.PATTERN,
            'required':FormVals.Fields.Password.REQUIRED,
            'data_view':FormVals.Fields.PUBLIC,
            'title':FormVals.Fields.Password.TITLE,
            'tabindex':FormVals.Fields.Password.TABINDEX_NEW
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

    maxl = FormVals.Fields.Password.MAX_LENGTH
    minl = FormVals.Fields.Password.MIN_LENGTH

    def __init__(self, *args, attr_id=None, attr_name=None, max=None, min=None,
                 **kwargs):
        """Initializes a new instance of the `DashSetPasswordField` class."""
        super().__init__(*args, **kwargs)
        # Route custom attributes to the field's widget via self/update_attrs
        self.attr_id = attr_id
        self.attr_name = attr_name
        self.maxl = max if max is not None else FormVals.Fields.Password.MAX_LENGTH
        self.minl = min if min is not None else FormVals.Fields.Password.MIN_LENGTH
        # call  superclass init_attrs via DashPasswordField and MRO
        self.init_attrs()  # No args

    def init_attrs(self):
        if isinstance(self.widget, forms.PasswordInput) and self.widget.attrs:
            self.widget.attrs.update(self.field_attrs())
            self.update_attrs()
        else:
            self.widget = forms.PasswordInput(attrs=self.field_attrs())
            self.update_attrs()

    def update_attrs(self):
        custom_attrs = {  # Construct custom attributes
            'id':self.attr_id,
            'name':self.attr_name,
        }
        if hasattr(super(),
                   'update_attrs'):  # Call the super's update_attrs if exists
            super().update_attrs(**custom_attrs)
        else:  # Just update using the current class method
            self.widget.attrs.update(custom_attrs)

    @classmethod
    def field_attrs(cls):
        """Default attributes for the field's widget."""
        base_attrs = super().field_attrs()  # call base field_attrs to get default attrs
        # add or update attrs specific to DashSetPasswordField
        # Update with the signup defauls when setting a password
        base_attrs.update({
            'id':'',
            'name':'',
            'autocomplete':FormVals.Fields.Password.AUTO_COMPLETE_NEW,
            'placeholder':FormVals.Fields.Password.PLACEHOLDER_NEW,
            'tabindex':FormVals.Fields.Password.TABINDEX_NEW,
            'title':FormVals.Fields.Password.TITLE_NEW
        })
        return base_attrs


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
        self.fields['remember_me'].label = 'Remember Me'
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
        ret = super().login(*args, **kwargs)
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
        attr_id='signup-email',
        attr_name='email',
        label=FormVals.Fields.Email.LABEL,
        help_text=FormVals.Fields.Email.HELP_TEXT,
        max_length=FormVals.Fields.Email.MAX_LENGTH,
        min_length=FormVals.Fields.Email.MIN_LENGTH,
    )
    password1 = DashSetPasswordField(
        help_text=FormVals.Fields.Password.HELP_TEXT,
        attr_id='password1',
        attr_name='password1',
        min_length=FormVals.Fields.Password.MIN_LENGTH,
    )
    password2 = DashSetPasswordField(
        help_text=FormVals.Fields.Password.HELP_TEXT,
        attr_id='password1',
        attr_name='password2',
        min_length=FormVals.Fields.Password.MIN_LENGTH,
    )
    # # print(email.widget.attrs.items())
    print(password1.widget.attrs.items())
    # print(password1.widget.attrs['maxlength'])
    # print(password1.max_length)
    # print(password2.widget.attrs.items())
    is_saved = False
    use_required_attribute = False  # Disabled HTML5 required attribute

    def __init__(self, attrs_name=None, attrs_pwdname=None, *args, **kwargs):
        """DashSignupForm class.

        Initialize a new instance of the DashSignupForm class.
        :param args:
        :param kwargs:
        """
        data = kwargs.get('data', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        print(f'DashSignupForm: Clean(): Form data: {cleaned_data}')  # fixed bug
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        print(f'DashSignupForm: Clean(): password1: {password1}')
        print(f'DashSignupForm: Clean(): password2: {password2}')

        if password1 != password2:
            self.add_error('password', "Password does not match")

    # # pylint: disable=useless-super-delegation,W0246
    # def save(self, request):
    #     """Save Method.
    #
    #     :param request: Django request object
    #     :return: User object
    #
    #     This method is used to save a signup form and create a new user in the
    #      system. It takes in a Django request object and returns the created
    #      user object.
    #     """
    #     # from allauth.account.forms import SignupForm
    #     # self.base_signup_form_class = SignupForm
    #     # - todo Add custom signup save / cleanup logic here
    #     # - fixme W0246: Useless parent or super() delegation in method 'save'
    #     # - fixme (useless-super-delegation)
    #     print(f'SignUpForm: Save(): Form data: {self.cleaned_data}')
    #     return super().save(request)
    #
    # def clean(self):
    #     """Clean the form data.
    #
    #     This method validates:
    #     1) Super().clean() links in a chain of super().clean() methods.
    #     1) Checks the username field `username`: for handling Dummy
    #      via adapter.
    #     2) Checks the email field `email`: for handling Dummy via adapter.
    #     3) Cleans the password field to minimum length:  via adapter method.
    #         Uses a dummy user, as no user in db, as new user not created yet.
    #        - App Settings: Minimum Password Length
    #        - Django Valid: Is none.
    #        - Validate: Hooks from  settings enabled
    #             - refer: django.contrib.auth.validate_password
    #     3) the password fields `password1` and `password2`: `DashSignupForm`
    #        and  It ensures that both passwords match each other.
    #
    #     Attrs.name is html_name attribute, assigned by Forms fields
    #     - note: This method is called by the `is_valid` method of the form.
    #     - note: not calling in the super().clean() method
    #     - note: Is a good practice to call the super().clean() to inherit all
    #     - note: just copied and reimplemeted the super().clean() method
    #     - todo: refactor to use super().clean() method later, once it works
    #     - validate: 2023-10-04
    #     :return: The cleaned form data.
    #     :rtype: dict
    #     """
    #     super().clean()
    #     if self.valid:
    #         print(f'SignUpForm: Clean(): Form data: {self.cleaned_data}')
    #     print('SignUpForm: Clean(): Form data: Fetch User: Dummy User')
    #     User = get_user_model()  # pylint: disable=invalid-name
    #     dummy_user = User()
    #     user_username(dummy_user,
    #                   self.cleaned_data.get(
    #                       FormVals.Fields.Username.HTML_LABEL))
    #     user_email(dummy_user,
    #                self.cleaned_data.get(
    #                    FormVals.Fields.Email.HTML_LABEL))
    #     print(f'SignUpForm: Clean(): Form data: {self.cleaned_data}')
    #     newpass = self.cleaned_data.get(FormVals.Fields.Password.HTML_NEW)
    #     confirmpass = (
    #         self.cleaned_data.get(FormVals.Fields.Password.HTML_CONFIRM))
    #
    #     print(f'{FormVals.Fields.Password.HTML_NEW}: {newpass}',
    #           f'{FormVals.Fields.Password.HTML_CONFIRM}: {confirmpass}')
    #
    #     if newpass:
    #         try:
    #             print(f'SignUpForm: Clean(): Clean Pass: {newpass}')
    #             get_adapter().clean_password(newpass, user=dummy_user)
    #         except forms.ValidationError as invalid_password:
    #             print(f'SignUpForm: Clean(): Error: Invalid Pass: {newpass}')
    #             self.add_error(FormVals.Fields.Password.HTML_NEW,
    #                            invalid_password)
    #
    #     if (
    #         app_settings.SIGNUP_PASSWORD_ENTER_TWICE
    #         and FormVals.Fields.Password.HTML_NEW in self.cleaned_data
    #         and FormVals.Fields.Password.HTML_CONFIRM in self.cleaned_data
    #     ) and newpass != confirmpass:
    #         print(f'SignUpForm: Clean(): Error: No Match Pass: {newpass}')
    #         self.add_error(
    #             FormVals.Fields.Password.HTML_CONFIRM,
    #             _(FormVals.Fields.Password.ERROR_MATCH),
    #         )
    #     return self.cleaned_data
    #
    # def try_save(self, request):
    #     """Try Save Method extended.
    #
    #     :return: User object
    #
    #     This method is used to save a signup form and create a new user in the
    #      system. It takes in a Django request object and returns the created
    #      user object.
    #     """
    #     if self.account_already_exists:
    #         self.is_saved = False
    #
    #     self.is_saved = True
    #     if self.is_saved:
    #         print(f'SignUpForm: Try_Save(): Form data: {self.cleaned_data}')
    #     return super().try_save(request)
