#!/usr/bin/env bash
# install test environment
conda install -y coverage > tmp.txt && echo "alive";
pip install coveralls > tmp.txt && echo "alive";
pip install hypothesis
