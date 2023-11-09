#!/user/bin/env python3
# pylint: skipfile
"""This module contains the general logging functions for
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
    """Log the request object. Progressive logging levels/verbosity/data:

    :param request: The request object.
    :param label: A label for the request. (optional)
    :return: None
    :rtype: None
    """
    # pylint: disable=unused-variable
    # pylint: disable=unused-variable
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
    loggey.info('DnD INFO: View Request: %s',
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
    debug_request(message='DnD DEBUG: View Request: ',
                  obj=request,
                  kind='django',
                  detail=lite_extra)


# noinspection PyUnusedFunction
def log_views_response(response, label=None, desc=None):
    """Log the response object. Progressive logging levels/verbosity/data:

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
                      'content_type': response['Content-Type'],
                      'status': response.status_code}
    options = LoggerOptions(kind='django', on=True, off=False,
                            detail=response_extra)
    # Get the 'django' logger
    logge = logging.getLogger('django')
    # Info: View Response: <TemplateResponse status_code=200,
    # "text/html; charset=utf-8"> (23-09-17)
    logge.info('DnD INFO: View Response: %s',
               response,
               extra=response_extra)
    # Warning: View Response: <TemplateResponse status_code=200,
    # "text/html; charset=utf-8"> (23-09-17)
    logge.warning('DnD WARN: View Response: ',
                  exc_info=True,
                  extra=response_extra)
    # Error: View Response: <TemplateResponse status_code=200,
    # "text/html; charset=utf-8"> (23-09-17)
    logge.error('DnD ERROR: View: Response is: %s',
                response,
                exc_info=True,
                stack_info=True,
                extra=response_extra)
    # Debug: View Response: <TemplateResponse status_code=200,
    # "text/html; charset=utf-8"> (23-09-17)
    debug_response(message='DnD DEBUG: View Response: ',
                   obj=response,
                   logger_options=options)


# noinspection PyUnusedFunction
def send_debug_mail(send_func):
    """:param send_func: A function that sends an email. This function should
     return a boolean value indicating whether the email was sent successfully
     or not.
    :return: The result returned by the `send_func` parameter.

    This method `send_debug_mail` is responsible for sending a debug email
    using the given `send_func`. It wraps the `send_func` with error handling
     and logging functionality.

    The `send_debug_mail` function attempts to send an email by calling the
    `send_func`. If the `send_func` returns a truthy value, which indicates
    that the email was sent successfully, it logs a debug message stating
    "Email sent successfully."
    Otherwise, it logs a debug message stating "Failed to send email."
     The method then returns the result returned by the `send_func`.

    If a `BadHeaderError` exception is raised during the email sending process
    , it logs an exception message stating "Bad headers were detected in the
     email." If any other unexpected exception occurs, it logs an exception
     message stating "An unexpected error occurred in trying to send an email."

    Note: This method requires the `logging` module and the `BadHeaderError`
    exception from the `django.core.mail` module to be imported.
    """
    # noinspection PyBroadException
    try:
        result = send_func()
        if result:
            loggey.debug('Email sent successfully.')
        else:
            loggey.debug('Failed to send email.')
    except BadHeaderError:
        loggey.exception('Bad headers were detected in the email.')
        return None  # Add this line
    except Exception:  # pylint: disable=broad-exception-caught
        loggey.exception(
            'An unexpected error occurred when trying to send an email.')
        return None  # Add this line
    return result


# noinspection DuplicatedCode
def debug_request(message, obj, kind=None, on=True, off=False, detail=None):
    # noinspection DuplicatedCode
    """Log a message with severity 'DEBUG' on the root logger."""
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
class LoggerOptions:
    """Represents the options for configuring a logger.

    :param kind: The kind of logger. Defaults to None.
    :type kind: Any, optional
    :param on: Whether the logger should be turned on. Defaults to True.
    :type on: bool, optional
    :param off: Whether the logger should be turned off. Defaults to
        False.
    :type off: bool, optional
    :param detail: The level of detail for the logger. Defaults to None.
    :type detail: Any, optional
    """

    def __init__(self, kind=None, on=True, off=False, detail=None):
        """Initializes a LoggerOptions object with the given parameters.

        :param kind: The kind of logger options.
        :param on: A boolean specifying if the logger is turned on.
        :param off: A boolean specifying if the logger is turned off.
        :param detail: Additional details for the logger options.
        """
        self.kind = kind
        self.on = on
        self.off = off
        self.detail = detail


def debug_response(message, obj, logger_options=None):
    """Log a message with severity 'DEBUG' on the root logger.

    Usage:
    e.g. debug
    options = LoggerOptions(kind="some kind", on=True,
                            off=False, detail=detail_dict)
    debug_response("message", obj, options)
    """
    if logger_options is None:
        logger_options = LoggerOptions()

    logger = logging.getLogger(logger_options.kind) \
        if logger_options.kind is not None \
        else logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s '
        '- %(message)s - %(response)s - '
        '%(label)s - %(context)s - %(content_type)s - %(status)s - '
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.debug(f'{message} %s',
                 obj,
                 exc_info=logger_options.on,
                 stack_info=logger_options.off,
                 extra=logger_options.detail)


class IgnoreFilter(logging.Filter):
    """
    The IgnoreFilter class is a logging filter that can be used to ignore
     log messages that contain a specific string.

    :args:
        ignore_string (str): The string to ignore in log messages.

    """
    def __init__(self, ignore_string):
        """
        Constructor method for IgnoreFilter class.

        :param ignore_string: The string to ignore in log messages.
        :type ignore_string: str

        """
        super().__init__()
        self.ignore_string = ignore_string

    def filter(self, record):
        """
        :param record: The log record to be filtered.
        :type record: logging.LogRecord
        :return: True if the log record should be included,
                False if it should be ignored.
        :rtype: bool
        """
        return self.ignore_string not in record.getMessage()


class MiddlewareFilter(logging.Filter):
    """
    The IgnoreFilter class is a logging filter that can be used to ignore
     log messages that contain a specific string.

    :args:
        ignore_string (str): The string to ignore in log messages.

    """

    def __init__(self, exclude_string):
        """
        Constructor method for MiddlewareFilter class.

        :param ignore_string: The string to ignore in log messages.
        :type ignore_string: str

        """
        super().__init__()
        self.exclude_string = exclude_string

    def filter(self, record):
        """
        :param record: The log record to be filtered.
        :type record: logging.LogRecord
        :return: True if the log record should be included,
                False if it should be ignored.
        :rtype: bool
        """
        return self.exclude_string not in record.getMessage()
