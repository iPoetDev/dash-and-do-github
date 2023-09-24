# App Name: kore namespace

#  Copyright (c) 2023.
# ================== URL Patterns ==================
# Changed 2023-08-24
# added: Site Mapping for kore app installation Comments

from django.urls import path

from apps.kore import views

app_name = 'kore'

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
    # path('about/', views.static_about, name='about'),
    # path('fas/', views.static_faq, name='faq'),
    # path('error/', views.error_public, name='error'),
    # path('verify/', views.verify_public, name='verify'),

    path('form_contact/', views.form_contact, name='form_contact'),
    # path('form_signup/', views.signup, name='signup'),
    # path('form_login/', views.login, name='login'),
    # path('form_reset/', views.reset, name='reset'),
]

thirdparty = [
    # External Sources/Credit
    # Django-Htmx: Adapt Chainz
    # https://github.com/adamchainz/django-htmx/blob/main/example/example
    path("favicon.ico", views.favicon),
]

urlpatterns += thirdparty

# handler404 = 'kore.views.core_page_not_found'
