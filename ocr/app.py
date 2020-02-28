import flask

import html_page
import ocr

from flask import Flask
from flask import request

from html_page import HtmlPage
from ocr import OCR

app = Flask(__name__)

@app.route('/')
def home():
    try:
        img_url = request.args.get('img')
        title = 'Your image url is {}'.format(img_url)
        text = OCR(img_url).text()
        html = HtmlPage()
        return html.render(title, img_url, text)
    except ValueError:
        return "<p>Please ensure there is a valid img arg</p><p>Example: <a href=\"http://0.0.0.0:5000/?img=https://i.stack.imgur.com/vrkIj.png\">http://0.0.0.0:5000/?img=https://i.stack.imgur.com/vrkIj.png</a>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
