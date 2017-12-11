#!/usr/bin/env bash

#- coverage run -m unittest discover
- coverage run  --branch -m unittest discover
- coverage report yamlloader/*.py
