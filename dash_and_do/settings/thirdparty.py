"""


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
        "tags": ["dash-and-do"],
        "track_clicks": False,
        "track_opens": False,

    },
    "IGNORE_RECIPIENT_STATUS": True,
    "IGNORE_UNSUPPORTED_FEATURES": True,
    "REQUESTS_TIMEOUT": (30.0, 60.0),
    "DEBUG_API_REQUESTS": False,
}
