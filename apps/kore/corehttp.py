#!/user/bin/env python3
"""
This module contains the views for the kore app.

    @File: corehttp.py
    @Version: 0.3.0 to 0.3.0.?
    @Desc: apps | kore | http
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/09/13
    @Date Modified: 23/09/13
    @Python Version: 3.11.04
    @Django Version: 4.2.3
    @Notes / Ideas v Implement:
    @Changelog:
     - todo:
        - 2023-09-21:
            - contact-htmx-response - per any HTMX response
            - messages - per any response in template response
    - added:
        - 2023-09-13:
            - Initialised file
            - Refactored form_contacts.
            - handle_post_request
    - updated:
        - 2023-09-21:
            - contact-http-response - per any HTTP response
                todo: change name v reuse
            - contact-email-response - per contact form:
            - contact-responses - per contact form
            - template-response: Universial for all responses
    - debugged:
        - 2023-09-21:
            - PARTIALLY: contact-http-response - per any HTTP response
            - contact-email-response - per contact form:
            - contact-responses - per contact form
             - PARTIALLY: template-response: Universial for all responses
    - removed:
        - HttpMessage for HTTP from emailing.values
    - noted: HTTP. Helper functions for handling HTTP requests/responses.
"""
#  Copyright (c) 2023.
# Django Libraries

# OS Libraries
import traceback

from django.http import (HttpResponse,
                         HttpResponseBadRequest,
                         HttpResponseServerError)
from django.template.response import TemplateResponse

from apps.kore.emailing.values import HTTP
from apps.kore.helpers import (pp_label)
from apps.kore.values import (Ctx, Template, Feedback, Signal, Forms)
## Local: Common Libraries
from dash_and_do.settings import DEBUG


# OopCompanion:suppressRename

# class Signal:
#     """
#     Message Levels
#     """
#     INFO = 'info'
#     SUCCESS = 'success'
#     ERROR = 'error'
#     FAIL = False
#
#     class MSG:
#         """
#         Message Levels
#         """
#         DEBUG = messages.DEBUG
#         INFO = messages.INFO
#         SUCCESS = messages.SUCCESS
#         WARNING = messages.WARNING
#         ERROR = messages.ERROR
#         FAIL = False


def contact_http_response(request, form, response, htmx_request) \
    -> TemplateResponse:
    """
    Handles the response in response JS/HTMX is enabled/disabled.
    Progerssive Enhancement failed back.
    :param request: The HTTP request object.
    :param form: A form, saved to to the Database
    :param response: The response from the emailing service.
    :param htmx_request: Boolean value for if the request is htmx.
    :return: Formated tempalated HTTP response with status codes.
     =>   :method: contact_response
     =>   :method: contact_htmx_responses
     =>   :args:
     =>       HTTP request,
     =>       Form: contact,
     =>       HTMX Request Object: Boolean,
     =>       HTTP Response
    :rtype: TemplateResponse or None
    :raises: None
    """
    # Handle the response if it was successful
    if response is not None:
        # Save the form to DB, regardless of the response.
        if htmx_request:
            # - todo: 2023-09-21
            pp_label(f'contact_http_response: htmx_request: {htmx_request}')
            # HTMX Request & Response, JavaScript Enabled
            return contact_htmx_responses(request,
                                          htmx_request,
                                          form,
                                          response)
        else:
            # - debugged: 2023-09-21
            pp_label(f'contact_http_response: Non HTMX: {htmx_request}')
            # Progressive Enahancement, JavaScript Disabled
            return contact_responses(request,
                                     form,
                                     response)
    # - added: 2023-0023: Add a 404 Template'd Response if the response is None
    pp_label(f'contact_http_response: response is None: 404 {response}')
    return render_404(request)


def render_404(request, template_name=Template.COREPAGE_NOT_FOUND) -> (
    TemplateResponse):
    """
    Renders a 404 error page. Adds a stack trace when in debug mode.
    :param request:
    :param template_name:
    :return:
    """
    stack_trace = traceback.format_exc() if DEBUG else ''
    context = {
        'message': 'Response not found',
        'trace': stack_trace
    }
    # Return a 404 response, with the template.
    return TemplateResponse(request,
                            template_name,
                            context,
                            status=404)


