#!/bin/bash
set -eux pipefail

jupyter notebook --generate-config --allow-root \
&& echo "c.NotebookApp.password = u'sha1:6a3f528eec40:6e896b6e4828f525a6e20e5411cd1c8075d68619'" >> /root/.jupyter/jupyter_notebook_config.py \
&& jupyter notebook --allow-root --notebook-dir=. --ip=0.0.0.0 --port=8888 --no-browser
