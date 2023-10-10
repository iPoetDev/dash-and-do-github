#!/user/bin/env python3

"""
This module contains the settings from thirdparty config.

@File: thirdparty.py
@Version: 0.2.0 to 0.3.0.?
@Desc: project | dash_and_do | thirdparty.py: 3rd Party config
@Author: Charles Fowler
@Copyright: 2023
@Date Created: 23/08/07
@Date Modified: 23/09/30
@Python Version: 3.11.04
@Django Version: 4.2.3
@Notes / Ideas v Implement:
@Changelog:
-
"""
# ===================== Provider specific settings ===================== #
# Changelog:
# 2023-10-01:
# -added: SOCIALACCOUNT_PROVIDERS
#  - added: 'github'
#  - todo: add Secrets to github

# SOCIALACCOUNT_PROVIDERS = {
#     'github': {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
#         'APP': {
#             'client_id': '123',
#             'secret': '456',
#             'key': ''
#         }
#     }
# }

ANYMAIL = {
    "MAILGUN_API_KEY": "12345",
    "SEND_DEFAULTS": {
        "metadata": {
            "service": "Dash and Do",
        },
        "tags": [ "dash-and-do" ],
        "track_clicks": False,
        "track_opens": False,

    },
    "IGNORE_RECIPIENT_STATUS": True,
    "IGNORE_UNSUPPORTED_FEATURES": True,
    "REQUESTS_TIMEOUT": (30.0, 60.0),
    "DEBUG_API_REQUESTS": False,
}

# https://docs.sentry.io/platforms/python/guides/logging/
# sentry_logging = LoggingIntegration(
#     level=logging.INFO,        # Capture info and above as breadcrumbs
#     event_level=logging.ERROR  # Send errors as events
# )

# sentry_sdk.init(
#     dsn="https://70bb04b94d9483eb6591c7d8f4d0221e@o4505894567346176.ingest
#     .sentry.io/4505894604242944",
#     # https://docs.sentry.io/platforms/python/guides/django/
#     integrations=[
#         DjangoIntegration(
#             transaction_style='url',
#             middleware_spans=True,
#             signals_spans=False,
#             cache_spans=False,
#         ),
#     ],
#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     # https://docs.sentry.io/platforms/python/guides/django/#behavior
#     send_default_pii=True,
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production.
#     traces_sample_rate=1.0,
#     # Set profiles_sample_rate to 1.0 to profile 100%
#     # of sampled transactions.
#     # We recommend adjusting this value in production.
#     profiles_sample_rate=1.0,
# )
#
# SENTRY = sentry_sdk
# SENTY_LOGGING = sentry_logging