def contact_email_response(form, send_mail_func) \
    -> HttpResponse:
    """
    Post Email Handler
    :param form:
    :param send_mail_func:
    :return: HttpResponse or None
    :rtype: HttpResponse or None
    """
    # Pass the contact form data for the emailing.
    # - checked / debugged: 2023-09-21
    email_response = send_mail_func(form)
    print(f'contact_email: email_response: {email_response.content}')
    # for successful emailing
    if email_response.status_code == HTTP.STATUS.OK:
        pp_label(f'contact_email_response: OK  : {email_response}')
        return HttpResponse(HTTP.MSG_SENT,
                            status=200)

    # for invalid header in emailing, signal a bad request
    # Typing for the HTTP response
    elif email_response.status_code == HTTP.STATUS.BAD_REQUEST:
        pp_label(f'contact_email_response: BAD_REQUEST  : {email_response}')
        return HttpResponseBadRequest(HTTP.BAD_REQUEST,
                                      status=400)

    # for invalid header in emailing, signal a bad request
    # Typing for the HTTP response
    elif email_response.status_code == HTTP.STATUS.NOT_FOUND:
        pp_label(f'contact_email_response: NOT_FOUND  : {email_response}')
        return HttpResponseBadRequest(HTTP.NOT_FOUND,
                                      status=404)

    # 500: for failed email servers, Typing for the HTTP response
    elif email_response.status_code == HTTP.STATUS.INTERNAL_SERVER_ERROR:
        pp_label(
            f'contact_email_response: INTERNAL_SERVER_ERROR  : {email_response}')
        return HttpResponseServerError(HTTP.INTERNAL_SERVER_ERROR,
                                       status=500)

    # for other non-defined errors
    else:
        pp_label(f'contact_email_response: UNKNOWN_ERROR  : {email_response}')
        return HttpResponse(HTTP.EMAILERRORS.UNKNOWN_ERROR,
                            status=email_response.status)
    # No None. Code should never reach here.


def contact_htmx_responses(request, htmx_request, contact, response) \
    -> (TemplateResponse or None):
    """
    Resolve HTTP Responses, for HTMX (JS enabled).
    :param request:
    :param htmx_request:
    :param response:
    :param contact
    :return: Formated tempalated HTTP response
     =>   :method: templated_contact_response
     =>   :args:
     =>       HTTP request,
     =>       Form: contact,
     =>       Template.CONTACT: ./form/form_contact.html,
     =>       Signals: Messages.SUCCESS, Messages.ERROR,
     =>       Feedback: EMAILSUCCESS, BADREQUEST, SERVERERROR, EMAILERROR,
     =>       HTTP Response Status Codes: 200, 400, 405, 500
    :rtype: TemplateResponse or None
    """
    # - todo: 2023-09-21
    if all([ response.status_code == 200, htmx_request ]):
        # Successful Email: 200 Ok, Fresh unbounded form.
        pp_label('HTMX: contact_responses: SUCCESS: '
                 f'{response.serialize()}')
        return template_response(request,
                                 contact,
                                 Forms.CONTACT,
                                 Template.CONTACT,
                                 Signal.SUCCESS,
                                 Feedback.EMAILSUCCESS,
                                 response.status_code,
                                 fail=Signal.FAIL)
    elif all([ response.status_code == any([ 400, 403, 405, 410 ]),
               htmx_request ]):
        # Response Codes for
        # 400: Bad Request:         Return bounded form with errors
        # 403: Forbidden:           Return bounded form with errors
        # 405: Method Not Allowed:  Return bounded form with errors
        # 410: Gone:                Return bounded form with errors
        pp_label('contact_responses: BAD REQUEST: '
                 f'{response.serialize()}')
        return template_response(request,
                                 contact,
                                 Forms.CONTACT,
                                 Template.CONTACT,
                                 Signal.ERROR,
                                 Feedback.BADREQUEST,
                                 response.status_code,
                                 fail=Signal.FAIL)
    elif all([ response.status_code == 500, htmx_request ]):
        # Server Error: 500, Return unbounded form with errors
        pp_label('HTMX: contact_responses: SERVER ERROR: New Form '
                 f'{response.serialize()}')
        return template_response(request,
                                 contact,
                                 Forms.CONTACT,
                                 Template.CONTACT,
                                 Signal.ERROR,
                                 Feedback.SERVERERROR,
                                 response.status_code,
                                 fail=Signal.FAIL)
    elif all([ response is None, htmx_request ]):
        # 500: Server Error:     Return unbounded form no errors, clean slate
        # Cover up the server error and return a fresh form, so recovery is
        # seemless to the user.
        pp_label('HTMX: contact_responses: SERVER ERROR: New Form '
                 f'{response.serialize()}')
        return template_response(request,
                                 contact,
                                 Forms.CONTACT,
                                 Template.CONTACT,
                                 Signal.ERROR,
                                 Feedback.EMAILERROR,
                                 HTTP.STATUS.NOT_FOUND,  # 404
                                 fail=Signal.FAIL)
    else:
        # ??: Status Code not defined, Error Unknown
        pp_label('HTMX: contact_responses: response UNKNOWN: '
                 f'{response.serialize}')
        return template_response(request,
                                 contact,
                                 Forms.CONTACT,
                                 Template.CONTACT,
                                 # 'forms/form_contact.html',
                                 Signal.ERROR,
                                 Feedback.EMAILERROR,
                                 response.status_code,  # 404
                                 fail=Signal.FAIL)


