#!/usr/bin/env bash
echo "============================ Building docs for test ============================"
uv add sphinx sphinx-rtd-theme sphinxcontrib-apidoc sphinx-autodoc-typehints > tmp.txt && echo 'doc utils installed'
bash docs/make_docs.sh 2>&1 | tail -n 11 && \
echo "======================= Finished building docs for test ========================"
