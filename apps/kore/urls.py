#!/user/bin/env python3
"""This module contains the views for the kore app.

@File: views.py
@Version: 0.3.0 to 0.3.0.?
@Desc: apps | kore |  urls: URLSConf for kore app
@Author: Charles Fowler
@Copyright: 2023
@Date Created: 23/08/07
@Date Modified: 23/09/30
@Python Version: 3.11.04
@Django Version: 4.2.3
@Notes / Ideas v Implement:
@Changelog:
"""

from django.urls import path

from apps.kore import views


app_name = 'kore'  # pylint: disable=invalid-name

# ================== Site Map ================================
# URLPatterns - .html Template: DjangoApp => urls.py | views.py
# ================== Core App =======================
# Page: Public & Private
# / - index.html: Home Page => Core Index.urls
# Page Parts: Private
#   > /form_signup/ - Signup Form =>
#      kore.urls kore.views kore.forms kore.models
#   > /form_login/ - Login Form =>
#     kore.urls| kore.views kore.forms kore.models
#   > /form_password_reset/ - Password Reset Form =>
#      kore.urls | kore.views kore.forms kore.models
# Page Parts: Private
#   > /link_logout/ - Accounts/Logout Link => profile.urls @ Sidebar, Menu |
#   kore.view
# Page Parts: All
# / - index.html
#   > /form_contact/ - Password Reset Form => kore.urls | kore.views kore.forms
#                      kore.email
# /verify/ - verify.html - Verify Email =>
#        kore.urls | kore.views kore.http (redirect)
"""
#    URLPatterns - Handles Full Pages
    - Index: kore.urls | kore.views
    - Verify: kore.urls | kore.views
    - Error: kore.urls | kore.views
"""

urlpatterns = [
    path('', views.index, name='index'),
    path('private/', views.private, name='private'),
    # path('about/', views.static_about, name='about'),
    # path('fas/', views.static_faq, name='faq'),
    # path('error/', views.error_public, name='error'),
    path('verify/', views.verify_public, name='verify'),
    path('confirm/', views.confirm_public, name='confirm'),
    # MidSection from Index GET /
    path('midsection/', views.midsectionpartial, name='midsection'),
    # Forms
    path('form_contact/', views.form_contact, name='form_contact'),
]

thirdparty = [
    # External Sources/Credit
    # Django-Htmx: Adapt Chainz
    # https://github.com/adamchainz/django-htmx/blob/main/example/example
    path('favicon.ico', views.favicon),
]

urlpatterns += thirdparty

# handler404 = 'kore.views.core_page_not_found'
