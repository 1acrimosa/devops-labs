from split_settings.tools import include

from .base import *  # noqa

include(
    "conf/databases/test.py",
    "conf/caches/test.py",
)
