#!/user/bin/env python3
"""@File: utils.py
@Version: 0.3.0 to 0.3.1: Contact Form & Email
@Desc: common | dash-and-do |  utilde: Helper Functions
@Author: Charles Fowler
@Copyright: 2023
@Date Created: 23/09/13
@Date Modified: 23/09/113
@Python Version: 3.11.04
@Django Version: 4.2.3
@Notes / Ideas v Implement:
- Common Utility functions, prohector wide.
- Move into own custom module/app?
@Changelog:
- Added:
- 23/09/12: Added docstrings
- 23/09/12: Created initial file
- 23/09/12: added Projects Common Utility Functions
- Updated:
- Deprecated:
- 23/09/12: Deprecated
- Removed:
- 23/09/12: Removed
@Plan:
"""

import datetime
from bs4 import BeautifulSoup

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def get_date():
    """Gets the formated current date and time.

    Common Utility Function :scope: Site Wide
    :return: current_datetime: datetime: Current date and time.
    """
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime(DATE_FORMAT)


def escape_html_and_newlines(data):
    soup = BeautifulSoup(data, "html.parser")
    text = soup.get_text()
    return text.replace('\n', '  -  ')

def get_error_detail(response):
    if hasattr(response, "content"):
        content = response.content
        if isinstance(content, bytes):
            content = content.decode('utf-8')
        return escape_html_and_newlines(content)
    return "Unknown error"
