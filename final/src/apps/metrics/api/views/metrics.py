import logging

from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

logger = logging.getLogger(__name__)


@swagger_auto_schema(
    methods=["GET"],
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def metrics(request) -> Response:
    """
    Return metrics.
    """
    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)
