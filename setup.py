#!/usr/bin/python
# -*- coding: utf-8
from setuptools import setup, find_packages

pkg_vars = {}

#with open("whoisit/_version.py") as fp:
#    exec(fp.read(), pkg_vars)

setup(
    name='cfddns',
    #version=pkg_vars['__version__'],
    author='Selçuk Karakayalı',
    author_email='skarakayali@gmail.com',
    url='https://github.com/karakays/cf-ddns',
    #description='Find out who has unfollowed you on Twitter',
    install_requires=['requests>=2.21.0'],
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.6',
    #keywords=['twitter', 'followers', 'authentication'],
    #long_description=open('README.rst').read(),
    entry_points={
        'console_scripts': [ 'ddns = cfddns.__main__:main' ]
    },
    classifiers=[ "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License"
    ]
)
