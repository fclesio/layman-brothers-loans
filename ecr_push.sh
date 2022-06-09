#!/bin/bash
set -euo pipefail

VERSION="latest"

aws ecr get-login-password --region us-east-1 | \
docker login --username AWS --password-stdin 585031190124.dkr.ecr.us-east-1.amazonaws.com && \
docker build -t layman_brothers_loans:$VERSION . &&\
docker tag layman_brothers_loans:$VERSION 585031190124.dkr.ecr.us-east-1.amazonaws.com/layman_brothers_loans:$VERSION && \
docker push 585031190124.dkr.ecr.us-east-1.amazonaws.com/layman_brothers_loans:$VERSION
