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


class DebugAdapter:
    """@Class: DebugAdapter
    @Desc: <desc>
    @Notes / Ideas v Implement:
    - .
    @Changelog:
    - Added:
    """

    def __init__(self):
        """@Method: __init__"""
        pass

    @staticmethod
    def print_post(request):
        """Print post data.

        :param request:
        """
        print('===========================')
        print(f'SignupView: post: {request}')
        print(f'request.POST: {request.POST}')
        for key, value in request.POST.items():
            print(f'Key: {key}, Value: {value}')
        print('===========================')

    @staticmethod
    def print_get(request):
        """Print get data.

        :param request:
        """
        print(f'SignupView: get: {request}')
        print(f'request.GET: {request.GET}')
        for key, value in request.GET.items():
            print(f'Key: {key}, Value: {value}')

    @staticmethod
    def print_formerrors_signup(request,
                                form,
                                is_json=False,
                                escape=False):
        """:param request: The HTTP request object.
        :param form: The form object to check for errors.
        :param is_json: Optional boolean value indicating whether
            to print the errors as JSON or not. Default is False.
        :param escape: Optional boolean value indicating whether
            to escape HTML characters in the output. Default is False.
        :return: None

        Example usage:

        request = HttpRequest()
        form = SignupForm()
        DebugAdapter.print_formerrors_signup(request, form)
        """
        # Check for Form errors
        print(f'SignupView: form.errors: \n'
              f'{form.errors}')
        print(f'SignupView: form.non_field_errors: \n'
              f'{form.non_field_errors}', )
        print(f'SignupView: form\'s request: {request}')
        print('SignupView: Per form fields')
        # Check for Email errors
        # if form.has_error('email'):
        #     print(f'SignupView: form.errors.email: '
        #           f'{form.errors.email}')
        # Check for Password errors
        if form.has_error('password`1'):
            print(f'SignupView: form.errors.username: '
                  f'{form.errors.password1}')
        # Check for Password2 errors
        if form.has_error('password`2'):
            print(f'SignupView: form.errors.password: '
                  f'{form.errors.password2}')
        # Switch between json and data
        if is_json:
            print(f'SignupView: form.errors.as_json: \n'
                  f'{form.errors.as_json(escape_html=escape)}')
        else:
            print(f'SignupView: form.errors.as_data: \n'
                  f'{form.errors.as_data()}')


    @staticmethod
    def print_post_data(classname, data, func='__init__'):
        """:param classname: Name of the class where the method is called from.
        :param data: The data passed as a dictionary.
        :param func: Name of the method being called. Default: '__init__'.

        :return: None

        """
        if data is not None:
            print(f'{classname}: {func}(): data keys: {data.keys()}')
            for value in data.values():
                print(f'{classname}: {func}(): data Value: {value}')
        print(f'{classname}: {func}(): data: {data}')

    @staticmethod
    def print_cleandata(classname, cleandata, func='clean'):
        """:param classname: Name of the class where the method is called from.
        :param data: The data passed as a dictionary.
        :param func: Name of the method being called. Default: '__init__'.
        :return: None
        """
        print(f'{classname}: {func}(): Form data: {cleandata}')  # fixed bug
