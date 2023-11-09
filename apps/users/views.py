#!/user/bin/env python3
# pylint: disable=R0901
"""@File: <filename>.py
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
- added: Created initial file: 23/09/26:
- Updated:
- updated:
@Plan:
- TODO:
- FIXME:
- CHECK:
    - DONE: PyLint 2023/09/30
    - IGNORE: PyLint R0901,R0903
"""
import logging

from allauth.account.utils import passthrough_next_redirect_url
# OopCompanion:suppressRename
# AllAuth Libraries
from allauth.account.views import ConfirmEmailView
from allauth.account.views import LoginView
from allauth.account.views import LogoutView
from allauth.account.views import SignupView
from allauth.core.exceptions import ImmediateHttpResponse
# Django Libraries
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from django.middleware.csrf import get_token
from django.shortcuts import render
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy

# Local Libraries: Users
from apps.users.debugg import DebugAdapter as Debugg
# Local Libraries
from apps.users.forms import DashLoginForm
from apps.users.forms import DashSignupForm
from apps.users.helpers import get_last_status
from apps.users.sessions import DashUserSession
from apps.users.values import SiteContext
from dash_and_do.htmx import hx_redirect_success
from dash_and_do.settings import DEBUG
from dash_and_do.settings import LOGIN_REDIRECT_URL
from dash_and_do.settings import LOGOUT_REDIRECT_URL
# from dash_and_do.settings import SESSION_COOKIE_AGE as DEFAULT_SESSION_AGE
# Local Libraries: Dash and Do
from dash_and_do.utils import get_date


# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import ensure_csrf_cookie


debugr = Debugg()


class FormViews:  # pylint: disable=too-few-public-methods
    """Form Values: Strings."""
    DEFAULT_FORM_KEY = 'form'
    INDEX_REVERSE = 'kore:index'
    VERIFY_REVERSE = 'kore:verify'
    PRIVATE_REVERSE = 'kore:private'
    CONFIRM_REVERSE = 'kore:confirm'
    TOGGLE_FRIENDLY = False
    TOGGLE_ERROR = True


    class Login:  # pylint: disable=too-few-public-methods
        """Constants Class for Login FormView."""
        VIEWNAME = 'DashLoginView'
        CTXNAME = 'login_form'
        TEMPLATE = 'forms/form_login.html'
        PREFIX = 'current'
        REMEMBER = 'remember'


    class Signup:  # pylint: disable=too-few-public-methods
        """Constants Class for Signup FormView."""
        VIEWNAME = 'DashSignupView'
        CTXNAME = 'signup_form'
        TEMPLATE = 'verify.html'
        SIGNUP_KEY = 'signup_url'
        SIGNUP_URL = 'users:account_signup'
        SUCCESS_URL = 'verify.html'
        CONFIRM_URL = 'account_confirm_email.html'
        PREXIX_KEY = 'prefix'
        PREFIX_UNBOUND = 'new'
        PREFIX_BOUND = 'data'
        SUCCESS_MESSAGE = ('Please check your email to '
                           'activate your account.')
        UNEXPECTED_FRIENDLY = ('An unexpected issue occurred during '
                               'registration. Please try again later.')


    # noinspection PyUnusedClass
    class Confirm:  # pylint: disable=too-few-public-methods
        """Constants Class for Signup FormView."""
        CTXNAME = 'confirm_view'
        TEMPLATE = 'confirm.html'
        PREFIX = 'confirm'
        EMAIL_CTXKEY = 'email'
        IS_CTXCONFIRM = 'can_confirm'


    class LogoutView:  # pylint: disable=too-few-public-methods
        """Constants Class for LogoutView."""
        TEMPLATE = 'account/logout.html'


class SessionVals:
    """The SessionVals class: Set of constants/flags used for session values.

    Attributes:
        VALID (bool): Represents a valid session value.
        INVALID (bool): Represents an invalid session value.
        CONFIRMED (bool): Represents a confirmed session value.
        NOTCONFIRM (bool): Represents a not confirmed session value.
        VERIFIED (bool): Represents a verified session value.
    NOTVERIFIED (bool): Represents a not verified session value.
    """
    VALID = True
    INVALID = False
    CONFIRMED = True
    NOTCONFIRM = False
    VERIFIED = True
    NOTVERIFIED = False
    # If "remember" is not set, expire the session
    # hen the user closes their browser.
    EXPIRE_NOT_SET = -1
    REMEMBER = 60 * 60 * 24 * 7 * 2
    BROWSER_CLOSE = 0


