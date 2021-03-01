#!/usr/bin/env bash

if [[ "$TRAVIS_OS_NAME" == "linux" ]]; then
        wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O anaconda.sh;
        PHYNIX_PYTHON_VERSION=$TRAVIS_PYTHON_VERSION;
elif [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
        PHYNIX_PYTHON_VERSION="3.9";
        wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O anaconda.sh;
fi

bash anaconda.sh -b -p $HOME/anaconda > tmp.txt && echo "alive"
export PATH="$HOME/anaconda/bin:$PATH"
hash -r
conda config --set always_yes yes --set changeps1 no

conda info -a
