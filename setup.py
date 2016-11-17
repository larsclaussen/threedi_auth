#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.1.0'

if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='threedi_auth',
    version=version,
    description="""Gebruiker authenticatie en autorisatie vonden tot nu toe beide plaats in de SSO server. Aangezien dit leidde tot beheerproblemen is besloten om de SSO server alleen nog maar authenticatie te laten doen. De verschillende applicaties zoals Lizard en 3Di zorgen dan zelf voor implementatie van de autorisatie kant, is het idee. In dit plan wordt de uitwerking hiervan voorgesteld.""",
    long_description=readme + '\n\n' + history,
    author='larsclaussen',
    author_email='claussen.lars@gmail.com',
    url='https://github.com/larsclaussen/threedi_auth',
    packages=[
        'threedi_auth',
    ],
    include_package_data=True,
    install_requires=["django-model-utils>=2.0",],
    zip_safe=False,
    keywords='threedi_auth',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
