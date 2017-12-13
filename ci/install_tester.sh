#!/usr/bin/env bash
# install test environment
conda install -y coverage > tmp.txt && echo "alive";
if [[ "$PHYNIX_PYTHON_VERSION" > 2.6 ]]; then
    pip install coveralls > tmp.txt && echo "alive";
fi
pip install hypothesis
