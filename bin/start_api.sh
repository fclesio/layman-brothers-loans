#!/bin/bash
set -eux pipefail

uvicorn main:app --host 0.0.0.0 --port 8000 --app-dir /app/src/main --workers 2 --reload
