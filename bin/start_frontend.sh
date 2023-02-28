#!/bin/bash
set -eux pipefail

python -m streamlit run /app/src/main/frontend/streamlit/app.py --server.port 8503
