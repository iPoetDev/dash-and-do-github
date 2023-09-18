#!/user/bin/env python3
"""
This module contains the views for the core app.

    @File: views.py
    @Version: 0.3.0 to 0.3.0.?
    @Desc: apps | core |  views
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/08/07
    @Date Modified: 23/09/12
    @Python Version: 3.11.04
    @Django Version: 4.2.3
    @Notes / Ideas v Implement:
    @Changelog:
    - noted: Use function based views for the core app.
    - added: login_required decorator to all puiblic views
    - added: login_required decorator to all private views
"""
# Django Imports
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed
from django.template.response import TemplateResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

# Local: Project Imports
from dash_and_do.htmx import is_htmx
from dash_and_do.logger import log_views_request, log_views_response
# Local: App Imports
from .forms import ContactForm
from .http import (contact_email, contact_http_response)
from .email.emails import send_mail_contact

class HTTP:
    """
    HTTP Methods
    """
    GET = 'GET'
    POST = 'POST'


class Template:
    """
    Template Paths
    """
    HOME = 'index.html'
    CONTACT = '/all/form_contact.html'


class Ctx:
    """
    Context Variables
    """
    FORM = 'form'


class SiteMeta:
    """
    Site Meta Data
    TITLE = 'title'
    URL = 'url'
    PERSON = 'person'
    DESCRIPTION = 'description'
    KEYWORDS = 'keywords'
    CONTACT = 'contact'
    """
    NAME = 'Dashboard and Do GitHub Manager'
    URL = 'https://dash-and-do.herokuapp.com/'
    PERSON = 'Charles J Fowler, @iPoetDev.github.com'
    DESC = 'A GitHub Portfolio Manager for the Dashboard and Do '
    KEYWORDS = 'GitHub, Portfolio, Manager, Dashboard, Do, '
    CONTACT = 'Github: @iPoetDev'

class Brand:
    """
    Brand Names
    """
    class Site:
        """
        Site Brand Names
        """
        NAME = 'Dashboard and Do GitHub Manager'
        SHORT_NAME = 'Dash and Do'
        LOGO = 'dash_and_do/logo.png'
        LOGO_ALT = 'Dash and Do Logo'
        LOGO_TITLE = 'Dash and Do Logo'
        FAVICON = 'dash_and_do/favicon.ico'
        FAVICON_ALT = 'Dash and Do Favicon'
        FAVICON_TITLE = 'Dash and Do Favicon'

class Page:
    """
    Page Titles
    """
    class Index:
        """
        Index Page Details
        """
        USE = 'all'
        TITLE = 'Home: Dashboard and Do GitHub Manager'
        ATITLE = 'Home: Dashboard and Do GitHub Manager'
        ATEXT = 'Home'
    class About:
        """
        About Page Details | Static
        """
        USE = 'menu_public'
        TITLE = 'About: Dashboard and Do GitHub Manager'
        ATITLE = 'About: Dashboard and Do GitHub Manager'
        ATEXT = 'About'

    class Contact:
        """
        Contact Section Partial/Fragment Details
        """
        USE = 'menu_public'
        TITLE = 'Contact: Dashboard and Do GitHub Manager'
        ATITLE = 'Contact Us: Send an Message to Dash and Do'
        ATEXT = 'Contact'

    class AccountMenu:
        """
        Account Menu Details
        """
        USE = 'menu_private'
        MENU_TITLE = 'Accounts Menu'
        ACCOUNT_BUTTEXT = 'Account'
        PROFILE_ATITLE = 'Accounts: View your account profile'
        PROFILE_ATEXT = 'Profile'
        GITHUB_ATITLE = 'GitHub: Connect GitHub to your profile'
        GITHUB_ATEXT = 'Connect'
        SETTINGS_ATITLE = 'Settings: Manwge your profile'
        SETTINGS_ATEXT = 'Settings'
        LOGOUT_ATITLE = 'Logout: Sign Out of your profile'
        LOGOUT_ATEXT = 'Logout'

class Log:
    """
    Log Messages
    """
    INDEX = 'Index'
    CONTACT_FORM = 'Contact Form'

    class Desc:
        """
        Log Descriptions
        """
        COMPLETED_FORM = 'Completed Form: Valid & POST',
        BOUNDED_FORM = 'Bounded: Invalid Form & POST',
        UNBOUND_FORM = 'Unbounded: Empty Form: Method != POST'
# ====================== Home Page Views ===========================

