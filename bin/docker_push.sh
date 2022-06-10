#!/bin/bash

set -euo pipefail

VERSION="latest"

docker build -t mlopsde/layman-brothers-loans:$VERSION . &&\
docker push mlopsde/layman-brothers-loans:$VERSION
