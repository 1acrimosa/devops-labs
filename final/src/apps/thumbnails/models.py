from django.db import models

from common.models import TimestampedModel


class Thumbnail(TimestampedModel):
    url = models.URLField()
    max_height = models.IntegerField()
    max_width = models.IntegerField()
    image = models.ImageField(upload_to="thumbnails", blank=True, null=True)

    class Meta:
        verbose_name = "Thumbnail"
        verbose_name_plural = "Thumbnails"

    def __str__(self):
        return self.url
