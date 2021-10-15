#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fp:
    install_requires = fp.read().splitlines()

setup(
    name="kftools", 
    version="0.0",
    author="KCNI Griffiths Lab et al.",
    author_email="",
    description="tools for working with kernel flow fnirs/eeg data",
    keywords="fNIRS, EEG, Neuroimaging, SNIRF, Diffuse Optical Tomography",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = install_requires,
    url='https://github.com/griffithslab/kernel-flow-tools',
    license="BSD (3-clause)",
    entry_points={},#{"console_scripts": ["eegnb=eegnb.cli.__main__:main"]},
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
