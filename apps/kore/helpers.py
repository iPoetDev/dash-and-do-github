#!/user/bin/env python3
"""@File: helpers.py
@Version: 0.3.0 to 0.3.1: form Form Helpers
@Desc: apps | kore |  forms | helpers: Form Helper Functions
@Author: Charles Fowler
@Copyright: 2023
@Date Created: 23/09/12
@Date Modified: 23/09/13
@Python Version: 3.11.04
@Django Version: 4.2.3
@Notes / Ideas v Implement:
-
@Changelog:
- Added:
- 23/09/19: Added docstrings
- 23/09/19: Created initial file
- Updated:
- Deprecated:
@Plan:
"""
#  Copyright (c) 2023.

import inspect

from rich import pretty
from rich.pretty import pprint as pp

pretty.install()


def debuginfo():
    """Debug Info :return:

    :rtype str
    """
    frame = inspect.currentframe().f_back
    filename = frame.f_code.co_filename
    lineno = frame.f_lineno
    return f'{filename}:{lineno}'


def pp_form(form, label=None):
    """Pretty print form & values.

    :param form:
    :param label: Name of Holder Function
    :return:
    """
    if form.is_valid():
        pp(f'{label} {form}')
        for field_name, value in form.cleaned_data.items():
            print(f'{field_name}: {value}')

    if not form.is_valid():
        pp(f'{label} {form}')
        for field_name, errors in form.errors.items():
            pp(f'{field_name}: {errors}')
        for field_name, value in form.cleaned_data.items():
            print(f'{field_name}: {value}')


def pp_email(data: dict, label: str = None):
    """Pretty print response.

    :param data:
    :param label: Name of Holder Function
    :return:
    """
    pp('======PP Email Form Values======')
    pp(f'{label} : {data}')
    for key, value in data.items():
        pp(f'{key}: {value}')
    debuginfo()


def pp_message(subject,  # pylint: disable=too-many-arguments,R0913
               recipients,
               sender,
               message,
               copy=None,
               smtp=None,
               authuser=None,
               fail=None,
               label=None):
    """Pretty print response.

    :param subject:
    :param sender:
    :param recipients:
    :param message:
    :param copy:
    :param smtp:
    :param authuser:
    :param fail: :label: Name of Holder Function
    :param label: Name of Holder Function
    :return:
    """
    pp('======PP Email Message Values======')
    pp(f'{label} : {subject} : {sender} : {recipients}, {copy} : {message}')
    pp(f'{label} : {smtp} : {authuser} : {fail}')
    debuginfo()


def pp_response(response, label=None):
    """Pretty print response.

    :param response:
    :param label: Name of Holder Function
    :return:
    """
    label = '1: View: contact_email response'
    pp('======PP Response Values======')
    pp(f'{label} : {response}')


def pp_function(function, label=None):
    """Pretty print function.

    :param function:
    :param label: Name of Holder Function
    :return:
    """
    pp('======PP Function======')
    pp(f'{label} %s{function}')
    debuginfo()


def pp_file(label=None):
    """Pretty print location.

    :param label: Name of Holder Function
    :return:
    """
    pp('======PP File Values======')
    pp(f'{label} %s{__file__}')


def pp_locate(obj=None, label=None):
    """Pretty print location.

    :param obj: object to print
    :param label: Name of Function or Statement
    :return: None
    """
    pp('======PP Locate Values======')
    if label:
        print(
            f'{label} is at line {inspect.currentframe().f_back.f_lineno}'
            f' in function {inspect.currentframe().f_back.f_code.co_name}')

    if obj:
        print(
            f'{obj} is at line {inspect.currentframe().f_back.f_lineno}'
            f' in function {inspect.currentframe().f_back.f_code.co_name}')


def pp_console(obj: object, label=None):  # noqa: A
    """Pretty print object.

    :param obj: object to print
    :param label: Name of Holder Function
    :return: None
    """
    print('=======')
    pp_function(obj, label)
    pp_locate(obj, label)
    pp_file(label)
    print('=======')


# noinspection PyUnusedFunction
def pp_consoleform(form, label=None):
    """Pretty print object.

    :param form: object to print
    :param label: Name of Holder Function
    :return: None
    """
    print('=======')
    pp_form(form, label)
    pp_locate(label)
    pp_file(label)
    print('=======')


def pp_label(label):
    """Pretty print object.

    :param label: Name of Holder Function
    :return: None
    """
    print('=======')
    pp_locate(label)
    # pp_file(label)
    print('=======')
