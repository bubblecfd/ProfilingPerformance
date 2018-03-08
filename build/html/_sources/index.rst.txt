.. Lesson Plan documentation master file, created by
   sphinx-quickstart on Sun Jan 28 19:33:27 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=======================
Profiling & Performance
=======================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


************
Introduction
************

[1-3 paragraphs introducing topic(s)]


Learning Objectives
===================

Upon successful completion of this lesson, you will be able to:

* use timing strategies to assess code constructs.
* identify bottlenecks in Python code.
* use PyPy to run simple Python scripts to improve their performance.
* refactor Python code to use Cython for performance improvement.


New Words or Concepts
=====================

* Profiling
* timeit
* memoization
* PyPy
* Cython


Required Reading
================

* Profiling

  | https://docs.python.org/3.6/library/debug.html
  | https://docs.python.org/3.6/library/timeit.html



Optional Reading
================




*******
Content
*******


Profiling
=========

time & timeit
-------------

Unix Command line tool that times the duration of processes: time

.. code-block:: bash

    $ time -p find ~/Documents
    $ time --verbose find ~/Documents

Gnu-time installed via Homebrew on Mac OS X for more depth.

.. code-block:: bash

    $ brew install gnu-time
    $ gtime --verbose find ~/Documents


Memoization
===========

.. Resource:  https://anandology.com/python-practice-book/functional-programming.html#example-memoize

.. Resource: Screenshots of Joe's code from 2018-03-07



PyPy
====


Cython
======



****
Quiz
****



********
Activity
********



**********
Assignment
**********



******************
Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