def contact_responses(request, contact, response) \
    -> (TemplateResponse or None):
    """
    Resolve HTTP Responses, for Progressive Enhancement (JS disabled).
    :param request:
    :param contact:
    :param response:
    :return: Formated tempalated HTTP response
        :method: template_response
        :args:
            HTTP request,
            Form: contact,
            Template.CONTACT: ./all/form_contact.html,
            Signals: Messages.SUCCESS, Messages.ERROR,
            Feedback: EMAILSUCCESS, BADREQUEST, SERVERERROR, EMAILERROR,
            HTTP Response Status Codes: 200, 400, 405, 500
    :rtype: TemplateResponse or None
    """
    # - debugged: 2023-09-21
    if response.status_code == 200:
        # Successful Email: 200 Ok, Fresh unbounded form.
        pp_label('contact_responses: SUCCESS: '
                 f'{response.serialize()}')
        return template_response(request,
                                 contact,
                                 Forms.CONTACT,
                                 Template.CONTACT,
                                 Signal.MSG.SUCCESS,
                                 Feedback.EMAILSUCCESS,
                                 response.status_code,  # 200
                                 fail=Signal.FAIL)
    elif response.status_code == any([ 400, 403, 405, 410 ]):
        # Response Codes for
        # 400: Bad Request:         Return bounded form with errors
        # 403: Forbidden:           Return bounded form with errors
        # 405: Method Not Allowed:  Return bounded form with errors
        # 410: Gone:                Return bounded form with errors
        pp_label(f'contact_responses: BAD REQUEST: '
                 f'{response.serialize()}')
        return template_response(request,
                                 contact,
                                 Forms.CONTACT,
                                 Template.CONTACT,
                                 Signal.MSG.ERROR,
                                 Feedback.BADREQUEST,
                                 response.status_code,  # 400, 403, 405, 410
                                 fail=Signal.FAIL)
    elif response.status_code == 500:
        # 500: Server Error:     Return unbounded form no errors, clean slate
        # Cover up the server error and return a fresh form, so recovery is
        # seemless to the user.
        pp_label(f'contact_responses: SERVER ERROR: New Form '
                 f'{response.serialize()}')
        return template_response(request,
                                 contact,
                                 Forms.CONTACT,
                                 Template.CONTACT,
                                 Signal.MSG.ERROR,
                                 Feedback.SERVERERROR,
                                 response.status_code,  # 500
                                 fail=Signal.FAIL)
    elif response is None:
        # 404: Not Found when response is None.
        # Allow user to retry the request with form data.
        pp_label('contact_responses: response is None:')
        return template_response(request,
                                 contact,
                                 Forms.CONTACT,
                                 Template.CONTACT,
                                 Signal.MSG.ERROR,
                                 Feedback.EMAILERROR,
                                 HTTP.STATUS.NOT_FOUND,  # 404
                                 fail=Signal.FAIL)
    else:
        # Code should never reach here
        pp_label(f'contact_responses: response UNKNOWN: '
                 f'{response.serialize}')
        return template_response(request,
                                 contact,
                                 Forms.CONTACT,
                                 Template.CONTACT,
                                 Signal.MSG.ERROR,
                                 Feedback.EMAILERROR,
                                 response.status_code,  # 404
                                 fail=Signal.FAIL)


def template_response(request,
                      form,
                      label,
                      template,
                      signal,
                      message,
                      status,
                      fail=True) -> TemplateResponse:
    """

    Creates and returns a TemplateResponse and form associated with a
    HTTP Request, along with a Django signal message and Feedback message,
    per HTTP Response Status Code.

    :param request: HTTP Request
    :param form: Form (Bounded or Unbounded)
    :param label: Form Label: form name to switch / context assignment
    :param template: Template Path
    :param signal: Message Level
    :param message: Custom HTTP Response Message
    :param status: HTTP Response Status Code, Optional
    :param fail: Boolean, Optional, Default: False
    :return: Shared TemplateResponse
    :rtype: TemplateResponse
    """
    # checked / debugged: 2023-09-21

    response_messaages(signal, message, fail)
    # Switch the Context form's name/per context render by form label's key.
    form_key = switch_form(label)
    # Assign the form to the context
    context = {form_key: form}
    # return the form and the template response
    return TemplateResponse(request, template, context, status)


def switch_form(form_label=Forms.GENERIC,
                ctx_formkey=Ctx.GENERIC_FORM) -> dict:
    """
    Form Switch for different contexts.
    :param form_label:
    :param ctx_formkey:
    :return: dictionary lookup key: form key: form name for context
    :rtype: dict
    """
    form_lookup = {
        Forms.CONTACT: Ctx.CONTACT_FORM,
        Forms.LOGIN: Ctx.LOGIN_FORM,
        Forms.SIGNUP: Ctx.SIGNUP_FORM,
        Forms.PASSWORD_RESET: Ctx.PASSWORD_RESET_FORM,
        Forms.PASSWORD_CHANGE: Ctx.PASSWORD_CHANGE_FORM,
        Forms.PROFILE: Ctx.PROFILE_FORM,
        Forms.GITHUB: Ctx.GITHUB_FORM,
        Forms.SETTINGS: Ctx.SETTINGS_FORM,
    }
    return form_lookup.get(form_label, ctx_formkey)


def response_messaages(signal, message, fail=True):
    """

    :param signal:
    :param message:
    :param fail:
    """
    # todo / fixme: 2023-09-21: Messagesd not working
    # messages.add_message(request, signal, message, fail_silently=fail)
    pass
