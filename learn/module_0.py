# -*- coding: utf-8 -*-
"""
module_0.py

Introduction to modules
=======================

This module serves as an example for how everything should
look in a typical module. You can copy this module and use it as a template.

To run the tests, open a command prompt in the root directory (the one that
contains setup.py: 'learn_python') and type python -m unittest -v. This will 
find and run all of the tests in this project. Alternatively, 
type `python setup.py tests` to do the same thing, but using the setup.py file
that I've created for this package.

To only run the tests for this module (this is not the typical way of doing
things, but it might be more convenient under these circumstances), simply
run this module and the script at the bottom will automatically run the tests
for this module.  Alternatively, you can run the tests for this module directly
from the command line::
    python -m unittest tests/test_module_0.py

**Other interesting things to try:**

1. Running a module

This module defines a function `hello_world()`  **AND** it runs a script. If
you run this module, the python interpreter will get to the line that defines
the hello_world function and save the function to memory. To execute the
function, you will need to call it like this::

    `hello_world()`

If you want to try this out, then either alter the module by adding
`hello_world()` after it gets defined, or you can type `hello_world()` into
the interpreter some time after you have run the module.

2. Exploring the code with dir() and help()

One important feature of Python is that it allows you to explore all of the
code in memory using the directory command: `dir()` and the help
command: `help()`

Try this out by first typing in `dir()`. Everything that gets listed can also
explored using help().  For example::

    >>> dir()
    ... # a long list is returned; 'quit' is in this list.

    >>> dir(quit)
    ... # another long list is returned; 'rewrite' is in this list.

    >>> dir(quit.rewrite)
    ... # and so on...

Try typing `help(quit.rewrite)`
or `help(hello_world)`

If you are using Spyder, try typing `Cntrl-I` when your cursor is next to
hello_world. This will open up a formatted version of the docstring in a
special help window. If this window isn't open at first, you can open it by
following these commands on the menu: View > Panes > Help  **or**
`Cntrl-Shift-H`

3. Using Import to read a module

The import command allows you to read in a module and put it into the
namespace. Try to import this file like this::
    >>>import module_0

Next, use the dir() and help() commands to learn about the module.:
    >>>help(module_0)
    ... # This returns the docstring that you are reading!
    >>>help(module_0.hello_world)
    ... # This returns the docstring for hello_world, which we saw earlier.

What is next?
=============

Open up the file module_1.py and read its docstring. Or try importing it and

"""


def hello_world():
    """
    You are reading the docstring for hello_world(). You can access this
    text by typing help(hello_world) in the python interpreter.

    Print 'Hello World' to the screen.

    Args:
    ----
        none

    Returns:
    -------
        True
    """
    print("Hello World!")
    return True


if __name__ == '__main__':

    print('Inside of module_0.main()')
    import unittest

    # run the test module that corresponds to this module.
    unittest.main("tests.test_module_0", verbosity=2)
