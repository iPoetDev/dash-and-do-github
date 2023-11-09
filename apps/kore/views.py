"""This module contains the views for the kore app.

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
import logging
import traceback

# Django HTTP Imports
from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
# Django Imports
from django.shortcuts import render
from django.template.response import TemplateResponse
# from django.views.decorators.cache import never_cache  # TODO
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_protect
# TODO
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_http_methods
# Django View Imports
from django.views.defaults import page_not_found as dj_page_not_found
# Third Party Imports
from django_htmx.middleware import HtmxDetails

# Local: Kore
from apps.kore.corehttp import contact_email_response
from apps.kore.corehttp import contact_http_response
from apps.kore.corehttp import switch_form
from apps.kore.emailing.emails import send_mail_contact2
# Local: App Imports
from apps.kore.forms import ContactForm
from apps.kore.helpers import pp_label
from apps.kore.helpers import pp_response
from apps.kore.values import Brand
from apps.kore.values import Forms
from apps.kore.values import HTTP
from apps.kore.values import Page
from apps.kore.values import SiteMeta
from apps.kore.values import Template
# Local: Users Forms
from apps.users.forms import DashLoginForm
from apps.users.forms import DashSignupForm
# Local: Project Imports
from dash_and_do.htmx import is_htmx
from dash_and_do.settings import DEBUG


# Local: Users Values


# OopCompanion:suppressRename

# ====================== Home Page Views ===========================

# https://github.com/adamchainz/django-htmx/blob/main/example/example/views.py
# Typing pattern recommended by django-stubs:
# https://github.com/typeddjango/django-stubs#how-can-i-create-a-httprequest-
# thats-guaranteed-to-have-an-authenticated-user
class HtmxHttpRequest(HttpRequest):
    """HTMX HTTP request.

    A HttpRequest that is guaranteed to have an authenticated user.
    """
    htmx: HtmxDetails


class SiteContext:
    """Site Context."""

    @property
    def context(self):
        """Provides the context data for use in all full page views.

        :return: A dictionary containing the full page views's context data .
            - 'sitename': The name of the site (SiteMeta.NAME).
            - 'siteurl': The url of the site (SiteMeta.URL).
            - 'siteperson': The person of the site (SiteMeta.PERSON).
            - 'sitedesc': The description of the site (SiteMeta.DESC).
            - 'siteright': The rights of the site (SiteMeta.COPY).
            - 'sitekeywords': The keywords of the site (SiteMeta.KEYWORDS).
            - 'sitecontact': The contact of the site (SiteMeta.CONTACT).
            - 'website': The website of the site (SiteMeta).
            - 'brand': The brand of the site (Brand).
            - 'page': The page of the site (Page).
        """
        return {
            'sitename': SiteMeta.NAME,
            'siteurl': SiteMeta.URL,
            'siteperson': SiteMeta.PERSON,
            'sitedesc': SiteMeta.DESC,
            'siteright': SiteMeta.COPY,
            'sitekeywords': SiteMeta.KEYWORDS,
            'sitecontact': SiteMeta.CONTACT,
            'website': SiteMeta,
            'brand': Brand,
            'page': Page
        }

    @property
    def index(self):
        """Provides the context data for the index view.

        :return: A dictionary containing the context data for the index view.
            - 'title': The title of the page (Page.Index.TITLE).
        """
        return {
            'title': Page.Index.TITLE,
        }

    @property
    def verify(self):
        """Provides the context data for the verify view.

        :return: A dictionary containing the context data for the verify view.
            - 'title': The title of the page (Page.Index.TITLE).
        """
        return {
            'title': Page.Verify.TITLE,
        }

    @property
    def confirm(self):
        """Provides the context data for the confirm view.

        :return: A dictionary containing the context data for the confirm view.
            - 'title': The title of the page (Page.Index.TITLE).
        """
        return {
            'title': Page.Confirm.TITLE,
        }


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
                        'template': Template.HOME,
                        'context': context})


@xframe_options_sameorigin
# @ensure_csrf_cookie
@csrf_protect
@require_GET
def index(request):
    """Index view.

    | Access: All Users
    :param request: The HTTP request object.
    :return: None
    :raises: None
    """
    # Don't' not use constants in tag labels within the context
    # Use constants for the context values
    login = DashLoginForm()
    signup = DashSignupForm()
    contact = ContactForm()

    context = {
        'site': SiteMeta.NAME,
        'title': Page.Index.TITLE,
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
        'contactname': contact.fields['name'],
        'contactemail': contact.fields['email'],
        'contactmessage': contact.fields['message'],
        'contactcopy': contact.fields['copy_sent'],
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
    if DEBUG:
        # Log the template
        log_template('Index',
                     request,
                     context,
                     Template.HOME)
    # Return the rendered response
    return render(request,
                  Template.HOME,
                  context)
    # print(str(ret.content, 'utf-8'))


@xframe_options_sameorigin
@csrf_protect
@require_GET
def verify_public(request):
    """Verify view.

    | Access: All Users
    :param request: The HTTP request object.
    :return: None
    :raises: None
    """
    site_ctx = sitecontext.context
    verify_ctx = sitecontext.verify
    context = {
        # **site_ctx,
        **verify_ctx,
    }
    if DEBUG:
        log_template('Verify',
                     request,
                     context,
                     Template.VERIFY)
    return render(request, Template.VERIFY,
                  context)


@xframe_options_sameorigin
@csrf_protect
@require_GET
def confirm_public(request):
    """Confirm view.

    | Access: All Users
    :param request: The HTTP request object.
    :return: None
    :raises: None
    """
    site_ctx = sitecontext.context
    confirm_ctx = sitecontext.confirm
    context = {
        **site_ctx,
        **confirm_ctx,
    }
    if DEBUG:
        log_template('Confirm',
                     request,
                     context,
                     Template.CONFIRM)
    return render(request, Template.CONFIRM,
                  context)


# ====================== All | Public Form Views ===========================


@require_http_methods([HTTP.POST])
def form_contact(request):  # sourcery skip: dict-assign-update-to-union
    """Form contact view.

    | Access: All Users Checks for HTTP POST request and if the request
    is htmx. Then checks if the form is valid and if so, sends the
    emailing. If the emailing is sent successfully, the user is
    redirected to the
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
        if response is not None and response.status_code == HTTP.STATUS.OK:
            contact.save()
            contact = ContactForm()
            # # pp_response(response, '2: View: contact_email: SUCCESS')
            # print(f'contact_email: SUCCESS: {response.serialize()}')
            # corehttp.py: contact_http_response
            completed: TemplateResponse = contact_http_response(request,
                                                                contact,
                                                                response,
                                                                is_htmx(
                                                                    request))
            # Render the completed Response for form with status codes
            if completed is None:
                # Geneate a 404
                # pp_label(
                #     label='form_contact: ContactForm: Completed is None')
                raise Http404(HTTP.MESSAGES.NOT_FOUND)

            # Render a completed form i.e. a new unbounded form
            contact = ContactForm()
            base_ctx = {Forms.CONTACT: contact}
            # pp_label(
            #     label='form_contact: ContactForm: Completed')
            return render_completed_form(request, completed,
                                         base_ctx, 'form_contact')
        elif response is not None:  # noqa RET505
            # pp_label(label='3: View: contact_email: Response is not 200')
            # Render the bounded Response for user to try again
            render_bounded_form(request, contact,
                                Forms.CONTACT, base_ctx)

        # pp_label(label='4: View: contact_email: Response is None')
        contact = ContactForm()
        render_unbounded_form(request, contact,
                              Forms.CONTACT, base_ctx)

    elif (not contact.is_valid() and contact.data and request.method ==
          HTTP.POST):
        # pp_label(label='5: form_contact: ContactForm: Invalid')
        contact = ContactForm()
        return render_bounded_form(request, contact,
                                   Forms.CONTACT, base_ctx)

    # If the reqeust is has no data, or if nothing POST
    # contact.data is None or request.method != HTTP.POST:
    # If the form data is empty or not HTTP POST, create a new form.
    # pp_label(label='6: form_contact: ContactForm: Empty & Not POST')
    contact = ContactForm()
    render_unbounded_form(request, contact,
                          Forms.CONTACT, base_ctx)
    return None


