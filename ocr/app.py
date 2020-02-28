import flask
import io
import PIL
import pytesseract
import requests

import html_page

from flask import Flask
from flask import request
from io import BytesIO
from PIL import Image
from PIL import ImageFilter

from html_page import HtmlPage

app = Flask(__name__)

@app.route('/')
def home():
    img_url = request.args.get('img')
    title = 'Your image url is {}'.format(img_url)
    text = process_image(img_url)
    html = HtmlPage()
    return html.render(title, img_url, text)

def process_image(url):
    image = _get_image(url)
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)

def _get_image(url):
    return Image.open(BytesIO(requests.get(url).content))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
