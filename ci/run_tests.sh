#!/usr/bin/env bash

#- coverage run -m unittest discover
travis_wait 30 coverage run  --branch -m unittest discover && coverage report yamlloader/*.py
