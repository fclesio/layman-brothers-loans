init:
	find ./ -type f -exec sed -i -e 's/ml_template/$(PROJECT)/g' {} \;
	find . -name "*-e" -type f -delete
start:
	export DOCKER_BUILDKIT=0  \
	&& export COMPOSE_DOCKER_CLI_BUILD=0 \
	&& docker-compose -f docker-compose.yml up --build --detach \
	&& sleep 5 \
	&& docker container ps
stop:
	docker-compose stop
ecr_push:
	sh ecr_push.sh
lint:
	black --line-length 88 --verbose src
tests:
	python -m pytest /app/src/test/unit_test/test_requirements.py -o log_cli=true --log-cli-level=INFO
