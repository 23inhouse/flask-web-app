This is a demo flask web app that accepts an img url and uses ocr to display the text below the image.

```bash
docker build -t flask-web-app:latest .
```

```bash
docker run -p 5000:5000 flask-web-app
```

```bash
open http:0.0.0.0:5000
```

Example:

```bash
open http://0.0.0.0:5000/?img=https://www.pyimagesearch.com/wp-content/uploads/2017/06/tesseract_header.jpg
```
