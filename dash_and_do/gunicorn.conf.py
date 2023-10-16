#!/user/bin/env python3
"""@File: gunicorn.conf.py
    @Version: 0.3.0 to 0.3.0.?
    @Desc: dash_and_do | gunicorn | gunicorn.conf:
           Configuration for gunicorn WSGI server.
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/10/10
    @Date Modified: 23/10/10
    @Python Version: 3.11.04
    @Django Version: 4.2.6
    @Changelog:
    - Added:
        - added: Created initial file: 23/10/11:
    - Updated:
        - updated: Use Environ.get() for Heroku $PORT, default: 8080: 23/10/11
        - updated: enabled reload for development: 23/10/11
        - updated: enabled preload_app for Django: 23/10/11
        - updated: added timeout (120 seconds): 23/10/11
    - linked: Procfile:
        - `web: gunicorn dash_and_do.wsgi -c ./dash_and_do/gunicorn.conf.py`
        - `log-file -` : direct to stdout
        - `log-level info` : info level
           The available log levels for Gunicorn, in increasing order:
            critical: Only really important messages are logged.
                This is the highest level of severity.
                error: Regular error messages are logged.
                This usually means something has gone wrong.
            warning: Warning messages are logged.
                This usually means something unexpected happened,
                or there may be some issue coming up.
            info: Regular informational messages are logged.
                This is the default log level if none is specified.
            debug: Full debug messages are logged.
                This includes lower level system details, and
                is usually used when debugging issues.
    - linked: heroku logs --tail
        - Heroku CLI and log in using heroku login.
    @Plan:
        - TODO:
        - FIXME:
        - CHECK:

Free Tier (web Dyno) Heroku.
    - 1 web dyno
    - 1 worker dyno
    - 10k rows Postgres
    - 512mb RAM
    - 1gb disk space

 gunicorn WSGI server configuration.
# If you are using Django and PostgreSQL,
it's a good idea to set preload_app = True.
This setting will reduce the time needed for a new worker to boot up

"""
from os import environ
from dash_and_do.settings import DEBUG
# envs load from .env file in settings and imports to settings
# Works locally and on Heroku.
from dash_and_do.settings import envs

# The Proc file has
# web: gunicorn dash_and_do.wsgi -c dash_and_do/gunicorn.conf.py --log-file - --log-level debug


# Load a flah to toggle Heroku Local
HEROKU_LOCAL = envs.bool('HEROKU_LOCAL')
# Differentiate Heroku Local Port from Runserver Port
HEROKU_LOCAL_PORT = envs.str('HEROKU_LOCAL_PORT', '8001')

# Heroku Local: Mimic Heroku Dyno, Gunicorn
if DEBUG and HEROKU_LOCAL:
    # Default condition for local development
    bind = f'127.0.0.1:{HEROKU_LOCAL_PORT}'
elif not DEBUG and HEROKU_LOCAL:
    # Test condition for local development
    bind = f'127.0.0.1:{HEROKU_LOCAL_PORT}'

# Heroku Remote: Network Access
if not DEBUG and not HEROKU_LOCAL:
    # Default condition for remote/production
    bind = '0.0.0.0:' + environ.get('PORT', '8000')
elif DEBUG and not HEROKU_LOCAL:
    # Test condition for remote/production
    bind = '0.0.0.0:' + environ.get('PORT', '8000')

# Free Tier
workers = 1
timeout = 120
reload = True  # for development
preload_app = True
# workers = environ.get('GUNICORN_FREEWEB_DYNO', 1)
# timeout = environ.get('GUNICORN_TIMEOUT', 120)
# reload = environ.get('GUNICORN_RELOAD', True)  # for development
# preload_app = environ.get('GUNICORN_PRELOAD_APP', True)
