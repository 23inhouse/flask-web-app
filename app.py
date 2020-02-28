import flask
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    img_url = request.args.get('img')
    title = 'Your image url is {}'.format(img_url)
    html = '<p>{}</p><p><img src="{}"/></p>'.format(title, img_url)
    return html


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
