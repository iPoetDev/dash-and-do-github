#!/user/bin/env python3
"""
    This module contains the general logging functions for
    - all views, forms, users, emails(?)  | logging.

    @File: views.py
    @Version: 0.3.5 to 0.3.0.?
    @Desc: dash_and_do | logger: General logging for the project.
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/08/17
    @Date Modified: 23/09/17
    @Python Version: 3.11.04
    @Django Version: 4.2.3
    @Notes / Ideas v Implement:
        - Log the request object (form submission.
        - Log the response object (form response).
        - TODO: Log the form object (form data)
        - TODO: Log the user object.
        - TODO: Log the emailing object (emailing data)
    @Changelog:
    - noted: Use defacto logging for the project.
    - noted: See settings.py | LOGGING for more info.
    - added: log_views_request (23-09-17)
    - added: log_views_response (23-09-17)
"""
import logging

from django.core.mail import BadHeaderError

loggey = logging.getLogger(__name__)


# noinspection PyUnusedFunction,PyUnusedLocal
def log_views_request(request, label=None):
    """

    Log the request object.
    Progressive logging levels/verbosity/data:

    :param request: The request object.
    :param label: A label for the request. (optional)
    :return: None
    :rtype: None
    """
    full_extra = {'request': request,
                  'label': label,
                  'user': request.user,
                  'content_type': request.content_type,
                  'method': request.method,
                  'path': request.path,
                  'path_info': request.path_info,
                  'encoding': request.encoding,
                  'scheme': request.scheme,
                  'content_params': request.content_params,
                  'resolver_match': request.resolver_match,
                  }
    lite_extra = {'request': request,
                  'label': label,
                  'user': request.user,
                  'method': request.method,
                  'path': request.path,
                  }
    # Info: View INFO: <WSGIRequest: POST '/'> (23-09-17)
    # loggey.info("DnD INFO: View Request: %s",
    #             request,
    #                     extra={'request': request, 'label': label})
    loggey.info("DnD INFO: View Request: %s",
                request,
                exc_info=True,
                stack_info=False,
                extra=lite_extra, )
    # Warning: View WARNING: <WSGIRequest: POST '/'> (23-09-17)
    # loggey.warning("DnD WARN: View Request:",
    #                exc_info=True, extra={'request': request, 'label': label})
    # Error: View ERROR: <WSGIRequest: POST '/'> (23-09-17)
    # loggey.error("DnD ERROR: View Request:",
    #              exc_info=True,
    #              stack_info=True,
    #              extra=lite_extra)),
    debug_request(message="DnD DEBUG: View Request: ",
                  obj=request,
                  kind='django',
                  detail=lite_extra)


# noinspection PyUnusedFunction
def log_views_response(response, label=None, desc=None):
    """

    Log the response object.
    Progressive logging levels/verbosity/data:

    :param response:
    :param label: A label for the response. (optional)
    :param desc: Description of the response scenario. (optional)
    :return: None
    :rtype: None
    """
    # Logging Key: Params
    response_extra = {'response': response,
                      'label': label,
                      'description': desc,
                      'context': response.context_data,
                      'content_type': response[ 'Content-Type' ],
                      'status': response.status_code}

    # Get the 'django' logger
    logge = logging.getLogger('django')
    # Info: View Response: <TemplateResponse status_code=200, "text/html; charset=utf-8"> (23-09-17)
    logge.info("DnD INFO: View Response: %s",
               response,
               extra=response_extra)
    # Warning: View Response: <TemplateResponse status_code=200, "text/html; charset=utf-8"> (23-09-17)
    logge.warning("DnD WARN: View Response: ",
                  exc_info=True,
                  extra=response_extra)
    # Error: View Response: <TemplateResponse status_code=200, "text/html; charset=utf-8"> (23-09-17)
    logge.error("DnD ERROR: View: Response is: %s",
                response,
                exc_info=True,
                stack_info=True,
                extra=response_extra),
    # Debug: View Response: <TemplateResponse status_code=200, "text/html; charset=utf-8"> (23-09-17)
    debug_response(message="DnD DEBUG: View Response: ",
                   obj=response,
                   kind='django',
                   detail=response_extra)


# noinspection PyUnusedFunction
def send_debug_mail(send_func):
    # noinspection PyBroadException
    try:
        result = send_func()
        if result:
            loggey.debug("Email sent successfully.")
        else:
            loggey.debug("Failed to send email.")
        return result
    except BadHeaderError:
        loggey.exception("Bad headers were detected in the email.")
    except Exception:
        loggey.exception(
            "An unexpected error occurred when trying to send an email.")


# noinspection DuplicatedCode
def debug_request(message, obj, kind=None, on=True, off=False, detail=None):
    # noinspection DuplicatedCode
    """
        Log a message with severity 'DEBUG' on the root logger.
        """

    logger = logging.getLogger(kind) if type is not None \
        else logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(request)s - '
        '%(label)s - %(user)s - %(content_type)s - %(method)s - %(path)s - '
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.debug(f'{message} %s',
                 obj,
                 exc_info=off,
                 stack_info=on,
                 extra=detail)


# noinspection DuplicatedCode
def debug_response(message, obj, kind=None, on=True, off=False, detail= \
    None):
    # noinspection DuplicatedCode
    """
        Log a message with severity 'DEBUG' on the root logger.
        """
    logger = logging.getLogger(kind) if type is not None \
        else logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(response)s - '
        '%(label)s - %(context)s - %(content_type)s - %(status)s - '
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.debug(f'{message} %s',
                 obj,
                 exc_info=on,
                 stack_info=off,
                 extra=detail)
