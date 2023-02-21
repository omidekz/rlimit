#!/usr/bin/env python

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rlimit",
    python_requires=">=3.6",
    version="1.4",
    url="https://github.com/omidekz/rlimit",
    license="GPLv3",
    description="Python Rate Limiter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="omidekz",
    keywords=['rate limit', 'python rate limit', 'rate limiter', 'python rate limiter'],
    author_email="omidekz@gmail.com",
    packages=setuptools.find_packages(exclude=['tests']),
    project_urls={
        "Bug Tracker": "https://github.com/omidekz/rlimit/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
