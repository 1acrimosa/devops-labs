from common.environ import env

# Django REST Framework
# https://www.django-rest-framework.org/api-guide/settings/

DISABLE_THROTTLING = env("DISABLE_THROTTLING", cast=bool, default=False)
MAX_PAGE_SIZE = env("MAX_PAGE_SIZE", cast=int, default=1000)

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    "DEFAULT_PAGINATION_CLASS": "common.api.paginations.CustomLimitOffsetPagination",
    "PAGE_SIZE": env("PAGE_SIZE", cast=int, default=100),
    "DEFAULT_THROTTLE_RATES": {
        "anon-auth": "10/min",
    },
}

SPECTACULAR_DEFAULTS = {"SERVE_PERMISSIONS": ["rest_framework.permissions.IsAuthenticated"]}
