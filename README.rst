**************
muzik-dumpster
**************

A Python 3.6 project for sorting text based music collections.
The process will sort one file or a directory of files and store
results in a file.

Usage
=====

help
$ muzik-dumpster -h

file
$ muzik-dumpster \
    --archive \
    -- type '[a media type]'
    -files /path/to/file

directory
$ muzik-dumpster \
    --archive \
    -- type 'all'
    -files /path/to/directory

Development
===========

- Start a python3 virtual environment

- Execute core.py to test changes

$ python muzikdumpster/core.py -a -f muzik-dumpster/tests/resources

- Install into virtualenv site-packages to run as an executable

$ pip install .

or

$ python setup.py sdist
$ pip install dist/muzid-dumpster-x.x.x.tar.gz
$ muzik-dumpster -a -f muzik-dumpster/tests/resources

Packaging
=========

See: http://python-packaging.readthedocs.io
