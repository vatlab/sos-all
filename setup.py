#!/usr/bin/env python
#
# Copyright (c) Bo Peng and the University of Texas MD Anderson Cancer Center
# Distributed under the terms of the 3-clause BSD License.

from setuptools import setup

__version__ = '0.9.9.4'

description = '''\
Computationally intensive disciplines such as computational biology often 
requires one to exploit a variety of tools implemented in different programming
languages, and to analyze large datasets on high performance computing systems.
Although scientific workflow systems are powerful in organizing and executing
large-scale data analysis processes, there are usually non-trivial learning
curve and engineering overhead in creating and maintaining such workflows,
making them unsuitable for data exploration and prototyping. To bridge the
gap between interactive analysis and workflow systems, we developed Script
of Scripts (SoS), a system with strong emphases on readability, practicality,
and reproducibility for daily computational research. For exploratory analysis
SoS provides a multi-language file format and scripting engine that centralizes
all computations, and creates dynamic report documents for publishing and
sharing. As a workflow engine, SoS provides an intuitive syntax to create
workflows in process-oriented, outcome-oriented and mixed styles, as well as
a unified interface to executing and managing tasks on a variety of computing
platforms with automatic synchronization of files between isolated systems.
In this paper we illustrate with real-world examples the use of SoS as both
interactive analysis tool and pipeline platform for all stages of methods
development and data analysis projects. In particular we demonstrate how SoS
can easily be adopted based on existing scripts and pipelines, yet resulting
in substantial improvement in terms of organization, readability and
cross-platform computation management.

Please refer to http://vatlab.github.io/SOS/ for more details on SoS.
'''

#
# This is a super package for sos with the sole purpose to install
# components of SoS with a single command.
#

setup(name = "sos-essentials",
    version = __version__,
    description = 'Essential components of Script of Scripts (SoS)',
    long_description=description,
    author = 'Bo Peng',
    url = 'https://github.com/vatlab/SOS',
    author_email = 'bpeng@mdanderson.org',
    maintainer = 'Bo Peng',
    maintainer_email = 'bpeng@mdanderson.org',
    license = '3-clause BSD',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: BSD',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        ],
    install_requires=[
        'sos>=0.9.11.2',
        'sos-notebook>=0.9.11.3',
        'sos-pbs>=0.9.10.4',
        'sos-bash>=0.9.10.1',
        'sos-python>=0.9.10.1',
        'sos-r>=0.9.10.3',
      ]
)
