import logging
from collections import OrderedDict

from rest_framework.exceptions import ErrorDetail
from rest_framework.utils.serializer_helpers import ReturnDict

from common.api.exceptions import APIError

logger = logging.getLogger(__name__)


def _collect_errors(key, value, errors):
    if type(value) in [str, ErrorDetail]:
        errors[key] = value
    elif type(value) in [list, tuple]:
        if len(value) == 1 and type(value[0]) in [str, ErrorDetail]:
            errors[key] = value[0]
        else:
            for index, v in enumerate(value):
                _collect_errors("%s:%s" % (key, index), v, errors)
    elif type(value) in [dict, OrderedDict, ReturnDict]:
        for k in value:
            _collect_errors("%s:%s" % (key, k), value[k], errors)
    else:
        raise NotImplementedError("Unsupperted type: %s." % type(value))


def validate_serializer_or_raise_exception(serializer):
    serializer.is_valid()
    if bool(serializer.errors):
        errors = {}
        _collect_errors("", serializer.errors, errors)
        error_text = "\n".join(["[%s] — %s" % (key[1:], value) for key, value in errors.items()])
        logger.warning("Serializer Errors: %s" % errors)
        raise APIError(error_text, data=serializer.errors)
