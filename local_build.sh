#!/bin/bash
pip uninstall dist/* -y
rm -fr dist/
python setup.py bdist_wheel
pip install dist/*