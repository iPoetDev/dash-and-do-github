#!/user/bin/env python3
"""@File: <filename>.py .

@Version: 0.3.0 to 0.3.0.?
@Desc: apps | <app> |  <module>
@Author: Charles Fowler
@Copyright: 2023
@Date Created: 23/09/?
@Date Modified: 23/09/??
@Python Version: 3.11.04
@Django Version: 4.2.3/.04/.05
@Notes / Ideas v Implement:
- Added after suvvessful migrations
- TODO: Create a superuser
- Prompt for email address
- No errors to occur
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
# Third Party: Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Local: apps
from apps.users.models import DashUser


class DashUserAdmin(BaseUserAdmin):
    """DashUserAdmin class.

    Credit.

    - Author: Sarthak Kumar(@ksarthak4ever)
    - Title: Django Custom User Model + Allauth for OAuth
    - Date Created: 2019-04-02
    - URL: https://medium.com/
    - USER: @ksarthak4ever/
    - SLUG: django-custom-user-model-allauth-for-oauth-20c84888c3184
    - Last Accessed: 2023-09-24.
    """
    fieldsets = (
        (None,
         {'fields': ('email', 'password', 'name', 'last_login')}),
        ('Permissions',
         {'fields': (
             'is_active',
             'is_staff',
             'is_superuser',
             'groups',
             'user_permissions',
         )}
         ),
    )
    add_fieldsets = (
        (None,
         {
             'classes': ('wide',),
             'fields': ('email', 'password1', 'password2')
         }
         ),
    )

    list_display = ('email', 'name', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(DashUser, DashUserAdmin)
