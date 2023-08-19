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

from django.contrib.auth import views as auth_views
from django.conf import settings

from dash_and_do import settings as project_settings

# ================== URL Patterns ==================
# Changed 2023-08-15
# added: URL + includes for DEV when Admin enabled
# added: URL + includes for Debug Toolbar when Admin enabled
# added: URL + includes for Admin Password reset when Admin enabled
# added: URL + includes for Admin Docs when Admin enabled
# Changed 2023-08-16:
# added: URL + includes for AllAuth for accounts & Commented Out
# added: URL + includes for Accounts for accounts & Commented Out
# added: URL + includes for Dash accounts & Commented Out
# noted : Progressive enablement of Accounts, Dash, AllAuth
# Noted: that you do not need the URLs provided by django.contrib.auth.urls
# Noted: can use the URLs provided by allauth:
#  - account_login,
#  - account_logout,
#  - account_set_password


urlpatterns = [
    path('admin/', admin.site.urls),
    #path("__debug__/", include("debug_toolbar.urls")),
    path('core/', include('core.urls')),
    # path('accounts/', include('accounts.urls')),
    # path('accounts/', include('allauth.urls')),
    # path('dash/', include('dash.urls')),
]
