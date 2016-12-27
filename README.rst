.. image:: https://travis-ci.org/ldiary/importlazy.svg?branch=master
    :target: https://travis-ci.org/ldiary/importlazy
    :alt: See Build Status on Travis CI
.. image:: https://img.shields.io/coveralls/ldiary/importlazy/master.svg
   :target: https://coveralls.io/r/ldiary/importlazy
.. image:: https://ci.appveyor.com/api/projects/status/github/ldiary/importlazy?branch=master
    :target: https://ci.appveyor.com/project/ldiary/importlazy/branch/master
    :alt: See Build Status on AppVeyor

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