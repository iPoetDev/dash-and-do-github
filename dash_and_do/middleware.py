#!/user/bin/env python3
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
- added: Created initial file: 23/09/??:
- Updated:
- updated:
@Plan:
- TODO:
- FIXME:
- CHECK:
"""
import logging

from dash_and_do.utils import get_date

# from datetime import datetime
from dash_and_do.utils import get_error_detail

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    """
    Initialize the RequestLoggingMiddleware class.


    """
    def __init__(self, get_response):
        """
        Initialize the RequestLoggingMiddleware class.

        :param get_response: A callable to get the response for the request.
        :type get_response: callable
        """
        self.get_response = get_response
        self.requestlogger = logging.getLogger('django.request')

    def __call__(self, request):
        """ Logs and Captures all the request parameters

       Do note, sensitive data such as user's IP address, authorization headers
        etc are contained in the headers as well as meta. Ensure that your
        production logging does not cause privacy violations or data exposure.

        1) Deployment: Remove prior to deployment or only show if
         a) the DEBUG is true and
         b) the internal IPS is local 127.

        Hooks django.request loggers
        And handles the
        1) request headers
        2) request meta
        3) request GET
        4) request POST

        :param request: The incoming request object.
        :type request: django.http.HttpRequest
        :return: The HTTP response object.
        :rtype: django.http.HttpResponse
        """
        # Headers
        self.requestlogger.debug('Request Headers:'
                                 f' {self.request_headers(request)}')
        # Meta
        # self.requestlogger.debug('Request Meta:  '
        #                          f'{self.request_meta(request)}')
        self.requestlogger.debug(f'=========================================')
        # Get
        self.requestlogger.debug(f'Request GET: {self.request_get(request) if
                                    not None else 'No GET Data'}')
        self.requestlogger.debug(f'=========================================')
        # Post
        self.requestlogger.debug(f'Request POST: {self.request_post(request) if
                                             not None else 'No POST Data'}')
        self.requestlogger.debug(f'=========================================')
        self.requestlogger.debug(f'Request Details"'
                                 f'{self.request_details(request)}')
        response = self.get_response(request)
        return response

    def request_headers(self, request):
        sorted_headers = dict(
            sorted(request.headers.items(), key=lambda x: x[0].lower()))
        return sorted_headers

    # noinspection PyMethodMayBeStatic
    def request_meta(self, request):
        sorted_meta = dict(
            sorted(request.META.items(), key=lambda x: x[0].lower()))
        return sorted_meta

    # noinspection PyMethodMayBeStatic
    def request_post(self, request):
        if request.method == 'POST':
            sorted_data = dict(sorted(request.POST.items(),
                                      key=lambda x: x[0].lower()))
            return sorted_data
        else:
            return None

    # noinspection PyMethodMayBeStatic
    def request_get(self, request):
        if request.method == 'GET':
            sorted_data = dict(sorted(request.GET.items(),
                                      key=lambda x: x[0].lower()))
            return sorted_data
        else:
            return None

    def request_details(self, request):
        """"""
        data = ''
        if request.method == 'GET':
            data = f'GET: HOST: {request.get_host()}\n'
            data = f'GET: PATH INFO: {request.get_full_path_info()}\n'

        if request.method == 'POST':
            data = f'POST: HOST: {request.get_host()}\n'
            data = f'POST: PATH INFO: {request.get_full_path_info()}\n'

        return data


class DashLoggingMiddleware:
    """Middleware class to log requests and responses in a Django
    application.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the request
        request_headers = self.safe_headers(request.META)
        request_string = (f"Request: {request.method} "
                          f"{request.get_full_path()}, "
                          f"Headers: {request_headers}")
        logger.debug(request_string)

        # Handle response and any potential exceptions
        response_string, response = self.handle_response(request)

        # Log the response
        self.log_response(response, response_string)

        return response

    def handle_response(self, request):
        response = None
        response_string = "\nAn error occurred while handling the response.\n"
        try:
            response = self.get_response(request)
            response_string = self.build_response_string(request, response)
        except Exception as e:
            err_message = f"\nException occurred: {str(e)}\n"
            logger.error(err_message, exc_info=True)
        return response_string, response

    def log_response(self, response, response_detail):
        if 200 <= response.status_code < 300:
            response_string = (
                '\n'
                f'================= 200 OK ================\n'
                f"200+: Successful Response:"
                f" {response.status_code}\n"
                f" {response_detail}\n"
                f'========================================\n'
                '\n'
            )
            logger.info(response_string)
        elif 300 <= response.status_code < 400:
            response_string = (
                '\n'
                f'================= 300 REDIRECT =========\n'
                f"300+: Redirect Response:"
                f" {response.status_code}\n"
                f" {response_detail}\n"
                f'========================================\n'
                '\n'
            )
            logger.debug(response_string)
        elif 400 <= response.status_code < 600:
            level = logging.ERROR if response.status_code >= 500 \
                else logging.WARNING
            # Assume that error detail is packed into response content.
            # Escape HTML and Newlines from response content.
            error_detail = get_error_detail(response)
            response_string = (
                '\n'
                f'================ 400 | 500 ERROR ========\n'
                f"400 | 500: Error Response: "
                f" {response.status_code}\n"
                f" {response_detail}\n"
                f"Detail: {error_detail}\n\n"
                f'========================================\n'
                '\n'
            )
            logger.log(level, response_string)

    def safe_headers(self, headers, sensitive=True, allheaders=False):
        # Prepare a copy of headers excluding any that may have sensitive data
        safe_headers = headers.copy()

        if sensitive:
            sensitive_headers = ["HTTP_COOKIE", "HTTP_AUTHORIZATION"]
            for header in sensitive_headers:
                safe_headers.pop(header, None)  # Remove sensitive headers

        if allheaders:
            return safe_headers

        attributes = {
            'ip_address':'REMOTE_ADDR',
            'protocol':'SERVER_PROTOCOL',
            'host':'HTTP_HOST',
            'query_string':'QUERY_STRING',
            'remote_user':'REMOTE_USER',
            'request_method':'REQUEST_METHOD',
            'path_info':'PATH_INFO'
        }

        filtered_headers = {attr:safe_headers.get(header, '') for attr, header
            in
            attributes.items()}

        return filtered_headers

    def build_response_string(self, request, response):
        try:
            datetime_stamp = get_date()
            safe_headers = self.safe_headers(request.META)

            attr_values = {
                'datetime_stamp':datetime_stamp,
                'response_status':response.status_code if response else "No "
                                                                        "response",
                **safe_headers
            }
            # This will prevent a KeyError in case an attribute is
            # not exist in attr_values, it simply returns None as output
            attr_values = {k:(v if v is not None else 'No value') for k, v in
                attr_values.items()}
            #

            response_code =  {attr_values.get('response_status')}
            response_string = (
                f'\n'
                f'================== {response_code} ================'
                f'\n'
                f"{attr_values.get('datetime_stamp')} "
                f"{attr_values.get('ip_address')} "
                f"{attr_values.get('protocol')} \n"
                f"Host: {attr_values.get('host')} "
                f"QueryString: {attr_values.get('query_string')}\n"
                f"RemoteUser: {attr_values.get('remote_user')} \n"
                f"RequestMethod: {attr_values.get('request_method')} "
                f"Path: {attr_values.get('path_info')} "
                f"ResponseStatus: {attr_values.get('response_status')}"
                f'\n'
                f'=====================================\n'
                f'\n'
            )
            return response_string

        except Exception as e:
            err_message = (f"Exception occurred in build_response_string "
                           f"method: {str(e)}")
            logger.error(err_message, exc_info=True)
            return "An error occurred while building the response string."


class SessionCSRFLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """:param request: The incoming request object.
        :type request: HttpRequest
        :return: The response generated by the downstream middleware.
        :rtype: HttpResponse

        This method is the entry point for the SessionCSRFLoggingMiddleware.
        It is invoked when a request is made to the server.
        It logs
        - the session data,
        - the CSRF cookie and token, and
        then passes the request to the next middleware in the stack.
        The response generated by the downstream middleware is then returned.

        Example usage:

        middleware = SessionCSRFLoggingMiddleware()
        response = middleware(request)
        """
        session_data = request.session
        print(session_data)  # or use logging methods
        # csrf_cookie = request.META.get('CSRF_COOKIE', '')
        # if csrf_cookie:
        #     print('CSRF_COOKIE: ' + csrf_cookie)

        csrf_token = request.META.get('X-Csrftoken', '')
        if csrf_token:
            print(csrf_token)  # or use logging methods

        response = self.get_response(request)

        return response