# noinspection PyUnusedClass
class HTTP:  # pylint: disable=too-few-public-methods # noinspection
    """HTTP Headers: Strings."""

    REDIRECTS = True
    REDIRECTS_OFF = False


    # noinspection PyUnusedClass
    class Headers:  # pylint: disable=too-few-public-methods
        """HTTP Headers: Strings."""
        HX_REDIRECT = 'HX-Redirect'
        HTTP_LOCATION = 'Location'
        HX_CONTENT_TYPE = 'Content-Type'
        HX_CONTENT_FORMAT = 'text/html'


    # noinspection PyUnusedClass
    class Methods:  # noinspection
        """HTTP Methods: Strings."""
        GET = 'GET'
        POST = 'POST'
        PUT = 'PUT'


logger = logging.getLogger(__name__)
sitecontext = SiteContext()


def log_template(view, request, context, template,
                 exec=False, trace=True, level=1):
    """Log Template."""
    logger = logging.getLogger('django.template')
    logger.debug(view,
                 exc_info=exec,
                 stack_info=trace,
                 stacklevel=level,
                 extra={'request': request,
                        'template': template,
                        'context': context})


class DashSignupView(SignupView):
    """DashSignupView class is a custom implementation of the SignupView class
    from the allauth library.

    It provides functionality for user signup and
    handles the form validation and submission.

    Attributes:
    :param: template_name: The path to the template file for
                rendering the signup view.
    :param: success_url: The URL where the user will be redirected
                after successful signup.
    :param: form_class: A class representing the form used for user signup.

    Methods:
    :method: post
            It handles the form submission and validation.
            If the form is valid, it redirects the user to the success URL.
            If the form is invalid, it re-renders the form with error messages.
    :method: form_valid:
            It is called when the form is valid.
            It performs custom logic before saving the user instance.
            It sets the email and verification flags in the user session.
            It also sends a success message to the user.
            Finally, it redirects the user to the success URL
            using the `hx_redirect_success` function.
    :method: form_invalid:
            It is called when the form is invalid.
            It raises an ImmediateHttpResponse with the rendered
            form HTML to be handled by HTMX.
    :method: get_context_data
            It retrieves additional context data for the template rendering,
             including the session data and the latest status.
    :method: get_success_url:
            Returns the success URL for the user after successful signup.

    Note: This class relies on other imported modules and classes such as
    ConfirmEmailView, LoginView, LogoutView, ImmediateHttpResponse,
    hx_redirect_success, is_htmx, LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL,
    messages, HttpResponse, HttpResponseRedirect, render, render_to_string,
    reverse_lazy, DebugAdapter, get_last_status, and DashUserSession.
    """

    template_name = FormViews.Signup.TEMPLATE  # specify your own template
    success_url = reverse_lazy(FormViews.VERIFY_REVERSE)
    form_class = DashSignupForm  # Custom AllAuth Signup Form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = None
        self.setlog('django.request')

    def get(self, request, *args, **kwargs):
        signup = self.form_class()  # signup is the labeled form instance
        self.log(FormViews.Signup.VIEWNAME, self.request,
                 signup, 'GET')
        return render(request,
                      self.template_name,
                      {'signup_form': signup})

    def post(self, request, *args, **kwargs):
        """Post method for the SignupView class.

        :param request: The HTTP request object.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: An HTTP response | HTTP Redirect object(s).
        """
        # Validate the form.
        super().post(request, *args, **kwargs)
        signup = self.get_form()  # signup is the labeled form instance
        # Check if form is valid, redirect to success_url
        if signup.is_valid():
            # Redirect on valid.
            return HttpResponseRedirect(self.get_success_url())
        else:
            # If form is not valid, re-render the form with error messages
            signup_context = {FormViews.Signup.CTXNAME: signup}
            return TemplateResponse(request, FormViews.Signup.TEMPLATE,
                                    signup_context, content_type='text/html')

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        # Here you can add your custom logic before the user instance is saved
        # handle validation here...
        # ??
        # Call the parent class's method to handle the saving and redirection
        # logic
        # Call the parent class's method to handle the saving and redirection
        # logic
        response = super().form_valid(form)
        # For example, if you want to send a custom success message:
        messages.success(self.request, FormViews.Signup.SUCCESS_MESSAGE)

        return hx_redirect_success(self.request, response, self.success_url)

    def form_invalid(self, form):
        """If the form is invalid, return the form with error messages to
        HTMX.
        """
        signup_context = {FormViews.Signup.CTXNAME: form}
        form_html = render_to_string(self.template_name,
                                     signup_context,
                                     request=self.request)
        raise ImmediateHttpResponse(HttpResponse(form_html))

    def get_context_data(self):
        """Addto session_data to context_data.

        :return: A dictionary containing the context data.
        """
        context = super().get_context_data()
        last_status = get_last_status(self.request)
        if session_data := DashUserSession(self.request).fetch_session_data():
            context['session_data'] = session_data
        if last_status:
            context['latest_status'] = last_status
        return context

    def get_success_url(self):
        """Set the success_url for the view.

        Uses a proxy (the reverse_lazy() function) to future proof
        changes Uses a constant to have strings configured elsewhere
        :return: A string representing the success URL from namespace
            URL.
        """
        # Redirect the user to the verification page
        return reverse_lazy(FormViews.VERIFY_REVERSE)

    def setlog(self, loggr, debugg=DEBUG):
        """ Sets the logger for the class

        :param loggr: The logger to be used for logging.
        :param debugg: Django's DEBUG indicating whether to log or not
        based on the DEBUG setting.
        """
        if debugg:
            self.logger = logging.getLogger(loggr)
        else:
            self.logger = None

    def log(self, view, request, form=None, method=None):
        """ Logs the request and form details for debugging purposes.

        :param view: The name of the view.
        :type view: str
        :param request: The request object received from the client.
        :type request: django.http.HttpRequest
        :param form: The form object containing user login information.
        :type form: apps.users.forms.DashLoginForm
        :param method: The HTTP method used for the request.
        :type method: str
        :return: None
        :rtype: NoneType

        This method logs the request and form details for debugging purposes
         in the DashLoginView class.
         It uses the requestlogger to log the POST data and form information.
         If the requestlogger is not provided, no logging will occur.

        Example usage:
            view = DashLoginView()
            view.log(request, form)
        """
        if self.logger is not None:  # i.e. Only on DEBUG
            if method is not None:
                self.logger.debug(f'{view}: {method}: {request.POST}')
            if form is not None:
                self.logger.debug(f'{view}: {method}: form: {form}')


