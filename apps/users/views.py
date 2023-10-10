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
# OopCompanion:suppressRename
# AllAuth Libraries
from allauth.account.views import ConfirmEmailView
from allauth.account.views import LoginView
from allauth.account.views import LogoutView
from allauth.account.views import SignupView
from allauth.core.exceptions import ImmediateHttpResponse
from dash_and_do.htmx import hx_redirect_success

# Local Libraries: Dash and Do
from dash_and_do.htmx import is_htmx
from dash_and_do.settings import LOGIN_REDIRECT_URL
from dash_and_do.settings import LOGOUT_REDIRECT_URL

# Django Libraries
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy

# Local Libraries: Users
from apps.users.debugg import DebugAdapter as Debugg
from apps.users.helpers import get_last_status
from apps.users.helpers import redirect_response
from apps.users.sessions import DashUserSession

# Local Libraries
from .forms import DashLoginForm
from .forms import DashSignupForm

debugr = Debugg()

class FormViews:  # pylint: disable=too-few-public-methods
    """Form Values: Strings."""

    INDEX_REVERSE = 'kore:index'
    VERIFY_REVERSE = 'kore:verify'
    CONFIRM_REVERSE = 'kore:confirm'
    TOGGLE_FRIENDLY = False
    TOGGLE_ERROR = True

    class Login:  # pylint: disable=too-few-public-methods
        """Constants Class for Login FormView."""
        CTXNAME = 'login_form'
        TEMPLATE = 'users/account/login.html'
        PREFIX = 'current'

    class Signup:  # pylint: disable=too-few-public-methods
        """Constants Class for Signup FormView."""
        CTXNAME = 'signup_form'
        TEMPLATE = 'kore/verify.html'
        SUCCESS_URL = 'kore/verify.html'
        CONFIRM_URL = 'account_confirm_email.html'
        PREXIX_KEY = 'prefix'
        PREFIX_UNBOUND = 'new'
        PREFIX_BOUND = 'data'
        SUCCESS_MESSAGE = ('Please check your email to '
                           'activate your account.')
        UNEXPECTED_FRIENDLY = ('An unexpected issue occurred during '
                               'registration. Please try again later.')

    class Confirm:  # pylint: disable=too-few-public-methods
        """Constants Class for Signup FormView."""
        CTXNAME = 'confirm_view'
        TEMPLATE = 'kore/confirm.html'
        PREFIX = 'confirm'
        EMAIL_CTXKEY = 'email'
        IS_CTXCONFIRM = 'can_confirm'


    class LogoutView:  # pylint: disable=too-few-public-methods
        """Constants Class for LogoutView."""
        TEMPLATE = 'users/account/logout.html'

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


class HTTP:  # pylint: disable=too-few-public-methods
    """HTTP Headers: Strings."""

    REDIRECTS = True
    REDIRECTS_OFF = False

    class Headers:  # pylint: disable=too-few-public-methods
        """HTTP Headers: Strings."""
        HX_REDIRECT = 'HX-Redirect'
        HTTP_LOCATION = 'Location'
        HX_CONTENT_TYPE = 'Content-Type'
        HX_CONTENT_FORMAT = 'text/html'

    class  Methods:
        """HTTP Methods: Strings."""
        GET = 'GET'
        POST = 'POST'
        PUT = 'PUT'

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

    def post(self, request,  *args, **kwargs):
        """Post method for the SignupView class.

        :param request: The HTTP request object.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: An HTTP response | HTTP Redirect object(s).
        """
        super().post(request, *args, **kwargs)
        form = DashSignupForm(request.POST)
        # Check if form is valid, redirect to success_url
        if form.is_valid():
            # Process the data, create user, etc.
            return HttpResponseRedirect(self.get_success_url())

        # If form is not valid, re-render the form with error messages
        signup_context = {FormViews.Signup.CTXNAME: form}
        return render(request, FormViews.Signup.TEMPLATE, signup_context)

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        # Here you can add your custom logic before the user instance is saved
        # handle validation here...
        # ??
        # Call the parent class's method to handle the saving and redirection
        # logic
        response = super().form_valid(form)
        # You can also add any logic that you want to execute after the user
        # instance is saved
        # Link Request to custom session control: 1) Valid Email, 2) Flags
        session_data = DashUserSession(self.request)
        session_data.set_email(form.cleaned_data["email"])
        session_data.set_verification_flags(SessionVals.VALID)
        # For example, if you want to send a custom success message:
        messages.success(self.request, FormViews.Signup.SUCCESS_MESSAGE)
        return hx_redirect_success(self.request,
                                         response,
                                         self.success_url)

    def form_invalid(self, form):
        """If the form is invalid, return the form with error
        messages to HTMX.
        """
        signup_context =  {FormViews.Signup.CTXNAME:
                                       form}
        form_html = render_to_string(self.template_name,
                                     signup_context,
                                     request=self.request)
        raise ImmediateHttpResponse(HttpResponse(form_html))

    def get_context_data(self):
        """Addto session_data to context_data

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

        Uses a proxy (the reverse_lazy() function) to future proof changes
        Uses a constant to have strings configured elsewhere
        :return: A string representing the success URL from namespace URL.
        """
        # Redirect the user to the verification page
        return reverse_lazy(FormViews.VERIFY_REVERSE)


