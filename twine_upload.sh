#!/bin/bash

version=$(python ./setup.py --version)
bumpversion --current-version $version patch ./setup.py

python -m twine upload dist/* --verbose