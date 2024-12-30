import unittest

from ..utils import get_pil_image_from_url


class UtilsTestCase(unittest.TestCase):

    def test_get_pil_image_from_url(self):
        image = get_pil_image_from_url("https://picsum.photos/1000")
        self.assertIsNotNone(image)
        self.assertEqual(image.width, 1000)
        self.assertEqual(image.height, 1000)
