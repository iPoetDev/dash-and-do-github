#!/user/bin/env python3
"""
    @File: <filename>.py
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
# from datetime import datetime
from dash_and_do.utils import get_error_detail
from dash_and_do.utils import get_date

logger = logging.getLogger(__name__)


class DashLoggingMiddleware:
    """Middleware class to log requests and responses in a Django
    application."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the request
        request_headers = self.safe_headers(request.META)
        request_string = (f'Request: {request.method} '
                          f'{request.get_full_path()}, '
                          f'Headers: {request_headers}')
        logger.debug(request_string)

        # Handle response and any potential exceptions
        response_string, response = self.handle_response(request)

        # Log the response
        self.log_response(response, response_string)

        return response

    def handle_response(self, request):
        response = None
        response_string = '\nAn error occurred while handling the response.\n'
        try:
            response = self.get_response(request)
            response_string = self.build_response_string(request, response)
        except Exception as e:
            err_message = f'\nException occurred: {str(e)}\n'
            logger.error(err_message, exc_info=True)
        return response_string, response

    def log_response(self, response, response_detail):
        if 200 <= response.status_code < 300:
            response_string = (
                '\n'
                f'================= 200 OK ================\n'
                '200+: Successful Response:'
                f' {response.status_code}\n'
                f' {response_detail}\n'
                f'========================================\n'
                '\n'
            )
            logger.info(response_string)
        elif 300 <= response.status_code < 400:
            response_string = (
                '\n'
                f'================= 300 REDIRECT =========\n'
                '300+: Redirect Response:'
                f' {response.status_code}\n'
                f' {response_detail}\n'
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
                f'400 | 500: Error Response: '
                f' {response.status_code}\n'
                f' {response_detail}\n'
                f'Detail: {error_detail}\n\n'
                f'========================================\n'
                '\n'
            )
            logger.log(level, response_string)

    def safe_headers(self, headers, sensitive=True, allheaders=False):
        # Prepare a copy of headers excluding any that may have sensitive data
        safe_headers = headers.copy()

        if sensitive:
            sensitive_headers = ['HTTP_COOKIE', 'HTTP_AUTHORIZATION']
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

        return {
            attr: safe_headers.get(header, '')
            for attr, header in attributes.items()
        }

    def build_response_string(self, request, response):
        try:
            datetime_stamp = get_date()
            safe_headers = self.safe_headers(request.META)

            attr_values = {
                'datetime_stamp':datetime_stamp,
                'response_status':response.status_code if response else 'No '
                                                                        'response',
                **safe_headers
            }
            # This will prevent a KeyError in case an attribute is
            # not exist in attr_values, it simply returns None as output
            attr_values = {k:(v if v is not None else 'No value') for k, v in
                attr_values.items()}
            #

            response_code =  {attr_values.get('response_status')}
            return f"\n================== {response_code} ================\n{attr_values.get('datetime_stamp')} {attr_values.get('ip_address')} {attr_values.get('protocol')} \nHost: {attr_values.get('host')} QueryString: {attr_values.get('query_string')}\nRemoteUser: {attr_values.get('remote_user')} \nRequestMethod: {attr_values.get('request_method')} Path: {attr_values.get('path_info')} ResponseStatus: {attr_values.get('response_status')}\n=====================================\n\n"
        except Exception as e:
            err_message = (f'Exception occurred in build_response_string '
                           f'method: {str(e)}')
            logger.error(err_message, exc_info=True)
            return 'An error occurred while building the response string.'
