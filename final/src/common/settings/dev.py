from split_settings.tools import include

from .base import *  # noqa

include(
    "conf/databases/dev.py",
    "conf/caches/dev.py",
)
