"""
This module contains the views for the core app.

Changlog: 2023-08-24
    - noted: Use function based views for the core app.
    - added: login_required decorator to all puiblic views
    - added: login_required decorator to all private views
"""
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# ========================== Public Form Views =================================

"""
Form for Signup
Decorator to check if the user is logged in before executing the
form_signup function.

:param request: The HTTP request object.

:return: None

:raises: None
"""

def form_signup(request):
    # view function code here

"""

Use decorator that checks if the user is authenticated before allowing access
to the function.

:param request: The HTTP request object.
:return: None
:exceptions: None
"""

def form_login(request):
    # view function code here

"""
Form Login function. | Access: Only Authenticated Users

:param request: The HTTP request object.

:return: None

:raises: None
"""

def form_password_reset(request):
    # view function code here

# ========================== Public Form Views =================================
"""
Form contact function. | Access: All Users

:param request: The HTTP request object.

:return: None

:raises: None
"""
def form_contact(request):
    # view function code here
