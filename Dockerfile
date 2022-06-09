FROM python:3.8.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER=1
ENV LANG=C.UTF-8

RUN apt-get update -qq && apt-get install -y \
  && apt-get -y install nano \
  dumb-init \
  build-essential \
  gcc \
  libgmp3-dev \
  libpq-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && pip install --upgrade pip

RUN mkdir /app \
    && mkdir /app/src \
    && mkdir /app/data \
    && mkdir /app/models \
    && mkdir /app/docs \
    && mkdir /app/notebooks \
    && mkdir /app/bin \
    && mkdir /app/meta

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY Makefile /app/Makefile
COPY src /app/src


RUN pip install -r /app/requirements.txt

EXPOSE 8888
EXPOSE 80

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD ["/bin/bash"]
