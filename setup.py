# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os import path
from locust_runner.version import __version__


# URL to the repository on Github.
REPO_URL = 'https://github.com/hanpeter/locust-runner'

# Github will generate a tarball as long as you tag your releases, so don't
# forget to tag!
DOWNLOAD_URL = ''.join((REPO_URL, '/tarball/release/', __version__))

try:
    with open(path.join(path.dirname(__file__), 'README.md')) as f:
        long_description = f.read()
except Exception:
    # XXX: Intentional pokemon catch to prevent this read from breaking setup.py
    long_description = None

setup(
    name='locust-runner',
    version=__version__,
    author='Peter Han',
    author_email='git@peterhan.ca',
    description='Runner for Locust.io load testing tool',
    long_description=long_description,
    url=REPO_URL,
    download_url=DOWNLOAD_URL,
    url='https://github.com/hanpeter/locust-runner',
    packages=find_packages(exclude=['tests']),
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Testing',
    ],
    install_requires=[
        'locustio'
    ],
    python_requires='~=3.8',
    # Make sure the license file is packaged up too
    include_package_data=True,
)
