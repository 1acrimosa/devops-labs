# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

from django.utils.translation import gettext_lazy

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

LANGUAGE_CODE = "en-UK"

LOCALE_PATHS = ["locale"]

USE_L10N = True

LANGUAGES = (
    ("en", gettext_lazy("English")),
    ("kk", gettext_lazy("Kazakh")),
    ("es", gettext_lazy("Spain")),
)