@xframe_options_sameorigin
@ensure_csrf_cookie
@csrf_protect
def index(request):
    """
    Index view. | Access: All Users
    :param request: The HTTP request object.
    :return: None
    :raises: None
    """
    # Don't' not use constants in tag labels within the context
    # Use constants for the context values
    context = {
        'site': SiteMeta.NAME,
        'indextitle': Page.Index.TITLE,
        'siteurl': SiteMeta.URL,
        'siteperson': SiteMeta.PERSON,
        'sitedesc': SiteMeta.DESC,
        'sitekeywords': SiteMeta.KEYWORDS,
        'sitecontact': SiteMeta.CONTACT,
        'brand': Brand,
        'page': Page
    }
    log_views_request(request, label=Log.INDEX)
    # Template.HOME is 'index.html' - is a Class.CONSTANT value format/abstract
    return render(request, Template.HOME, context)


# ====================== All | Public Form Views ===========================
"""
@Changelog:
 - added: 23-09-12
    """


@require_http_methods([HTTP.POST])
@ensure_csrf_cookie
@csrf_protect
def form_contact(request):  # sourcery skip: dict-assign-update-to-union
    """
    Form contact view. | Access: All Users
    Checks for HTTP POST request and if the request is htmx.
    Then checks if the form is valid and if so, sends the email.
    If the email is sent successfully, the user is redirected to the
    :param request: The HTTP request object.
    :return: Rendered TemplateResponse for Contact Form
    :rtype: TemplateResponse
    :raises: None
    """
    log_views_request(request, label='Contact Form')
    contact = ContactForm(request.POST or None)
    base_ctx = {}

    if all([request.method == HTTP.POST, contact.is_valid()]):
        # send email, issue a HTTP Response, witn status codes on email state
        response = contact_email(contact, send_mail_contact)
        # Handle a completed Response/HTMX Response
        completed = contact_http_response(request, contact, response,
                                          is_htmx(request))
        completed.context |= base_ctx # merge ctx dict augmented union assigment
        # Log the completed Response
        log_views_response(completed,
                           label=Log.CONTACT_FORM,
                           desc=Log.Desc.COMPLETED_FORM)
        # Render the completed Response for form with status codes
        if completed is not None:
            return completed.render()

    elif request.method == HTTP.POST and not contact.is_valid():
        # If form validation fails, return the form data with errors
        if contact.data:
            bounded_ctx = {Ctx.FORM: contact}
            # Update the context with the base context
            bounded_ctx |= base_ctx # merge ctx dict augmented union assigment
            # Reply with a 400 - Bad Request bounded Form Response
            bounded = TemplateResponse(request, Template.CONTACT, bounded_ctx,
                                       status=HttpResponseBadRequest.status_code)
            # Log the bounded Response
            log_views_response(bounded,
                               label=Log.CONTACT_FORM,
                               desc=Log.Desc.BOUNDED_FORM)
            # Render the bounded Response for invalid form with Bed Request
            # status
            return bounded.render()

    # If the reqeust is has no data, or if nothing POST
    if contact.data is None or request.method != HTTP.POST:
        # If the form data is empty or not HTTP POST, create a new form.
        contact = ContactForm()
        unbounded_ctx = {Ctx.FORM: contact}
        unbounded_ctx |= base_ctx # merge ctx: dict augmented union assigment
        # Reply with a 405 - Method Not Allowed unbounded Form Response
        unbounded = TemplateResponse(request, Template.CONTACT, unbounded_ctx,
                                     status=HttpResponseNotAllowed.status_code)
        # Log the unbounded Response
        log_views_response(unbounded,
                           label=Log.CONTACT_FORM,
                           desc=Log.Desc.UNBOUND_FORM)
        # Render the unbounded Response for empty form with Method Not Allowed
        return unbounded.render()


# ====================== Only | Public Form Views ===========================

"""
@Changelog:
 - added: 23-09-12
"""


@require_http_methods([HTTP.POST])
@ensure_csrf_cookie
@csrf_protect
@never_cache
def form_signup(request):
    """
    Form for Signup
    Decorator to check if the user is logged in before executing the
    form_signup function.

    :param request: The HTTP request object.

    :return: None

    :raises: None
    """
    pass


"""
@Changelog:
 - added: 23-09-12
"""


@require_http_methods([HTTP.POST])
@ensure_csrf_cookie
@csrf_protect
@never_cache
def form_login(request):
    """
    Use decorator that checks if the user is authenticated before allowing access
    to the function.

    :param request: The HTTP request object.
    :return: None
    :exceptions: None
    """
    pass


@require_http_methods([HTTP.POST])
@ensure_csrf_cookie
@csrf_protect
@never_cache
def form_reset(request):
    """
    Use decorator that checks if the user is authenticated before allowing access
    to the function.

    :param request: The HTTP request object.
    :return: None
    :exceptions: None
    """
    pass
