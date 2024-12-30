"""
Django settings for project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from split_settings.tools import include

include(
    "conf/core.py",
    "conf/installed_apps.py",
    "conf/middleware.py",
    "conf/storages.py",
    "conf/localization.py",
    "conf/password.py",
    "conf/templates.py",
    "conf/secrets.py",
    "conf/security.py",
    "conf/logging.py",
    "conf/http.py",
    "conf/celery.py",
    "conf/api.py",
    "conf/redis.py",
    "conf/healthcheck.py",
    "conf/swagger.py",
)