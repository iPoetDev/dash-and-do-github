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
# OS Imports

# Local: Project Imports

# Django HTTP Imports

# Django Imports
from django.shortcuts import render
from django.template import Context
from django.template import Template


def debug_includes_console(request, template, ctx):
    """Debugs the includes in a Django template.

    This method renders the template with the given context and then prints
    out the content of each included template.
    The name of each included templateis also printed to provide a clear
    indication of the start and end of each include block.

    :param request: The HTTP request object.
    :param template: The template to render.
    :param ctx: The context to be passed to the template rendering engine.
    :return: None
    :rtype: None

    Example:
    ```python
    debug_includes_console(request, 'template.html', {})
    ```
    """
    html_code = str(render(request, template, ctx).content, 'utf-8')
    divided_html = html_code.split(
        '{% include ')  # separate included html templates

    for html in divided_html[1:]:  # exclude part before first include
        include_name = html.split('%}')[0].strip(
            '"\'')  # get name of included html file
        tpl = Template("{% include '" + include_name + "' %}")
        rendered = tpl.render(Context(ctx))
        print(f"#### START INCLUDE: {include_name} ####")
        print(rendered)
        print(f"#### END INCLUDE: {include_name}" + " ####\n")


def debug_includes_files(request, template, ctx):
    """Debugs the included HTML files in a Django template.

    :param request: The request object
    :type request: django.http.HttpRequest
    :param template: The path to the template file
    :type template: str
    :param ctx: The context for rendering the template
    :type ctx: dict
    :return: None
    :rtype: None

    Example usage:

    debug_includes_files(request, 'template/path.html', context)

    """
    html_code = str(render(request, template, ctx).content, 'utf-8')
    divided_html = html_code.split(
        '{% include ')  # separate included html templates

    from pathlib import Path

    filename = Path('debug_output.txt')
    with filename.open('w', encoding='utf-8') as debug_file:
        for html in divided_html[1:]:  # exclude part before first include
            include_name = html.split('%}')[0].strip(
                '"\'')  # get name of included html file
            tpl = Template("{% include '" + include_name + "' %}")
            rendered = tpl.render(Context(ctx))
            debug_file.write(f"#### START INCLUDE: {include_name}" + " ####\n")
            debug_file.write(rendered + "\n")
            debug_file.write(f"#### END INCLUDE: {include_name}" + " ####\n\n")
