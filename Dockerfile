FROM python:3.9

MAINTAINER Hugo Aguiar Martinez <martinez.avellan@icloud.com>

EXPOSE 5000

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD python application.py