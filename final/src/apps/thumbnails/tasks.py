import logging
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile

from common.celery import app

from .models import Thumbnail
from .utils import get_pil_image_from_url

logger = logging.getLogger(__name__)


@app.task(
    bind=True,
    max_retries=3,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_backoff_max=8,
    retry_jitter=False,
)
def process_thumbnail(self, thumbnail_id: int) -> None:
    """
    Process a thumbnail.
    """
    thumbnail = Thumbnail.objects.get(id=thumbnail_id)

    image = get_pil_image_from_url(thumbnail.url)
    image.thumbnail((thumbnail.max_width, thumbnail.max_height))
    image_io = BytesIO()
    image.save(image_io, format="JPEG")
    thumbnail.image.save(
        f"{thumbnail_id}.jpeg",
        InMemoryUploadedFile(
            image_io,
            None,
            f"{thumbnail_id}.jpeg",
            "image/jpeg",
            image_io.tell,
            None,
        ),
        save=False,
    )
    thumbnail.save()
