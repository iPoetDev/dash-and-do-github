# App Name: core namespace

#  Copyright (c) 2023.
# ================== URL Patterns ==================
# Changed 2023-08-24
# added: Site Mapping for core app installation Comments
# TODO: Check these URL Append/Prepend slash patterns

from django.urls import path

from . import views

app_name = 'core'



# ================== Site Map ================================
# URLPatterns - .html Template: DjangoApp => urls.py | views.py
# ================== Core App =======================
# Page: Public & Private
# / - index.html: Home Page => Core Index.urls
# Page Parts: Private
#   > /form_signup/ - Signup Form =>
#      core.urls core.views core.forms core.models
#   > /form_login/ - Login Form =>
#     core.urls| core.views core.forms core.models
#   > /form_password_reset/ - Password Reset Form =>
#      core.urls | core.views core.forms core.models
# Page Parts: Private
#   > /link_logout/ - Accounts/Logout Link => accounts.urls @ Sidebar, Menu | core.view
# Page Parts: All
# / - index.html
#   > /form_contact/ - Password Reset Form => core.urls | core.views core.forms
#                      core.email
# /verify/ - verify.html - Verify Email =>
#        core.urls | core.views core.http (redirect)

"""
#    URLPatterns - Handles Full Pages
    - Index: core.urls | core.views
    - Verify: core.urls | core.views
    - Error: core.urls | core.views
"""
urlpatterns = [
    path('', views.index, name='index'),
    # path('about/', views.static_about, name='about'),
    # path('fas/', views.static_faq, name='faq'),
    # path('error/', views.error_public, name='error'),
    # path('verify/', views.verify_public, name='verify'),
]

"""
# HTMXPatterns - Handles HTMX Requests URLPatterns & Includes
 - Form Contact: core.urls | core.views core.forms core.email
 - Form Signup: core.urls | core.views core.forms core.email core.models
 - Form Login: core.urls | core.views core.forms core.models
 - Form Password Reset: core.urls | core.views core.forms core.email core.models
"""
htmx_patterns = [
    path('form_contact/', views.form_contact, name='contact'),
    # path('form_signup/', views.signup, name='signup'),
    # path('form_login/', views.login, name='login'),
    # path('form_reset/', views.reset, name='reset'),
]

# Appends HTMX Patterns to urlpatterns
urlpatterns += htmx_patterns
