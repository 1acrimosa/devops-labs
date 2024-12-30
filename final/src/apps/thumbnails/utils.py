from io import BytesIO

import requests
from PIL import Image
from PIL.Image import Image as PILImage


def get_pil_image_from_url(url) -> PILImage:
    """
    Get an image.
    """
    response = requests.get(url)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))
