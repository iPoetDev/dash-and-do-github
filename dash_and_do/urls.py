"""URL configuration for dash_and_do project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. ✅ Import the include() function: from django.urls import include, path
    2. ✅ Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

Changelog:
2023-08-09
- Added URL + includes for Core/Dash/Accounts
"""

#  Copyright (c) 2023.

from django.contrib import admin
from django.urls import include
from django.urls import path

# ================== URL Patterns ==================
# Changed 2023-08-15
# added: URL + includes for DEV when Admin enabled
# added: URL + includes for Debug Toolbar when Admin enabled
# added: URL + includes for Admin Password reset when Admin enabled
# added: URL + includes for Admin Docs when Admin enabled
# Changed 2023-08-16:
# added: URL + includes for AllAuth for profile & Commented Out
# added: URL + includes for Accounts for profile & Commented Out
# added: URL + includes for Dash profile & Commented Out
# noted : Progressive enablement of Accounts, Dash, AllAuth
# Noted: that you do not need the URLs provided by django.contrib.auth.urls
# Noted: can use the URLs provided by allauth:
#  - account_login,
#  - account_logout,
#  - account_set_password
# Changed 2023-08-24:
# added: SiteMap in Comments as a Planner
# added: Core index forms to core.urls

# ================== Site Map ================================
# URLPatterns - .html Template: DjangoApp => urls.py | views.py
# ================== Core App =======================
#   Page: Public & Private
# / - index.html: Home Page => Core Index.urls
#   Page Parts: Private
#   > /form_signup/ - Signup Form => core.urls core.views core.forms core.models
#   > /form_login/ - Login Form => core.urls| core.views core.forms core.models
#   > /form_password_reset/ - Password Reset Form => core.urls | core.views
#     core.forms core.models
#   Page Parts: Private
#   > /link_logout/ - Accounts/Logout Link => profile.urls @ Sidebar, Menu | core.view
#   Page Parts: All
#   > /form_contact/ - Password Reset Form => core.urls | core.views core.forms
#                      core.email
# /verify/ - verify.html - Verify Email => core.urls | core.views core.http
# (redirect)
# ================== Accounts App ==================
#   Page: Private
# /account/ - profile.html: Accounts => profile.urls
#   Page Parts: Private
#   /profile/ - profile.html: Accounts/Profile => dash.urls
#   Page Parts: Private
#   > /form_profile/ - Profile Form => profile.urls
#   > /form_password_change/ - Password Change Form => profile.urls
#   /github/ - github.html: GitHub Integration
#   Page Parts:
#   > /form_github_token/ - Password Reset Form => profile.urls
#   /link_logout/ - Accounts/Logout Link => profile.urls
# ================== Dash App ======================
#   Page: Private
# /dash/ - Dash.html => dash.urls
# ================== Do'er App ======================
# ================== Admin App ======================
# IF DEBUG:
# /admin/ - Admin Site => admin.site.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    # index.html (root) is in core.urls
    path('', include('core.urls', namespace='core')),
    # index forms is in core.urls
    # path('form_signup/', include('core.urls.signup', namespace='core')),
    # path('form_login/', include('core.urls.login', namespace='core')),
    # path('form_reset/', include('core.urls.pwd_reset', namespace='core')),
    path('form_contact/', include('core.urls', namespace='core')),
    # path('profile/', include('profile.urls', namespace='profile')),
    # path('profile/', include('allauth.urls', namespace='profile')),
    # path('dash/', include('dash.urls, namespace='dash'')),
]