class DashLoginView(LoginView):
    """ DashLoginView is a class-based view that handles the login
    functionality in the application.

    Attributes:
    :param: template_name (str): The name of the template to be used for
            rendering the login page.
    :param: success_url (str): The URL to redirect the user to after
            successful login.
    :param: form_class (class): The form class to be used for rendering the login form.

    Methods:
    :method: __init__(self, *args, **kwargs):
             Initializes the DashLoginView object.
    :method: get_context_data(self, **kwargs) -> dict:
             Updates the context data for the template.
    :method: get(self, request, *args, **kwargs) -> HttpResponse:
             Handles the GET request for the login page.
    :method: post(self, request, *args, **kwargs) -> HttpResponse:
             Handles the POST request for the login page.
    :method: form_valid(self, form) -> HttpResponse:
             Handles the case when the form is valid.
    :method: form_invalid(self, form) -> HttpResponse:
             Handles the case when the form is invalid.
    :method: get_authenticated_redirect_url(self) -> str:
             Returns the URL to redirect the user to after authentication.
    :method: setlog(self, loggr, debugg=DEBUG):
             Sets the logger for the class.
    :method: log(self, view, request, form=None, method=None):
             Logs the request and form details for debugging purposes.
    """
    template_name = FormViews.Login.TEMPLATE
    success_url = reverse_lazy(FormViews.PRIVATE_REVERSE)
    form_class = DashLoginForm

    # - TODO: Redirect user based on their role after successful login
    #     Is is staff: redirect to admin dashboard, however research suggest
    #     that AllAuth does not handle admin logins, and that it is best to
    #     use a redirect to its login page, so assessor has two accesses
    #     1) Correct use of a superuser (admin only, no reuse)
    #     2) Creates a normal user to verify for functionality.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = None
        self.setlog('django.request')

    def get_context_data(self, **kwargs):
        """ Update the context data: logn form, signup url

        :param kwargs: Additional keyword arguments
        :type kwargs: dict
        :return: The updated context data
        :rtype: dict
        """
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Check if 'form' key exists in the context
        if FormViews.DEFAULT_FORM_KEY in context:  # 'form'
            # Map 'login_form' to the 'form' object
            context[FormViews.Login.CTXNAME] = context[  # 'login_form'
                FormViews.DEFAULT_FORM_KEY]  # 'form'
            # Remove the default 'form' key safely from the context
            context.pop(FormViews.DEFAULT_FORM_KEY, None)  # 'form'
        # Update the signup_url in the context for Local App
        context[FormViews.Signup.SIGNUP_KEY] = passthrough_next_redirect_url(
            self.request,
            reverse(FormViews.Signup.SIGNUP_URL),
            self.redirect_field_name)
        return context

    def get(self, request, *args, **kwargs):
        login = self.form_class()  # signup is the labeled form instance
        if DEBUG:
            self.log(FormViews.Login.VIEWNAME,
                     self.request,
                     login,
                     'GET')
            log_template(FormViews.Login.VIEWNAME + ': GET',
                         self.request,
                         self.get_context_data(),
                         self.template_name)
        return render(self.request,
                      self.template_name,
                      {'login_form': login})

    def post(self, request, *args, **kwargs):
        login = self.get_form()  # form for login and introspection/logging
        # Checks for valid login.
        if login.is_valid():
            remember_me = login.cleaned_data.get(FormViews.Login.REMEMBER)
            if remember_me:
                request.session.set_expiry(SessionVals.REMEMBER)  # 2 weeks
            else:
                request.session.set_expiry(SessionVals.BROWSER_CLOSE)  # 1 week
        # Process the form as per the super request.
        if DEBUG:
            self.log(FormViews.Login.VIEWNAME,
                     self.request,
                     login,
                     'POST')
            log_template(FormViews.Login.VIEWNAME + ': POST',
                         self.request,
                         self.get_context_data(),
                         self.template_name)
        return super().post(request, *args, **kwargs)

    # noinspection PyUnresolvedReferences
    def form_valid(self, form):
        response = super().form_valid(form)
        # Check if user is authenticated (which indicates active session)
        if self.request.user.is_authenticated:
            # When session is active: set configuration of the session here.
            # For instance, you may want to set a value in the session:
            # User tracking, session control, etc.
            self.request.session['session_start_time'] = get_date()
        else:
            # Handle case when a session is not active.
            # Possibly you may want to redirect to login page.
            # Possibly reloading the index page `/` on invalid requests
            return HttpResponseRedirect(LOGIN_REDIRECT_URL)
        return response

    # noinspection PyUnresolvedReferences
    # - todo: Add custom logging here, if in scope
    # - todo: add application clean up logic
    def form_invalid(self, form):
        if self.request.user.is_authenticated:
            user_identifier = (self.request.user.username or
                               self.request.user.email)
            if user_identifier:
                error_message = ('Invalid form submission by user: '
                                 f'{user_identifier}')
                if DEBUG:
                    form.add_error(None, error_message)
        return super().form_invalid(form)

    def get_authenticated_redirect_url(self):
        """
        Returns the URL to redirect the user to after authentication.

        :return: The URL to redirect the user to after authentication.
        :rtype: str
        """
        # Checks, defensively, if the user is authenticated, and
        #  checks if the redirect_field_name is set against
        #   a APPROVED LIST OF URLS (like a lookup for all app urlss)
        # Assume all input is malicious. i.e. self.redirect_field_name
        # Use an "accept known good" input validation strategy,
        # noinspection PyUnusedLocal
        redirect_field_name = self.redirect_field_name
        # then update the self.redirect_field_name to the new value, else,
        # logs the user out and kills the current session.
        authorised_redirect_url = super().get_authenticated_redirect_url()
        return authorised_redirect_url

    def setlog(self, loggr, debugg=DEBUG):
        """ Sets the logger for the class

        :param loggr: The logger to be used for logging.
        :param debugg: Django's DEBUG indicating whether to log or not
        based on the DEBUG setting.
        """
        if debugg:
            self.logger = logging.getLogger(loggr)
        else:
            self.logger = None

    def log(self, view, request, form=None, method=None):
        """

        :param view: The name of the view.
        :type view: str
        :param request: The request object received from the client.
        :type request: django.http.HttpRequest
        :param form: The form object containing user login information.
        :type form: apps.users.forms.DashLoginForm
        :param method: The HTTP method used for the request.
        :type method: str
        :return: None
        :rtype: NoneType

        This method logs the request and form details for debugging purposes
         in the DashLoginView class.
         It uses the requestlogger to log the POST data and form information.
         If the requestlogger is not provided, no logging will occur.

        Example usage:
            view = DashLoginView()
            view.log(request, form)
        """
        if self.logger is not None:  # i.e. Only on DEBUG
            if method is not None:
                self.logger.debug(f'{view}: {method}: {request.POST}')
            if form is not None:
                self.logger.debug(f'{view}: {method}: form: {form}')


