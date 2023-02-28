#!/bin/bash
set -eux pipefail

API_VERSION="0.0.1"
DOCKER_REPO="mlopsde"
APP_NAME="layman-brothers-loans"


docker image build --tag $DOCKER_REPO/$APP_NAME:latest --shm-size=8g . && \
docker image push $DOCKER_REPO/$APP_NAME:latest


docker image build --tag $DOCKER_REPO/$APP_NAME:$API_VERSION --shm-size=8g . && \
docker image push $DOCKER_REPO/$APP_NAME:$API_VERSION
