FROM python:3.9.7-alpine

WORKDIR /Backend

COPY . /Backend
## 
RUN pip install -r requirements.txt

##Adding kyle Baldwin's container
FROM ubuntu:focal
## MAINTAINER is depricated?
LABEL Kyle Baldwin <kwb@mail.sfsu.edu>

RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.utf8
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y wget

RUN wget https://lilypond.org/download/binaries/linux-64/lilypond-2.22.1-1.linux-64.sh

RUN sh lilypond-2.22.1-1.linux-64.sh

CMD ["python","app.py"]