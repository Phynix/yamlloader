#!/usr/bin/env bash
conda create -q --name=yamlloader-env python=$PHYNIX_PYTHON_VERSION > tmp.txt && echo "alive"
source activate yamlloader-env


