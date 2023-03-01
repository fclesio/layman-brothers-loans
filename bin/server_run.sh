#!/bin/bash
set -eux pipefail

chmod 777 ./bin/start_api.sh &&

chmod 777 ./bin/start_jupyter.sh &&

chmod 777 ./bin/start_frontend.sh &&

parallel -u ::: './bin/start_api.sh' './bin/start_jupyter.sh' './bin/start_frontend.sh' 
