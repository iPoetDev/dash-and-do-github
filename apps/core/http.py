#!/user/bin/env python3
"""
This module contains the views for the core app.

    @File: http.py
    @Version: 0.3.0 to 0.3.0.?
    @Desc: apps | core | http
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/09/13
    @Date Modified: 23/09/13
    @Python Version: 3.11.04
    @Django Version: 4.2.3
    @Notes / Ideas v Implement:
    @Changelog:
    - added:
        - 2023-09-13:
          - Initialised file
          - Refactored form_contacts.
          - handle_post_request
    - noted: HTTP. Helper functions for handling HTTP requests/responses.
"""

#  Copyright (c) 2023.
from django.template.response import TemplateResponse
from django.contrib import messages
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseServerError, HttpResponseNotAllowed)
from .email.values import HTTP
from .forms import ContactForm


class Template:
    """
    Template Paths
    """
    HOME = 'index.html'
    CONTACT = '/all/form_contact.html'
    #CONTACT_SUCCESS = '/all/contact_success.html'


class Ctx:
    """
    Context Variables
    """
    FORM = 'contact'


class Feedback:
    """
    Feedback Messages
    """
    EMAILSUCCESS = 'Your message has been sent.'
    BADREQUEST = 'Bad request, please verify your message and try again.'
    SERVERERROR = 'Server error, your message could not be sent.'
    EMAILERROR = 'An error occurred, your message could not be sent.'


class HttpMessage:
    """
    HTTP Messages
    """
    INVALID_HEADER = 'Invalid header found.'
    BAD_REQUEST = 'Bad Request.'
    SERVER_ERROR = 'Internal Server Error.'
    MSG_SENT = 'Message Sent'
    MSG_FAILED = 'Message Failed'


class Signal:
    """
    Message Levels
    """
    INFO = 'info'
    SUCCESS = 'success'
    ERROR = 'error'
    FAIL = False


def contact_http_response(request, form, response, htmx_request) \
    -> (TemplateResponse or None):
    """
    Handles the response in response JS/HTMX is enabled/disabled.
    Progerssive Enhancement failed back.
    :param request: The HTTP request object.
    :param form: A form, saved to to the Database
    :param response: The response from the email service.
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
        form.save()
        if htmx_request:
            # HTMX Request & Response, JavaScript Enabled
            return contact_htmx_responses(request,
                                          htmx_request,
                                          form,
                                          response)
        else:
            # Progressive Enahancement, JavaScript Disabled
            return contact_responses(request,
                                     form,
                                     response)


def contact_email(form, send_mail_func) \
    -> (HttpResponse or None):
    """
    Post Email Handler
    :param form:
    :param send_mail_func:
    :return: HttpResponse or None
    :rtype: HttpResponse or None
    """
    # Pass the contact form data for the email.
    email_response = send_mail_func(form)

    # for successful email
    if email_response == HTTP.MSG_SENT:
        return HttpResponse(HttpMessage.MSG_SENT, status=200)

    # for failed email
    elif email_response == HTTP.MSG_FAILED:
        return HttpResponseServerError(HttpMessage.SERVER_ERROR, status=500)

    # for invalid header in email, signal a bad request
    elif email_response == HTTP.INVALID_HEADER:
        return HttpResponseBadRequest(HttpMessage.BAD_REQUEST, status=400)

    return None


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
    if all([isinstance(response, HttpResponse), htmx_request,
            response.status_code == 200]):
        # Successful Email: 200 Ok, Fresh unbounded form.
        contact = ContactForm()  # Empty the form for the next input
        return template_response(request,
                                 contact,
                                 Template.CONTACT,
                                 Signal.SUCCESS,
                                 Feedback.EMAILSUCCESS,
                                 response.status_code,
                                 fail=Signal.FAIL)
    elif all([isinstance(response, HttpResponseBadRequest), htmx_request]):
        # Bad Request: 400, Return unbounded form with errors
        # Clear the form, allow user to retry the request afresh
        contact = ContactForm()  # Clear the form, as there was illegal input
        return template_response(request,
                                 contact,
                                 Template.CONTACT,
                                 Signal.ERROR,
                                 Feedback.BADREQUEST,
                                 HttpResponseBadRequest.status_code,
                                 fail=Signal.FAIL)
    elif all([isinstance(response, HttpResponseServerError), htmx_request]):
        # Server Error: 500, Return unbounded form with errors
        # Allow user to retry the request with form data.
        return template_response(request,
                                 contact,
                                 Template.CONTACT,
                                 Signal.ERROR,
                                 Feedback.SERVERERROR,
                                 HttpResponseServerError.status_code,
                                 fail=Signal.FAIL)
    elif all([response is None, htmx_request]):
        # Email Error: 405 Method Not Allowed
        # Allow user to retry the request with form data.
        return template_response(request,
                                 contact,
                                 Template.CONTACT,
                                 Signal.ERROR,
                                 Feedback.EMAILERROR,
                                 HttpResponseNotAllowed.status_code,
                                 fail=Signal.FAIL)

    return None


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
    if isinstance(response, HttpResponse) and response.status_code == 200:
        # Successful Email: 200 Ok, Fresh unbounded form.
        contact = ContactForm()  # Empty the form for the next input
        return template_response(request, contact,
                                 Template.CONTACT,
                                 Signal.SUCCESS,
                                 Feedback.EMAILSUCCESS,
                                 response.status_code,
                                 fail=Signal.FAIL)
    elif isinstance(response, HttpResponseBadRequest):
        # Bad Request: 400, Return unbounded form with errors
        # Clear the form, allow user to retry the request afresh
        contact = ContactForm()  # Clear the form, as there was illegal input
        return template_response(request,
                                 contact,
                                 Template.CONTACT,
                                 Signal.ERROR,
                                 Feedback.BADREQUEST,
                                 HttpResponseBadRequest.status_code,
                                 fail=Signal.FAIL)
    elif isinstance(response, HttpResponseServerError):
        # Server Error: 500, Return unbounded form with errors
        # Allow user to retry the request with form data.
        return template_response(request,
                                 contact,
                                 Template.CONTACT,
                                 Signal.ERROR,
                                 Feedback.SERVERERROR,
                                 HttpResponseServerError.status_code,
                                 fail=Signal.FAIL)
    elif response is None:
        # Email Error: 405 Method Not Allowed
        # Allow user to retry the request with form data.
        return template_response(request,
                                 contact,
                                 Template.CONTACT,
                                 Signal.ERROR,
                                 Feedback.EMAILERROR,
                                 HttpResponseNotAllowed.status_code,
                                 fail=Signal.FAIL)

    return None


def template_response(request,
                      form,
                      template,
                      signal,
                      message,
                      status=None,
                      fail=False):
    """

    Creates and returns a TemplateResponse and form associated with a
    HTTP Request, along with a Django signal message and Feedback message,
    per HTTP Response Status Code.

    :param request: HTTP Request
    :param form: Form (Bounded or Unbounded)
    :param template: Template Path
    :param signal: Message Level
    :param message: Custom HTTP Response Message
    :param status: HTTP Response Status Code, Optional
    :param fail: Boolean, Optional, Default: False
    :return: Shared TemplateResponse
    :rtype: TemplateResponse
    """
    messages.add_message(request, signal, message, fail_silently=fail)
    context = {Ctx.FORM: form}
    return TemplateResponse(request, template, context, status)
