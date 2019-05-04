#!/bin/sh
FROM alpine
MAINTAINER bouweceunen

RUN apk update 
RUN apk add --update --no-cache python py-pip 
RUN pip install idna\<2.6
RUN pip install requests==2.21.0
RUN pip install kubernetes

COPY cleanup.py cleanup.py

ENTRYPOINT ["python", "cleanup.py"]
