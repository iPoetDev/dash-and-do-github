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
    - DONE: PylInt: 23/09/30
    - IGNORE: PylInt: Invalid name "app_name"
      (should match ((?![0-9])\w+) pattern) (invalid-name)
"""
from django.urls import path
from apps.users import views

# Namespace for URL Patterns: users:route_link_reference
app_name = 'users'  # pylint: disable=invalid-name
"""
#    URLPatterns - Handles AllAuth
    - AllAuth Views/Templates: users.urls | kore.views
"""

urlpatterns = [
    path('login/', views.DashLoginView.as_view(), name='account_login'),
    path('logout/', views.DashLogoutView.as_view(), name='account_logout'),
    path('signup/', views.DashSignupView.as_view(), name='account_signup'),
    path(
        "confirm-email/<str:key>/",
        views.DashConfirmEmailView.as_view(),
        name="account_confirm_email",
    ),
    # including allauth urls
    # Other views@
    # 1) Password reset
    # 2) Password change & set
    # 3) Email change
    # 4) Account management
]
