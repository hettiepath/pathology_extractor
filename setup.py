#! /usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

DESCRIPTION = """
    a Python repository implementing information extraction from
    Breast cancer pathology report and progress notes
    """

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__ == "__main__":
    setup(
        name = "pathology extractors",
        version = "0.1.dev",
        author = "Titipat Achakulvisut",
        author_email = "titipat.a@u.northwestern.edu",
        description = DESCRIPTION,
        license = "MIT",
        keywords = "Pathology report, progress note, breast cancer",
        url = "https://github.com/titipata/pathology_extractor",
        long_description=read('README.md'),
        packages=['extractors'],
    )
