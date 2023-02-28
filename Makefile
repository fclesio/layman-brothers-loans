.PHONY: help start_dev_env start_services stop_dev_env docker_push tests
help: ## Help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
start_dev_env: ## Start docker-container that setup the development environment
	export DOCKER_BUILDKIT=0  \
	&& export COMPOSE_DOCKER_CLI_BUILD=0 \
	&& sh bin/start_dev_env.sh \
	&& sleep 2 \
	&& docker container ps
start_services: ## Start all services (I) Jupyter, (II) Frontend, (III) RESTFul API
	sh bin/server_run.sh
stop_dev_env: ## Stop docker-container that setup the development environment
	docker container stop layman-brothers-loans-services	
docker_push: ## Push images to the docker registry
	sh bin/docker_push.sh
tests: ## Run all tests
	python -m pytest /app/src/tests/unit_test/test_requirements.py -o log_cli=true --log-cli-level=INFO
