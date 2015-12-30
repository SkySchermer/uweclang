
This is a summary of the steps necessary to install and use our application. The goal is to perform each step on each possible setup and make sure it works as expected. There are the following setups:

UWEC - Software is hosted & running on UWEC servers.
Windows - Software is hosted locally on a windows PC.
Mac - Software is hosted locally on a Mac.

We'll use these handy marks to label what we can do:
✗ - Don't know how to do it.
○ - Know how to do it.

This table should also provide instructions for how to do anything that we know how to do.

1. Install Python
  - ✗ UWEC
  - Windows
    https://www.python.org/downloads
    Click "Download Python X.Y.Z"
  - ✗ Mac

2. Install Django
  - ✗ UWEC
    + `pip install django`
  - ✗ Windows
  - ✗ Mac
    + `pip install django`

3. Install Antlr4 Runtime
  - ✗ UWEC
    + `pip install antlr4-python2-runtime`
  - ○ Windows
    + `pip install antlr4-python2-runtime`
    + `pip install antlr4-python3-runtime`
  - ○ Mac
    + `pip install antlr4-python2-runtime`
    + `pip install antlr4-python3-runtime`

4. Install NLTK
  - ✗ UWEC
    + `pip install nltk`
  - ✗ Windows
  - ✗ Mac
    + `pip install nltk`

5. Add UWECLANG library to PYTHONPATH
  - ✗ UWEC
    + `export PYTHONPATH=.`
  - ✗ Windows
  - ✗ Mac
    + `export PYTHONPATH=.`

6. Run Server
  - ✗ UWEC
  - ✗ Windows
  - ✗ Mac
    + `cd /django/src`
    + `./manage.py syncdb`
    + `./manage.py collectstatic`
    + `./manage.py runserver`