class DashLoginView(LoginView):
    """DashLoginView from Django AllAuth LoginView.

    :param template_name: The name of the template to be rendered.
    :param success_url: The URL to redirect to upon successful response.
    :param form_class: The form class for rendering the login form.
    :param redirect_field_name: The name of the redirect field.
    :param extra_context: Additional context data to be passed to the template.
    :param initial: Initial data for the form.
    """

    template_name = FormViews.Login.TEMPLATE  # specify your own template
    success_url = LOGIN_REDIRECT_URL  # Heads back to index
    form_class = DashLoginForm

    def get(self, request, *args, **kwargs):
        """Checks and directs user to a private index if authenticated.
        Retrieve the login view.

        :param request: The HTTP request object.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: An HTTP response object.

        """
        if request.user.is_authenticated:
            return HttpResponseRedirect(LOGIN_REDIRECT_URL)
        return super().get(request, *args, **kwargs)

    def get_form(self, form_class=None):
        """:param form_class: (optional)
            The form class for rendering the login form.
            If not specified, the default form class for the view will be used.
        :return: The instantiated form object
            with the necessary form arguments and prefix.

        This method is responsible for returning the login form to be rendered
        in the view. The `form_class` parameter is optional, and if not
        specified, the default form class for the view will be used.
        The form object is instantiated with the necessary form arguments
        and prefix for proper rendering.

        Example usage:

            form = self.get_form()
            # Use the retrieved form object for further processing
        """
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(**self.get_form_kwargs(),
                          prefix=FormViews.Login.PREFIX)

    def get_context_data(self, **kwargs):
        """Gets and sets a context form variable for the login form.
        :param kwargs: additional keyword arguments
        :return: dictionary with context data.

        This method adds additional context data to the view.
        It returns a dictionary with the updated context data.
        Assigned the signup form to the CTX login_form variable.

        Example usage:
            context = self.get_context_data(foo='bar')
            # context: {'foo': 'bar', ...}

        Note: This method is a part of the DashLoginView class.
        """
        context = super().get_context_data(**kwargs)
        context[FormViews.Login.CTXNAME] = self.get_form()
        return context

    def form_valid(self, form):  # noqa ARG002
        """Process the valid form data.

        :param form: Form containing the data submitted by the user.
        :return: An HTTP response redirecting to the success URL.

        Validates the form data submitted by the user during the login process.
        If the request is made via HX (Hypertext Transfer Protocol),
            it redirects to the success URL using the HX_REDIRECT header.
        Otherwise,
            it redirects to the success URL using the HTTP_LOCATION header.
        """
        context = self.get_context_data()

        if is_htmx(self.request):
            return redirect_response(self.request,
                                     self.template_name, context,
                                     self.success_url,
                                     HTTP.Headers.HX_REDIRECT)

        return redirect_response(self.request,
                                 self.template_name, context,
                                 self.success_url,
                                 HTTP.Headers.HTTP_LOCATION)


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
    template_name = 'kore/confirm.html'
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
        # Update the old session email data => confirm email if can_confirm
        # Use the super's can_confirm bool to set the verification flags
        # AllAuth.account.views.ConfirmEmailView line 432
        if context[FormViews.Confirm.IS_CTXCONFIRM]:
            session_data.set_email(context[FormViews.Confirm.EMAIL_CTXKEY])
            # So True: Email is valid, confirm sent, and can_confirm: True
            # Ti's over kill, and is tech debt: byt can_confirm is per view.
            # While sessions are across viewa: for session control/history
            session_data.set_verification_flags(SessionVals.VALID,
                                                SessionVals.CONFIRMED,
                                                SessionVals.VERIFIED)
        else:
            # So True: Email is valid, and confirm sent, but can_confirm: False
            session_data.set_verification_flags(SessionVals.VALID,
                                                SessionVals.CONFIRMED,
                                                SessionVals.NOTVERIFIED)
        return context
