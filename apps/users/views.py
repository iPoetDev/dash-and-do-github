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
from allauth.account import app_settings
from allauth.account.utils import complete_signup
from allauth.account.views import ConfirmEmailView
from allauth.account.views import LoginView
from allauth.account.views import LogoutView
from allauth.account.views import SignupView
from allauth.exceptions import ImmediateHttpResponse

# Django Libraries
from django.http import HttpResponseRedirect

# Local Libraries: Dash and Do
from dash_and_do.htmx import is_htmx
from dash_and_do.settings import LOGIN_REDIRECT_URL
from dash_and_do.settings import LOGOUT_REDIRECT_URL

# Local Libraries: Users
from apps.users.forms import DashLoginForm
from apps.users.forms import DashSignupForm
from apps.users.helpers import redirect_response


class FormViews:  # pylint: disable=too-few-public-methods
    """Form Values: Strings."""

    class Login:  # pylint: disable=too-few-public-methods
        """ Constants Class for Login FormView.

        """
        CTXNAME = 'login_form'
        TEMPLATE = 'users/account/login.html'
        PREFIX = 'current'

    class Signup:  # pylint: disable=too-few-public-methods
        """ Constants Class for Signup FormView.


        """
        CTXNAME = 'signup_form'
        TEMPLATE = 'users/account/signup.html'
        PREFIX = 'new'

    class Confirm:  # pylint: disable=too-few-public-methods
        """ Constants Class for Signup FormView.


        """
        CTXNAME = 'confirm_view'
        TEMPLATE = 'account/email_confirm.html'
        PREFIX = 'confirm'

    class LogoutView:  # pylint: disable=too-few-public-methods
        """ Constants Class for LogoutView.

        """
        TEMPLATE = 'users/account/logout.html'


class HTTP:  # pylint: disable=too-few-public-methods
    """HTTP Headers: Strings."""

    class Headers:  # pylint: disable=too-few-public-methods
        """ HTTP Headers: Strings.

        """
        HX_REDIRECT = 'HX-Redirect'
        HTTP_LOCATION = 'Location'


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
        context[ FormViews.Login.CTXNAME ] = self.get_form()
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
    template_name = FormViews.LogoutView.TEMPLATE  # specify your own template
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


class DashSignupView(SignupView):
    """- todo: UserPassesTestMixin: test if user is logged in
    - added: get a new form_valid and add prefix to form
    - added: get_context_data to add form to context for signup_form
    - added: form_valid to return a TemplateResponse with HX-Redirect
    - added: form_valid to return a HttpResponse with Location if JS disabled.
    """
    template_name = FormViews.Signup.TEMPLATE  # specify your own template
    success_url = LOGIN_REDIRECT_URL  # Heads back to index
    form_class = DashSignupForm  # Custom AllAuth Signup Form
    login_url = LOGIN_REDIRECT_URL  # Heads back to index

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
        """Gets the form and sets the form prefix.
        :param form_class: (optional)
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
                          prefix=FormViews.Signup.PREFIX)  # form prefix

    def get_context_data(self, **kwargs):
        """Gets and sets a context form variable for the signup form.
        :param kwargs: additional keyword arguments
        :return: dictionary with context data.

        This method adds additional context data to the view.
        It returns a dictionary with the updated context data.
        Assigned the signup form to the CTX signup_form variable.

        Example usage:
            context = self.get_context_data(foo='bar')
            # context: {'foo': 'bar', ...}

        Note: This method is a part of the DashLoginView class.
        """
        context = super().get_context_data(**kwargs)
        # Name the form variable for SPA & Mutli-Form on page
        # clean unbound form
        context[ FormViews.Signup.CTXNAME ] = self.get_form()
        return context

    def form_valid(self, form):
        """Process the valid form data.

        :param form: The validated form data.
        :return: An Template response (HttpResponse)
        :rtype: HttpResponse | TemplateResponse

        Saves the form data and redirects to the success URL.
        """
        form.save(self.request)
        context = self.get_context_data()

        if is_htmx(self.request):
            return redirect_response(self.request,
                                     self.template_name,
                                     context,
                                     self.success_url,
                                     HTTP.Headers.HX_REDIRECT)

        return redirect_response(self.request,
                                 self.template_name,
                                 context,
                                 self.success_url,
                                 HTTP.Headers.HTTP_LOCATION)

    def complete(self):
        """:param self
        :return:
        :rtype: HttpResponse | ImmediateHttpResponse
        """
        try:
            return complete_signup(
                self.request, self.user,
                app_settings.EMAIL_VERIFICATION,
                self.get_success_url())
        except ImmediateHttpResponse as i_h_r_except:
            return i_h_r_except.response


# Write the boilerplatfe for the allauth.account.views.ConfirmEmailView


class DashConfirmEmailView(ConfirmEmailView):
    """Confirm Email View."""

    def get_template_names(self):
        """Get template names."""
        # return your custom template
        return [ FormViews.Confirm.TEMPLATE ]
