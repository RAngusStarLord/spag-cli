#!/bin/bash

version=$(python ./setup.py --version)
bumpversion --current-version $version patch ./setup.py

git commit -am "bumping versions"

#python -m twine upload dist/* --verbose