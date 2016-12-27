.. image:: https://travis-ci.org/ldiary/importlazy.svg?branch=master
    :target: https://travis-ci.org/ldiary/importlazy
    :alt: See Build Status on Travis CI

importlazy
------------
A rework of https://bitbucket.org/hpk42/apipkg for learning purposes. Intends to support the latest versions of Python 3 only.

How it works
------------
The test scenarios in tests\test_use_project_awesome.py demonstrates different usages of importlazy.
The author of project_awesome enables lazy loading of modules by defining namespaces to export
inside the project_awesome\__init__.py file.

The test_use_project_awesome.py file takes advantage of these lazy loading functionality by using
the exported namespaces defined in by project_awesome.