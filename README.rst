===========
Change Case
===========

.. image:: https://requires.io/github/SkiftCreative/python-change-case/requirements.svg?branch=master
    :target: https://requires.io/github/SkiftCreative/python-change-case/requirements/?branch=master
    :alt: Requirements Status

What is this for?
=================

As simple as it is, I was surprised that there was no libraries in pypi that purely handled changing of casing from one
style to another. Sure simple .title() is easy. But this library allows you to easily take any casing type and go from
one to the other.

Types supported

* `camelCase`_ (lower camel case)
* `PascalCase`_ (upper camel case)
* `WikiCase`_
* `snake_case`_
* param-case (for url's)

.. _camelCase: http://en.wikipedia.org/wiki/CamelCase
.. _PascalCase: http://c2.com/cgi/wiki?PascalCase
.. _WikiCase: http://en.wikipedia.org/wiki/Wikipedia:Naming_conventions_%28capitalization%29
.. _snake_case: http://en.wikipedia.org/wiki/Snake_case

Python Version Support
======================

I only plan on supporting python 3, as that is what I primarily use. It works on python 3.3+. I have not tested on
older versions.

Usage
=====

Change Case is easy to use. You simply pass a string to get the new value. Example, if you want to convert a
``camelCasedString`` to a ``snake_cased_string``, you would simply run::

    old = "camelCasedString"
    new = ChangeCase.camel_to_snake(old)
    print(new)
    # camel_cased_string

To see what is possibly, simply view the main file. You can run tests by running the file directly. You can also look at
the tests to see the usage and response of each one.

Tests
=====

You can easily run tests one of two ways. You can run the change_case.py file manually with python, and it will run the
test.::

    python3 change_case.py

or you can do this as well::

    In [1]: from change_case import ChangeCase

    In [2]: ChangeCase.run_tests()
    camel_to_upper_camel tests passed.
    camel_to_pascal tests passed.
    camel_to_wiki tests passed.
    camel_to_snake tests passed.
    camel_to_param tests passed.
    pascal_to_camel tests passed.
    pascal_to_upper_camel tests passed.
    pascal_to_wiki tests passed.
    pascal_to_snake tests passed.
    pascal_to_param tests passed.
    wiki_to_camel tests passed.
    wiki_to_upper_camel tests passed.
    wiki_to_pascal tests passed.
    wiki_to_snake tests passed.
    wiki_to_param tests passed.
    snake_to_camel tests passed.
    snake_to_upper_camel tests passed.
    snake_to_pascal tests passed.
    snake_to_wiki tests passed.
    snake_to_param tests passed.
    param_to_camel tests passed.
    param_to_upper_camel tests passed.
    param_to_pascal tests passed.
    param_to_wiki tests passed.
    param_to_snake tests passed.

Contributing and Bugs
=====================

You can file any issues you find here:

https://github.com/SkiftCreative/python-change-case/issues

It is fairly simple to add new case types. Simply add the methods to ``ChangeCase`` and add the tests to
``ChangeCase.run_tests()``

=======
LICENSE
=======

The MIT License (MIT)

Copyright (c) [2015] [Shawn McElroy]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.