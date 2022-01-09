import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="farlimit",
    version="0.1.1",
    author="Omid Karimzade",
    author_email="omidekz@gmail.com",
    description="FastAPIRateLimit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omidekz/farlimit",
    project_urls={
        "Bug Tracker": "https://github.com/omidekz/farlimit/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
