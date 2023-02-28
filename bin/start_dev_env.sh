#!/bin/bash
set -eux pipefail

docker container run \
	-it \
	--rm \
	--name layman-brothers-loans-services \
	-p 8888:8888 \
	-p 8000:8000 \
	-p 8503:8503 \
	--hostname 0.0.0.0 \
	--log-opt max-size=1g \
	-e PYTHONUNBUFFERED=1 \
	-a stdin \
	-a stdout \
	-v ./src:/app/src \
	-v ./data:/app/data \
	-v ./models:/app/models \
	-v ./docs:/app/docs \
	-v ./notebooks:/app/notebooks \
	-v ./bin:/app/bin \
	-v ./meta:/app/meta  \
	-v ./Makefile:/app/Makefile \
	mlopsde/layman-brothers-loans:latest \
	/bin/bash
