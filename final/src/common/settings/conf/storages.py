from common.environ import env

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = env("STATIC_URL", cast=str, default="/static/")
STATIC_ROOT = env("STATIC_ROOT", cast=str, default="static")
LOCAL_SERVE_STATIC = env("LOCAL_SERVE_STATIC", cast=bool, default=True)


MEDIA_URL = env("MEDIA_URL", cast=str, default="/media/")
MEDIA_ROOT = env("MEDIA_ROOT", cast=str, default="media")
LOCAL_SERVE_MEDIA = env("LOCAL_SERVE_MEDIA", cast=bool, default=True)


STORAGES = {
    "staticfiles": {
        "BACKEND": env(
            "STATICFILES_STORAGE",
            cast=str,
            default="django.contrib.staticfiles.storage.StaticFilesStorage",
        )
    },
    "default": {
        "BACKEND": env(
            "DEFAULT_FILE_STORAGE", cast=str, default="django.core.files.storage.FileSystemStorage"
        )
    },
}
