"""
This module contains the views for the kore app.

    @File: views.py
    @Version: 0.3.0 to 0.3.0.?
    @Desc: apps | kore |  views
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/08/07
    @Date Modified: 23/09/12
    @Python Version: 3.11.04
    @Django Version: 4.2.3
    @Notes / Ideas v Implement:
    @Changelog:
    - noted: Use function based views for the kore app.
    - added: login_required decorator to all puiblic views
    - added: login_required decorator to all private views
"""
import traceback

# Django HTTP Imports
from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.template.response import TemplateResponse
# Django Imports
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_http_methods
# Django View Imports
from django.views.defaults import page_not_found as dj_page_not_found
# Third Party Imports
from django_htmx.middleware import HtmxDetails

# Local: Project Imports
from dash_and_do.htmx import is_htmx
from dash_and_do.settings import DEBUG
# Local: Kore
from apps.kore.corehttp import (contact_email_response, contact_http_response,
                                switch_form)
from apps.kore.emailing.emails import send_mail_contact2
# Local: App Imports
from apps.kore.forms import ContactForm
from apps.kore.helpers import (pp_response,
                               pp_label)
from apps.kore.values import (SiteMeta, Brand, Page, Template, HTTP, Forms)
# Local: Users Forms
from apps.users.views import DashSignupView, DashLoginView
from apps.users.forms import DashSignupForm, DashLoginForm
# OopCompanion:suppressRename

# ====================== Home Page Views ===========================

# https://github.com/adamchainz/django-htmx/blob/main/example/example/views.py
# Typing pattern recommended by django-stubs:
# https://github.com/typeddjango/django-stubs#how-can-i-create-a-httprequest-thats-guaranteed-to-have-an-authenticated-user
class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails


@xframe_options_sameorigin
# @ensure_csrf_cookie
# @csrf_protect
@require_GET
def index(request):
    """
    Index view. | Access: All Users
    :param request: The HTTP request object.
    :return: None
    :raises: None
    """
    # Don't' not use constants in tag labels within the context
    # Use constants for the context values
    login = DashLoginForm(prefix='current')
    signup = DashSignupForm(prefix='new')
    contact = ContactForm(prefix='sitemessage')

    context = {
        'site': SiteMeta.NAME,
        'indextitle': Page.Index.TITLE,
        'siteurl': SiteMeta.URL,
        'siteperson': SiteMeta.PERSON,
        'sitedesc': SiteMeta.DESC,
        'siteright': SiteMeta.COPY,
        'sitekeywords': SiteMeta.KEYWORDS,
        'sitecontact': SiteMeta.CONTACT,
        'brand': Brand,
        'page': Page,
        'contact_form': contact,  # Render initial clear form on Get
        'signup_form': signup,  # Render initial clear form on Get
        'login_form': login,  # Render initial clear form on Get
        'contactname': contact.fields[ 'name' ],
        'contactemail': contact.fields[ 'email' ],
        'contactmessage': contact.fields[ 'message' ],
        'contactcopy': contact.fields[ 'copy_sent' ],
    }
    pp_label(label='Index: ContactForm')
    # Template.HOME is 'index.html' - is a Class.CONSTANT value format/abstract
    # response = TemplateResponse(request, Template.HOME, context)
    # Check for HTMX request
    # if is_htmx(request):
    #     # HTMX enabled response
    #     # HTMX for header to update the url in the browser's address bar
    #     response[ 'HX-Current-Url' ] = request.get_full_path()
    # Render the templated response for index.html
    return render(request, Template.HOME, context)


# def menu_public_context(request):
#     """
#     Public Menu Context. | Access: All Users
#     :param request: The HTTP request object.
#     :return: None
#     :raises: None
#     """
#     context = {}
#     log_views_request(request, label=Log.INDEX)
#     return render(request, Template.MENU_PUBLIC, context)

# ====================== All | Public Form Views ===========================


@require_http_methods([ HTTP.POST ])
def form_contact(request):  # sourcery skip: dict-assign-update-to-union
    """
    Form contact view. | Access: All Users
    Checks for HTTP POST request and if the request is htmx.
    Then checks if the form is valid and if so, sends the emailing.
    If the emailing is sent successfully, the user is redirected to the
    :param request: The HTTP request object.
    :return: Rendered TemplateResponse for Contact Form
    :rtype: TemplateResponse
    :raises: None
    """
    contact = ContactForm(request.POST or None,
                          prefix='contact')
    base_ctx = {}
    if contact.is_valid() and request.method == HTTP.POST:
        # send emailing, issue a HTTP Response,
        # with status codes on emailing state
        # - debugged: OK: 2023-09-22 23:00:00
        response = contact_email_response(contact,
                                          send_mail_contact2)
        # Handle a completed Response/HTMX Response
        pp_response(response, '1: View: contact_email response')
        # response
        if response is not None and response.status_code == 200:
            contact.save()
            contact = ContactForm()
            pp_response(response, '2: View: contact_email: SUCCESS')
            print(f'contact_email: SUCCESS: {response.serialize()}')
            # corehttp.py: contact_http_response
            completed: TemplateResponse = contact_http_response(request,
                                                                contact,
                                                                response,
                                                                is_htmx(
                                                                    request))
            # Render the completed Response for form with status codes
            if completed is None:
                # Geneate a 404
                pp_label(
                    label='form_contact: ContactForm: Completed is None')
                raise Http404("Contact Form: Response is None.")
            else:
                # Render a completed form i.e. a new unbounded form
                contact = ContactForm()
                base_ctx = {Forms.CONTACT: contact}
                pp_label(
                    label='form_contact: ContactForm: Completed')
                return render_completed_form(request, completed,
                                             base_ctx, 'form_contact')
        elif response is not None:
            pp_label(label='3: View: contact_email: Response is not 200')
            # Render the bounded Response for user to try again
            render_bounded_form(request, contact,
                                Forms.CONTACT, base_ctx)

        else:
            pp_label(label='4: View: contact_email: Response is None')
            contact = ContactForm()
            render_unbounded_form(request, contact,
                                  Forms.CONTACT, base_ctx)

    elif (not contact.is_valid() and contact.data and request.method ==
          HTTP.POST):
        pp_label(label='5: form_contact: ContactForm: Invalid')
        contact = ContactForm()
        return render_bounded_form(request, contact,
                                   Forms.CONTACT, base_ctx)

    # If the reqeust is has no data, or if nothing POST
    if contact.data is None or request.method != HTTP.POST:
        # If the form data is empty or not HTTP POST, create a new form.
        pp_label(label='6: form_contact: ContactForm: Empty & Not POST')
        contact = ContactForm()
        render_unbounded_form(request, contact,
                              Forms.CONTACT, base_ctx)


