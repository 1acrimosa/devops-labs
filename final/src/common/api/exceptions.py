from rest_framework import status
from rest_framework.exceptions import ValidationError


class APIError(ValidationError):

    def __init__(self, detail, data=None):
        response = {
            "status": "failed",
            "detail": detail,
        }
        if data is not None:
            response["data"] = data
        super().__init__(response, status.HTTP_400_BAD_REQUEST)
