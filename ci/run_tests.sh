#!/usr/bin/env bash

coverage run  --source=. --branch -m unittest discover && coverage report src/yamlloader/*.py
coverage report
