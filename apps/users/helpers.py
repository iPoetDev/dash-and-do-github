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
- added: Created initial file: 23/09/27:
- added: added functions: 23/09/27:
- Updated:
- updated:
@Plan:
- TODO:
- FIXME:
- CHECK:
    - DONE: PyLint: 2023-09-30
    - DONE: Ruff: 2023-09-28
"""
from django.template.response import TemplateResponse


def redirect_response(request,
                      template_name,
                      context,
                      success_url,
                      redirect_key):
    """Redirect response helper function.

    :param request: The HTTP request object.
    :param template_name: The name of the template to be rendered.
    :param context: The context data to be passed to the template.
    :param success_url: The URL to redirect to upon successful response.
    :param redirect_key: The key for mapping the success_url in the response.

    :return: A TemplateResponse: Specified template, context data,
    and redirect URL.
    :rtype: TemplateResponse
    """
    response = TemplateResponse(request, template_name, context)
    response[redirect_key] = success_url
    return response


def set_remember_me_request(request, remember_me):
    """Helper function to set a remember me cookie.

    :param request: The HttpRequest object
    :param remember_me: Boolean value indicating if Remember Me is checked
    """
    if remember_me:
        # Set a cookie on the response indicating this
        max_age = 14 * 24 * 60 * 60  # two weeks
        request.set_cookie('remember_me', 'true', max_age=max_age)
        request.session.set_expiry(max_age)
    else:
        request.session.set_expiry(0)
        request.delete_cookie('remember_me')  # Session cookie
