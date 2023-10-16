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
from django.conf import settings
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
# added: Core index forms to kore.urls

from django.conf import settings
from django.urls import include, path
from django.contrib import admin

urlpatterns = [] # Base variable defintion

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += [
    path('admin/', admin.site.urls),
    path('', include('apps.kore.urls', namespace='kore')),
    path('', include('apps.users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),
]
# path('profile/', include('profile.urls', namespace='profile')),
# path('profile/', include('allauth.urls', namespace='profile')),
# path('dash/', include('dash.urls', namespace='dash'))