class DashLogoutView(LogoutView):
    """DashLogoutView from Django AllAuth LogoutView.

    :param template_name: The name of the template to be rendered.
    :param success_url: The URL to redirect to upon successful response.
    """
    template_name = FormViews.LogoutView.TEMPLATE
    success_url = LOGOUT_REDIRECT_URL  # Heads back to index

    # pylint: disable=W0246
    def dispatch(self, request, *args, **kwargs):
        """:param request: The HTTP request object.
        :param args: Optional positional arguments.
        :param kwargs: Optional keyword arguments.
        :return: The HTTP response object.

        Dispatches a GET request to log out the user from the application.
        This method overrides the dispatch method of the LogoutView class
        from the allauth.account.views module. It adds custom logic after
        the default behavior of logging out the user.

        The method first calls the dispatch method of the parent class
        to perform the default behavior of logging out the user.
        It saves the response returned by the parent method
         in the variable `response`.

        After that, you can add your own custom logic to be executed after
        the user is logged out.  This logic should be placed between the
        calls to the parent's dispatch method and the return statement.

        Example usage:
            logout_view = DashLogoutView()
            response = logout_view.dispatch(request)

        Note: The example assumes that `request` is
         instance of the `HttpRequest` class.

        """
        # - todo Call the parent's dispatch method to add custom logic
        # - fixme Current;y W0246: Useless parent or super() delegation
        # - fixme in method 'dispatch' (useless-parent-delegation)
        return super().dispatch(request, *args,
                                **kwargs)  # pylint: disable=W0246
        # Add your custom logic here

    # noinspection PyUnusedFunction
    @staticmethod
    def get_next_redirect_url():
        """Get the redirect URL for the next page after logout.

        :return: A string representing the redirect URL.
        """
        # return to index
        return LOGOUT_REDIRECT_URL  # pylint: disable=too-many-ancestors


class DashConfirmEmailView(ConfirmEmailView):
    """Confirm Email View."""
    # template_name = FormViews.Confirm.TEMPLATE  # specify your own template
    template_name = 'confirm.html'

    def get_redirect_url(self):
        """Redirect to 'verify.html' after successful email verification."""
        return reverse_lazy(FormViews.CONFIRM_REVERSE)

    def get_context_data(self, **kwargs):
        """Get context data for the view.

        :param kwargs: Additional keyword arguments.
        :return: A dictionary containing the context data.
        """
        context = super().get_context_data(**kwargs)
        session_data = DashUserSession(self.request)
        #
        site_ctx = sitecontext.context
        confirm_ctx = sitecontext.confirm
        #
        context.update(
            {
                **site_ctx,
                **confirm_ctx,
            }
        )
        return context
