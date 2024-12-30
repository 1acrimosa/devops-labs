from collections import OrderedDict

from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList

# Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OKResponse(Response):

    default_status = status.HTTP_200_OK

    def __init__(self, data=None, status=None, headers=None):
        if status is None:
            status = self.default_status

        response = {"status": "ok"}

        if data is not None:
            if type(data) is str:
                response["detail"] = data
            elif type(data) in [list, tuple, dict, ReturnDict, OrderedDict, ReturnList]:
                response["data"] = data
            elif data is None:
                pass
            else:
                raise NotImplementedError("Not implemented for type %s." % type(data))

        super(OKResponse, self).__init__(response, status=status, headers=headers)


class BadResponse(Response):

    default_status = status.HTTP_400_BAD_REQUEST

    def __init__(self, data=None, status=None, headers=None):
        if status is None:
            status = self.default_status

        response = {"status": "failed"}

        if data is not None:
            if type(data) is str:
                response["detail"] = data
            elif type(data) in [list, tuple, dict, ReturnDict, OrderedDict, ReturnList]:
                response["data"] = data
            elif data is None:
                pass
            else:
                raise NotImplementedError("Not implemented for type %s." % type(data))

        super(BadResponse, self).__init__(response, status=status, headers=headers)
