import io
import PIL
import pytesseract
import requests

from io import BytesIO
from PIL import Image
from PIL import ImageFilter

class OCR:

    def __init__(self, img_url = ''):
        self.img_url = img_url

    def text(self):
        return self._process_image(self.img_url)

    def _process_image(self, img_url = ''):
        if img_url == '':
            return ''

        try:
            image = self._get_image(img_url)
            image.filter(ImageFilter.SHARPEN)
            return pytesseract.image_to_string(image)
        except:
            return "Couldn't process the image"

    def _get_image(self, img_url = ''):
        return Image.open(BytesIO(requests.get(img_url).content))
