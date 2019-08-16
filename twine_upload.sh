#!/bin/bash

version=$(python ./setup.py --version)
bumpversion --current-version $version patch ./setup.py

git commit -am "bumping versions"

pip uninstall dist/* -y
rm -fr dist/
python setup.py bdist_wheel

python -m twine upload dist/* --verbose