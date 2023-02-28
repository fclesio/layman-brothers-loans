#!/bin/bash
set -eux pipefail


python -m pytest src/tests/unit_test/test_requirements.py -o log_cli=true --log-cli-level=INFO \
&& python3 src/main/model_training.py
