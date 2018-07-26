#!/usr/bin/env bash
# install test environment
pip install coverage > tmp.txt && echo "alive";
#conda install -y coverage > tmp.txt && echo "alive";
pip install coveralls > tmp.txt && echo "alive";
pip install hypothesis
