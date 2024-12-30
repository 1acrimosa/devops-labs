INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party
    "rest_framework",
    "drf_spectacular",
    "drf_yasg",
    "corsheaders",
    "django_prometheus",
    "health_check",
    "health_check.cache",
    "health_check.storage",
    "health_check.contrib.migrations",
    "health_check.contrib.celery_ping",
    "health_check.contrib.redis",
    # Local
    "apps.metrics",
    "apps.thumbnails",
]
