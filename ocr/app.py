import flask
from flask import Flask
from flask import request

import html_page
import ocr
from html_page import HtmlPage
from ocr import OCR

app = Flask(__name__)

@app.route('/')
def home():
    img_url = request.args.get('img')
    if img_url == None or img_url == '':
        return "<p>Please ensure there is a valid img arg</p><p>Example: <a href=\"http://0.0.0.0:5000/?img=https://i.stack.imgur.com/vrkIj.png\">http://0.0.0.0:5000/?img=https://i.stack.imgur.com/vrkIj.png</a>"

    text = OCR(img_url).text()
    html = HtmlPage().render(img_url, text)
    return html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
