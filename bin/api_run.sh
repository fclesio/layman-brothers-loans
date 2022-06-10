#!/bin/bash

black src/* \
&& python -m pytest src/tests/unit_test/test_requirements.py -o log_cli=true --log-cli-level=INFO \
&& uvicorn main:app --host 0.0.0.0 --port 80 --app-dir /app/src/main --workers 2 --reload
