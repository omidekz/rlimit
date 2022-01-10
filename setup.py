#!/usr/bin/env python

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="farlimit",
    python_requires=">=3.6",
    version="0.1.7",
    url="https://github.com/omidekz/farlimit",
    license="GPLv3",
    description="FastAPIRateLimit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Omid Karimzade",
    author_email="omidekz@gmail.com",
    packages=setuptools.find_packages(exclude=["test*"]),
    project_urls={
        "Bug Tracker": "https://github.com/omidekz/farlimit/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
