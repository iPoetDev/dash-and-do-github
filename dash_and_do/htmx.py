#!/user/bin/env python3
"""
    @File: htmx.py
    @Version: 0.3.0 to 0.3.0.?
    @Desc: common | dahs_and_do |  htmx. helpers functions
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/08/07
    @Date Modified: 23/09/12
    @Python Version: 3.11.04
    @Django Version: 4.2.3
    @Notes / Ideas v Implement:
        - Helper Functions for HTMX
        - Standalone helpers for HTMX
        - Model to add middleware implementations for HTMX
    @Changelog:
    - Added:
        - 23/09/12: Added docstrings
        - 23/09/12: Created initial file
        - 23/09/12: added Common Email Functionalities
    - Updated:
    - Deprecated:
        - 23/09/12: Deprecated
    - Removed:
        - 23/09/12: Removed
    @Plan:
        - TODO:
            - Create test cases for models.
              - Define Test Scenarios
                - Happy Path
                - Edge Cases
                - Other
"""

def is_htmx(request):
    """
    Checks if the given request is an HTMX request by looking for the 'Htmx-Request' header.

    :param: request (HttpRequest): The HTTP request object.
    :returns: str: The value of the 'Htmx-Request' header if present, else None.
"""
    return request.headers.get('Htmx-Request')

def add_htmx_header(headers, key, value):
    """
    Adds an HTMX header to an existing dictionary of headers.
    :usage: HTTP Request Headers, HTTP Responses

    :param: headers (dict): The dictionary of headers to add to.
    :param: key (str): The key of the header to add.
    :param: value (str): The value of the header to add.

    :returns: dic: The dictionary of headers with the new header added.
    """
    headers[key] = value
    return headers

def parse_htmx_response(response):
    """
    Parses an HTMX response into a dictionary.
    :param response:
    :return: dic: The dictionary of response data
    """
    data = {'status_code': response.status_code,
            'headers': response.headers,
            'content': response.content}
    return data

def set_htmx_status(response, status_code):
    """
    Sets the status code of an HTMX response.
    :param response: HTTP Response
    :param status_code:
    :return: HTTP Response with updated status code
    """
    response.status_code = status_code
    return response

def set_htmx_content(response, content):
    """
    Sets the content of an HTMX response.
    :param response:
    :param content:
    :return:
    """
    response.content = content
    return response
