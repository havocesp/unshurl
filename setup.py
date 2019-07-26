# -*- coding: utf-8 -*-
from pathlib import Path

from setuptools import setup, find_packages

import unshurl as pkg

exclude = ['.idea*', 'build*', '{}.egg-info*'.format(pkg.__package__), 'dist*', 'venv*', 'doc*', 'lab*']

requirements = Path(__file__).resolve().with_name('requirements.txt')
readme = Path(__file__).resolve().with_name('README.md')
readme.touch(exist_ok=True)
readme.touch(exist_ok=True)
requirements = requirements.read_text()
requirements = requirements.split('\n')

classifiers = [
    'Development Status :: 5 - Production',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
]

setup(
    name=pkg.__package__,
    version=pkg.__version__,
    packages=find_packages(exclude=exclude),
    url=pkg.__site__,
    license=pkg.__license__,
    keywords=pkg.__keywords__,
    author=pkg.__author__,
    author_email=pkg.__email__,
    long_description=readme.read_text(encoding='UTF-8'),
    description=pkg.__description__,
    classifiers=classifiers,
    install_requires=requirements,
    scripts=['bin/unshurl']
)
