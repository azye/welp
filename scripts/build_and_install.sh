#!/bin/bash

python3 setup.py sdist bdist_wheel

pip3 install --upgrade --force-reinstall dist/welp-0.0.3-py3-none-any.whl
