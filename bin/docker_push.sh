#!/bin/bash
set -eux pipefail

VERSION="latest"

docker build -t mlopsde/layman-brothers-loans:$VERSION . &&\
docker push mlopsde/layman-brothers-loans:$VERSION
