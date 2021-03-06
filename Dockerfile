FROM ubuntu:20.04

MAINTAINER Benjamin Lewis "23inhouse@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3 python3-dev python3-pip \
    tesseract-ocr

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

RUN python3 -m unittest discover -s ocr -p '*_test.py'

ENTRYPOINT [ "python3" ]

CMD [ "ocr/app.py" ]
