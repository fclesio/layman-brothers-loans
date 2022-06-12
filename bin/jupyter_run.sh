#!/bin/bash

black src/* \
&& python -m pytest src/tests/unit_test/test_requirements.py -o log_cli=true --log-cli-level=INFO \
&& jupyter notebook --generate-config --allow-root \
&& echo "c.NotebookApp.password = u'sha1:6a3f528eec40:6e896b6e4828f525a6e20e5411cd1c8075d68619'" >> /root/.jupyter/jupyter_notebook_config.py \
&& sleep 2

uvicorn main:app --host 0.0.0.0 --port 80 --app-dir /app/src/main --workers 2 --reload &
jupyter notebook --allow-root --notebook-dir=. --ip=0.0.0.0 --port=8888 --no-browser &
cd src; streamlit run /app/src/main/frontend/streamlit/app.py --server.port 8503 &
wait
