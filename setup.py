#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

HERE = os.path.dirname(__file__)
exec(open(os.path.join(HERE, "ctor", "version.py")).read())

setup(name = "construct3",
    version = version_string, #@UndefinedVariable
    description = "Ctor: the Modular Build System",
    author = "Tomer Filiba",
    author_email = "tomerfiliba@gmail.com",
    license = "MIT",
    url = "",
    packages = ["ctor"],
    platforms = ["POSIX", "Windows"],
    provides = ["ctor"],
    #scripts = [
    #    os.path.join("bin", "ctor"),
    #],
    entry_points = dict(
        console_scripts = ["ctor = ctor.main"]
    ),
    requires = ["six", "plumbum"],
    install_requires = ["six", "plumbum"],
    keywords = "make, build system",
    long_description = open(os.path.join(HERE, "README.rst"), "r").read(),
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
    ],
)