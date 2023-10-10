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
import traceback

# Local: Project Imports
from dash_and_do.htmx import is_htmx
from dash_and_do.settings import DEBUG

# Django HTTP Imports
from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse

# Django Imports
from django.shortcuts import render
from django.template.response import TemplateResponse

from django.template import Context, Template
import io
from django.test import RequestFactory


def debug_includes_console(request, template, ctx):
    html_code = str(render(request, template, ctx).content, 'utf-8')
    divided_html = html_code.split(
        '{% include ')  # separate included html templates

    for html in divided_html[ 1: ]:  # exclude part before first include
        include_name = html.split('%}')[ 0 ].strip(
            '"\'')  # get name of included html file
        tpl = Template("{% include '" + include_name + "' %}")
        rendered = tpl.render(Context(ctx))
        print(f"#### START INCLUDE: {include_name} ####")
        print(rendered)
        print(f"#### END INCLUDE: {include_name}" + " ####\n")


def debug_includes_files(request, template, ctx):
    html_code = str(render(request, template, ctx).content, 'utf-8')
    divided_html = html_code.split(
        '{% include ')  # separate included html templates

    with open('debug_output.txt', 'w', encoding='utf-8') as debug_file:
        for html in divided_html[ 1: ]:  # exclude part before first include
            include_name = html.split('%}')[ 0 ].strip(
                '"\'')  # get name of included html file
            tpl = Template("{% include '" + include_name + "' %}")
            rendered = tpl.render(Context(ctx))
            debug_file.write(f"#### START INCLUDE: {include_name}" + " ####\n")
            debug_file.write(rendered + "\n")
            debug_file.write(f"#### END INCLUDE: {include_name}" + " ####\n\n")
