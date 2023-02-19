#! /usr/bin/bash

from distutils.core import setup
import setuptools

VERSION = '0.2.0'
BRANCH = 'async'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def requirements():
    """Build the requirements list for this project"""
    requirements_list = []
    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())
    return requirements_list

reqs = requirements()



setup(
    name='Envy',
    version='0.2.0',
    description='Chat/war bot for init6/warnet',
    long_description=long_description,
    keywords="init6 chat bnet warrnet bot async",
    license="MIT",
    author='ensyde',
    author_email='ensyde0@gmail.com',
    url='https://github.com/ensyde/envy',
    packages=setuptools.find_packages(),
    requires=reqs,
    python_requires=">3.10",
    )
