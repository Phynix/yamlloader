#!/usr/bin/env bash

uv run coverage run --source=. --branch -m unittest discover && uv run coverage report src/yamlloader/*.py
uv run coverage report
