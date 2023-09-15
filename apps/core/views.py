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
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed
from django.template.response import TemplateResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

from dash_and_do.htmx import is_htmx
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
    return render(request, Template.HOME)

# ====================== All | Public Form Views ===========================
"""
@Changelog:
 - added: 23-09-12
    """
@require_http_methods([HTTP.POST])
@ensure_csrf_cookie
@csrf_protect
def form_contact(request):
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
    contact = ContactForm(request.POST or None)

    if all([request.method == HTTP.POST, contact.is_valid()]):
        # send email, issue a HTTP Response, witn status codes on email state
        response = contact_email(contact, send_mail_contact)
        # Render a completed Response
        completed = contact_http_response(request, contact, response, is_htmx(request))
        if completed is not None:
            return completed.render()

    if request.method == HTTP.POST and not contact.is_valid():
        # If form validation fails, return the form data with errors
        if contact.data:
            bounded_ctx = {Ctx.FORM: contact}
            # Reply with a 400 - Bad Request bounded Form Response
            bounded = TemplateResponse(request, Template.CONTACT, bounded_ctx,
                                    status=HttpResponseBadRequest.status_code)
            return bounded.render()

    # If the reqeust is has no data, or if nothing POST
    if contact.data is None or request.method != HTTP.POST:
        # If the form data is empty or not HTTP POST
        unbounded_ctx = {Ctx.FORM: contact}
        # Reply with a 405 - Method Not Allowed unbounded Form Response
        unbounded = TemplateResponse(request, Template.CONTACT, unbounded_ctx,
                                    status=HttpResponseNotAllowed.status_code)
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
