FROM python:3.8.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER=1
ENV LANG=C.UTF-8

RUN apt-get update -qq && apt-get install -y \
  && apt-get -y install nano \
  vim \
  dumb-init \
  build-essential \
  gcc \
  libgmp3-dev \
  libpq-dev \
  parallel \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /app \
    && mkdir /app/src \
    && mkdir /app/data \
    && mkdir /app/models \
    && mkdir /app/docs \
    && mkdir /app/notebooks \
    && mkdir /app/bin \
    && mkdir /app/meta

WORKDIR /app

COPY src /app/src
COPY models /app/models
COPY notebooks /app/notebooks
COPY bin /app/bin
COPY meta /app/meta
COPY Makefile /app/Makefile
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

EXPOSE 8888
EXPOSE 8000
EXPOSE 8503

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD ["/bin/bash", "-c", "./bin/server_run.sh"]