def switch_views(label):
    """
    Switch the view by label.
    :param label:
    :return:
    """
    viewformlookup = {
        'form_contact': Forms.CONTACT,
        'form_signup': Forms.SIGNUP,
        'form_login': Forms.LOGIN,
        'form_reset': Forms.PASSWORD_RESET,
        'form_password_change': Forms.PASSWORD_CHANGE,
        'form_profile': Forms.PROFILE,
        'form_github': Forms.GITHUB,
        'form_settings': Forms.SETTINGS,
    }
    return viewformlookup.get(label)


def render_completed_form(request,
                          response: TemplateResponse,
                          base_ctx: dict,
                          viewname: str = 'form_contact') -> TemplateResponse:
    """
    Render the completed form.
    """
    view = switch_views(viewname)
    pp_response(response, f'view: {view}: completed http response')
    # Render the completed Response for form with status codes
    context = response.context_data
    context.update(base_ctx)  # merge base_ctx dict with original context data
    return TemplateResponse(request,
                            template=response.template_name,
                            context=context,
                            status=response.status_code)


def render_bounded_form(request, form, label,
                        ctx, state_us=HTTP.STATUS.BAD_REQUEST) \
    -> TemplateResponse:
    """
    Render the bounded form.
    :param request: The HTTP request object.
    :param form: Form (Bounded or Unbounded)
    :param label: Form Label
    :param state_us: Response Status Code: Prior response current status
    :param ctx: Base Context
    :return: Rendered TemplateResponse for Contact Form
    :rtype: TemplateResponse
    :raises: None
    """
    # Switch the Context form's name/per context render by form label's key.
    form_key = switch_form(label)
    # Assign the form to the context
    bounded_ctx = {form_key: form}
    bounded_ctx |= ctx  # merge ctx: dict augmented union assigment
    # Reply with 400 for form validation error on bounded forms, or the
    # contingent status code from the emailing response
    bounded = TemplateResponse(request, Template.CONTACT, bounded_ctx,
                               status=state_us or HTTP.STATUS.BAD_REQUEST)
    # Render the bounded Response for form validation errors
    return bounded.render()


def render_unbounded_form(request, form, label,
                          ctx, state_us=HTTP.STATUS.OK) \
    -> TemplateResponse:
    """
    Render the unbounded form.
    :param request: The HTTP request object.
    :param form: Form (Bounded or Unbounded)
    :param label: Form Label
    :param ctx: Base Context
    :param state_us: Response Status Code: Prior response current status
    :return: Rendered TemplateResponse for Contact Form
    :rtype: TemplateResponse
    :raises: None
    """
    # Switch the Context form's name/per context render by form label's key.
    form_key = switch_form(label)
    # Assign the form to the context
    unbounded_ctx = {form_key: form}
    unbounded_ctx |= ctx  # merge ctx: dict augmented union assigment
    unbounded = TemplateResponse(request,
                                 Template.CONTACT,
                                 unbounded_ctx,
                                 status=state_us or HTTP.STATUS.OK)
    # Render the unbounded Response for empty form with Method Not Allowed
    return unbounded.render()


# ====================== Only | Public Form Views ===========================


@require_http_methods([ HTTP.POST ])
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


@require_http_methods([ HTTP.POST ])
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


@require_http_methods([ HTTP.POST ])
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


@require_GET
def favicon(request: HtmxHttpRequest) -> HttpResponse:
    """
    Credit: github.com/adamchainz/django-htmx (as above)
    - TODO: Update to own favicon
    Favicon view. | Access: All Users
    :param request:
    :return:
    """
    return HttpResponse(
        (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
            + '<text y=".9em" font-size="90">🦊</text>'
            + "</svg>"
        ),
        content_type="image/svg+xml",
    )


@require_GET
# def csrf_demo(request: HtmxHttpRequest) -> HttpResponse:
#     """
#
#     :param request:
#     :return:
#     """
#     return render(request, "csrf-demo.html")

def core_page_not_found(request, exception) -> HttpResponse:
    """
    404 Page Not Found view. | Access: All Users | Handler404 in urls.py
    :param request:
    :param exception:
    :return:
    """
    try:
        stack_trace = traceback.format_exc() if DEBUG else ''
        context = {
            'message': 'Page not found',
            'verbose': 'Sorry, but the page you were trying to view does not '
                       'exist.',
            'trace': stack_trace,
        }
        return render(request,
                      Template.PAGE_NOT_FOUND,
                      context,
                      status=404)
    except Exception:
        # If something goes wrong, fall back to the
        # default Django page not found view
        return dj_page_not_found(request, exception)
