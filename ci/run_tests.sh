#!/usr/bin/env bash

coverage run  --source=. --branch -m unittest discover && coverage report yamlloader/*.py
coverage report