def switch_views(label):
    """Switch the view by label.

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


# noinspection PySameParameterValue
def render_completed_form(request,
                          response: TemplateResponse,
                          base_ctx: dict,
                          viewname: str = Forms.CONTACT) -> TemplateResponse:
    """Render the completed form."""
    switch_views(viewname)
    # pp_response(response, f'view: {view}: completed http response')
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
    """Render the bounded form.

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
    """Render the unbounded form.

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


@require_GET
def favicon(request: HtmxHttpRequest) -> HttpResponse:  # noqa: E501,ARG001
    """Credit: github.com/adamchainz/django-htmx
    TODO: Update to own favicon
    Favicon view. | Access: All Users
    :param request:
    :return:
    """
    xmlns = Brand.FAVICON.XMLNS
    viewbox = Brand.FAVICON.VBOX
    viewy = Brand.FAVICON.VIEWY
    fontsize = Brand.FAVICON.FONTSIZE
    icon = Brand.FAVICON.ICON
    content = Brand.FAVICON.FORMAT
    svg_template = \
        f'''
        <svg xmlns="{xmlns}" viewBox="{viewbox}">
            <text y="{viewy}" font-size="{fontsize}">{icon}</text>
        </svg>
    '''

    return HttpResponse(svg_template, content_type=content)


@require_GET
# def csrf_demo(request: HtmxHttpRequest) -> HttpResponse:
#     """
#
#     :param request:
#     :return:
#     """
#     return render(request, "csrf-demo.html")

def core_page_not_found(request, exception) -> HttpResponse:
    """404 Page Not Found view.

    | Access: All Users | Handler404 in urls.py
    :param request:
    :param exception:
    :return:
    """
    # noinspection PyBroadException
    try:
        stack_trace = traceback.format_exc() if DEBUG else ''
        context = {
            'message': 'Page not found',
            'verbose': 'Sorry, but the page you were trying to view does not '
                       'exist.',
            'trace': stack_trace,
        }
        return render(request,
                      Template.COREPAGE_NOT_FOUND,  # 'kore/404.html'
                      context,
                      status=HTTP.STATUS.NOT_FOUND)  # 404
    except Exception:  # pylint: disable=broad-except
        # If something goes wrong, fall back to the
        # default Django page not found view
        return dj_page_not_found(request, exception)
