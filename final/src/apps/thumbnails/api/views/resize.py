import logging
import time

from celery.result import AsyncResult
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.metrics.prometheus import (
    resize_image_process_count,
    resize_image_process_time,
    resize_image_request_count,
)
from apps.thumbnails.models import Thumbnail
from apps.thumbnails.tasks import process_thumbnail

logger = logging.getLogger(__name__)


@swagger_auto_schema(
    methods=["GET"],
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def resize(request, max_height, max_width, url) -> Response:
    """
    Resize an image.
    """

    resize_image_request_count.labels(max_width=max_width, max_height=max_height).inc()

    thumbnail, _ = Thumbnail.objects.get_or_create(
        max_height=max_height, max_width=max_width, url=url
    )

    if not thumbnail.image:
        resize_image_process_count.labels(max_width=max_width, max_height=max_height).inc()
        begin_time = time.time()
        result: AsyncResult = process_thumbnail.apply_async(args=[thumbnail.id])
        try:
            result.wait()
        except Exception as e:
            logger.error(e)
        end_time = time.time()
        resize_image_process_time.labels(max_width=max_width, max_height=max_height).observe(
            end_time - begin_time
        )
        thumbnail.refresh_from_db()

    if thumbnail.image:
        return HttpResponse(thumbnail.image.read(), content_type="image/jpeg")
    else:
        thumbnail.delete()
        return HttpResponse("Not Found", status=404)
