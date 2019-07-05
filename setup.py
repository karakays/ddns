#!/usr/bin/python
# -*- coding: utf-8
from setuptools import setup, find_packages

pkg_vars = {}

setup(
    name='ddns',
    author='Selçuk Karakayalı',
    author_email='skarakayali@gmail.com',
    url='https://github.com/karakays/ddns',
    description='Dynamically update DNS records of the enclosing environment',
    install_requires=['requests>=2.21.0'],
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.6',
    keywords=['dns', 'ddns', 'ip-address'],
    long_description=open('README.rst').read(),
    entry_points={
        'console_scripts': [ 'ddns = cfddns.__main__:main' ]
    },
    classifiers=[ "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License"
    ]
)
