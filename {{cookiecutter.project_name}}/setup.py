# Standard library imports
from os import path

# Third party imports
from setuptools import (  # Always prefer setuptools over distutils
    find_packages,
    setup,
)

# Local application imports
from {{cookiecutter.project_name}} import __version__

here = path.abspath(path.dirname(__file__))

setup(
    name="{{cookiecutter.project_name}}",
    version=__version__,
    description="{{cookiecutter.short_description}}",
    long_description="",
    url="{{cookiecutter.url}}",
    # Author details
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author_email}}",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    test_suite="tests",
    install_requires=[],
    entry_points={},
)
