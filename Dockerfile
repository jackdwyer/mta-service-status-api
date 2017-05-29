FROM python:alpine

RUN apk update && apk add libxslt-dev gcc g++

RUN mkdir -p /opt/mta-service-status-api
COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

COPY worker.py app.py config.py /opt/mta-service-status-api/

WORKDIR /opt/mta-service-status-api
