from django.test import TestCase

from ..models import Thumbnail
from ..tasks import process_thumbnail


class AnimalTestCase(TestCase):
    def setUp(self):
        self.thumbnail_good = Thumbnail.objects.create(
            url="https://picsum.photos/1000",
            max_height=100,
            max_width=100,
        )
        self.thumbnail_bad = Thumbnail.objects.create(
            url="https://picsum.photos/",
            max_height=100,
            max_width=100,
        )

    def test_process_thumbnail_good(self):
        process_thumbnail(self.thumbnail_good.id)
        self.thumbnail_good.refresh_from_db()
        self.assertIsNotNone(self.thumbnail_good.image)
        self.assertGreater(self.thumbnail_good.image.size, 0)
        self.assertLessEqual(self.thumbnail_good.image.width, 100)
        self.assertLessEqual(self.thumbnail_good.image.height, 100)

    def test_process_thumbnail_bad(self):
        with self.assertRaises(Exception):
            process_thumbnail(self.thumbnail_bad.id)
