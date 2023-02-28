#!/bin/bash
set -eux pipefail

python -m pytest src/tests/unit_test/test_requirements.py -o log_cli=true --log-cli-level=INFO \

chmod 777 ./bin/start_api.sh &&

chmod 777 ./bin/start_jupyter.sh &&

chmod 777 ./bin/start_frontend.sh &&

chmod 777 ./bin/start_training.sh &&

sh ./bin/start_training.sh &&

parallel -u ::: './bin/start_api.sh' './bin/start_jupyter.sh' './bin/start_frontend.sh' 
