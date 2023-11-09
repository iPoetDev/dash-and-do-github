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
    - DONE: PyLint: 2023-10-??
    - DONE: Ruff: 2023-10-??
    - IGNORE: PyLint:
"""


class SiteMeta:  # pylint: disable=too-few-public-methods
    """Site Meta Data TITLE = 'title' URL = 'url' PERSON = 'person' DESCRIPTION
    = 'description' KEYWORDS = 'keywords' CONTACT = 'contact'.
    """
    NAME = 'Dashboard and Do GitHub Manager'
    URL = 'https://dash-and-do.herokuapp.com/'
    PERSON = 'Charles J Fowler, @iPoetDev.github.com'
    DESC = 'A GitHub Portfolio Manager for the Dashboard and Do '
    COPY = ('The Dash and Document GitHub is the '
            'copyright of Charles J Fowler, 2023-2028')
    KEYWORDS = 'GitHub, Portfolio, Manager, Dashboard, Do, '
    CONTACT = 'Github: @iPoetDev'


class Brand:  # pylint: disable=too-few-public-methods
    """Brand Names."""


    class Site:  # pylint: disable=too-few-public-methods
        """Site Brand Names."""
        NAME = 'Dashboard and Do GitHub Manager'
        SHORT_NAME = 'Dash and Do'
        LOGO = 'dash_and_do/logo.png'
        LOGO_ALT = 'Dash and Do Logo'
        LOGO_TITLE = 'Dash and Do Logo'
        FAVICON = 'dash_and_do/favicon.ico'
        FAVICON_ALT = 'Dash and Do Favicon'
        FAVICON_TITLE = 'Dash and Do Favicon'


    class FAVICON:
        """Favicon Configuration."""
        XMLNS = 'http://www.w3.org/2000/svg'
        VBOX = '0 0 100 100'
        VIEWY = '.9em'
        FONTSIZE = '90'
        ICON = '🦊'
        FORMAT = 'image/svg+xml'


class Page:  # pylint: disable=too-few-public-methods
    """Page Titles."""


    class Index:  # pylint: disable=too-few-public-methods
        """Index Page Details."""
        USE = 'all'
        TITLE = 'Home: Dashboard and Do GitHub Manager'
        ATITLE = 'Home: Dashboard and Do GitHub Manager'
        ATEXT = 'Home'


    class About:  # pylint: disable=too-few-public-methods
        """About Page Details | Static."""
        USE = 'menu_public'
        TITLE = 'About: Dashboard and Do GitHub Manager'
        ATITLE = 'About: Dashboard and Do GitHub Manager'
        ATEXT = 'About'


    class Verify:  # pylint: disable=too-few-public-methods
        """About Page Details | Static."""
        USE = 'services_public'
        IA = 'orphan'
        NAV = 'excluded'
        ROLE = 'services'
        FLOW = 'signup -> email_confirm -> verify -> index -> login'
        DESC: str = 'user confirmations and verification statuses'
        TITLE = 'Verify: Dashboard and Do GitHub Manager'
        ATITLE = 'Verify: Dashboard and Do GitHub Manager'
        ATEXT = 'Verify'


    class Confirm:  # pylint: disable=too-few-public-methods
        """About Page Details | Static."""
        USE = 'services_public'
        IA = 'orphan'
        NAV = 'excluded'
        ROLE = 'services'
        FLOW = ('signup -> verify -> email_confirm (link) -> confirm -> index '
                '->ogin')
        DESC: str = 'user confirmations and verification statuses'
        TITLE = 'Confirm: Dashboard and Do GitHub Manager'
        ATITLE = 'Confirm: Dashboard and Do GitHub Manager'
        ATEXT = 'Confirm'


    class Contact:  # pylint: disable=too-few-public-methods
        """Contact Section Partial/Fragment Details."""
        USE = 'menu_public'
        TITLE = 'Contact: Dashboard and Do GitHub Manager'
        ATITLE = 'Contact Us: Send an Message to Dash and Do'
        ATEXT = 'Contact'


    class AccountMenu:  # pylint: disable=too-few-public-methods
        """Account Menu Details."""
        USE = 'menu_private'
        MENU_TITLE = 'Accounts Menu'
        ACCOUNT_BUTTEXT = 'Account'
        PROFILE_ATITLE = 'Accounts: View your account profile'
        PROFILE_ATEXT = 'Profile'
        GITHUB_ATITLE = 'GitHub: Connect GitHub to your profile'
        GITHUB_ATEXT = 'Connect'
        SETTINGS_ATITLE = 'Settings: Manwge your profile'
        SETTINGS_ATEXT = 'Settings'
        LOGOUT_ATITLE = 'Logout: Sign Out of your profile'
        LOGOUT_ATEXT = 'Logout'


class SiteContext:
    """Site Context."""

    @property
    def context(self):
        """Provides the context data for use in all full page views.

        :return: A dictionary containing the full page views's context data .
            - 'sitename': The name of the site (SiteMeta.NAME).
            - 'siteurl': The url of the site (SiteMeta.URL).
            - 'siteperson': The person of the site (SiteMeta.PERSON).
            - 'sitedesc': The description of the site (SiteMeta.DESC).
            - 'siteright': The rights of the site (SiteMeta.COPY).
            - 'sitekeywords': The keywords of the site (SiteMeta.KEYWORDS).
            - 'sitecontact': The contact of the site (SiteMeta.CONTACT).
            - 'website': The website of the site (SiteMeta).
            - 'brand': The brand of the site (Brand).
            - 'page': The page of the site (Page).
        """
        return {
            'site': SiteMeta.NAME,
            'siteurl': SiteMeta.URL,
            'siteperson': SiteMeta.PERSON,
            'sitedesc': SiteMeta.DESC,
            'siteright': SiteMeta.COPY,
            'sitekeywords': SiteMeta.KEYWORDS,
            'sitecontact': SiteMeta.CONTACT,
            'website': SiteMeta,
            'brand': Brand,
            'page': Page
        }

    @property
    def index(self):
        """Provides the context data for the index view.

        :return: A dictionary containing the context data for the index view.
            - 'title': The title of the page (Page.Index.TITLE).
        """
        return {
            'title': Page.Index.TITLE,
        }

    @property
    def verify(self):
        """Provides the context data for the verify view.

        :return: A dictionary containing the context data for the verify view.
            - 'title': The title of the page (Page.Index.TITLE).
        """
        return {
            'title': Page.Verify.TITLE,
        }

    @property
    def confirm(self):
        """Provides the context data for the confirm view.

        :return: A dictionary containing the context data for the confirm view.
            - 'title': The title of the page (Page.Index.TITLE).
        """
        return {
            'title': Page.Confirm.TITLE,
        }

    # @property
    # def brand(self):
    #     """Provides the context data for the confirm view.
    #
    #     :return: A dictionary containing the context data for the confirm view.
    #         - 'title': The title of the page (Page.Index.TITLE).
    #     """
    #     return {
    #         'brand': Brand,
    #     }
