#!/usr/bin/env bash
conda create -q --name=yamlloader_env python=$PHYNIX_PYTHON_VERSION > tmp.txt && echo "alive"
source activate yamlloader_env


