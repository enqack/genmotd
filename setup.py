# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='genmotd',
    version='0.1.0',
    description='Generates a Message of the Day',
    long_description=readme,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approed :: BSD License',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Systems Administration'
    ],
    author='Enqack',
    author_email='enqack@gmail.com',
    url='https://github.com/enqack/genmotd',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    scripts=['bin/genmotd'],
    include_package_data=True,
    data_files=[('/etc/genmotd.d', [
        'files/00-header',
        'files/01-system-summary',
        'files/99-footer'
        ]
    )]
)
