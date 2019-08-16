from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sp-games",
    version="0.0.3",
    description="CLI Utility to extract information from Giant Bomb",
    packages=find_packages(exclude=['tests*']),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "argparse",
        "PyInquirer",
        "requests",
        "clint",
    ],
    classifiers=[
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3.7",
    ],
    entry_points={
        "console_scripts": [
            "spag = spag.main:main"
        ]
    })