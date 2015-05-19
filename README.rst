===========
Change Case
===========

What is this for?
=================

As simple as it is, I was surprised that there was no libraries in pypi that purely handled chaning of casing from one
style to another. Sure siple .title() is easy. But this library allows you to easily take any casing type and go from
one to the other.

Types supported
* camelCase (lower camel case)
* PascalCase (upper camel case)
* WikiCase
* snake_case
* param-case (for url's)

Python Version Support
======================

I only plan on supporting python 3, as that is what I primarily use. It works on python 3.3+. I have not tested on
older versions.

Usage
=====

Change Case is easy to use. You simply pass a string to get the new value. Example, if you want to convert a
``camelCasedString`` to a ``snake_cased_string``, you would simply run

    old = "camelCasedString"
    new = ChangeCase.camel_to_snake(old)
    print(new)
    # camel_cased_string

To see what is possibly, simply view the main file. You can run tests by running the file directly. You can also look at
the tests to see the usage and response of each one.

Contributing and Bugs
=====================

You can file any issues you find here:

https://github.com/SkiftCreative/python-change-case/issues

It is easy to add a new casing type. simply add the new functions, and tests. To submit a patch I am open to pull
requests as well.

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