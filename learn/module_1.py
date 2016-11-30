# -*- coding: utf-8 -*-
"""
module_1.py

In the last module, I encouraged you to look around and explore the files. In
this excercise, you'll get to modify the module and try your own tests.

To make the process easier, I've put all of the code and unittests into the
same file, module_1.py, so that you can see the test and the code on the same
page. This is not the normal way to write your tests. Normally, you would
separate your tests from your code, like I did with module_0 and test_module_0.
Unfortunately, the weird setup I use here does not work from the command line.
When you try to run `python -m unittest` from the command line, unittest only
looks for tests in modules with names that start with 'test_', so unittest
won't be able to find the tests in this module. So, you should run the tests
for this exercise by running the module in the interpreter.

Your first job is to fix the function fix_me() so that it can pass the test.

Your second job is to write a test that check whether fix_me() returns
a string. I put a comment in the place where you should put your test.

When you are done, save it all, commit it, and upload it to Github!
"""
import unittest


def add_five(value):
    """
    Returns a value plus five.

    Args:
    -----
        value (int): an integer or float.

    Returns:
    --------
        output: an integer or float that is five larger than the input value.
    """

    # For fun, alter this next line to add 6, and watch the tests fail.
    output = value + 5

    return output


def fix_me(name):
    """Returns a string that says hello.

    Args:
    -----
        name (str): the name of a person.

    Returns:
    --------
        output: a string that says, 'hello, <name>!'
    """
    output = 'Fix me ' + str(name) + '!'
    return output


class TestModule1(unittest.TestCase):

    def test_001_something_stupid(self):
        """Check: does 5 equal 5?
        """
        expected = 5
        actual = 5
        self.assertEqual(actual, expected)

    def test_6_add_five_returns_11(self):
        """Check that add_five(6) returns 11.
        """
        expected = 11
        actual = add_five(6)
        self.assertEqual(actual, expected, msg='Returned {}'.format(actual))

    def test_whether_add_five_returns_an_integer(self):
        """Check that add_five() returns an integer.
        """
        some_int = 5
        actual = add_five(some_int)
        self.assertIsInstance(actual, int, msg='Returned {0}, which'
                              ' is an instance of {1}'.format(actual,
                                                              type(actual)))

    def test_fix_me_Marty_returns_hello_Marty(self):
        """Check that fix_me('Marty') returns 'Hello, Marty'
        """
        expected = 'Hello, Marty!'
        actual = fix_me('Marty')
        self.assertEqual(actual, expected)

    # Write a test that checks that fix_me returns a string.
    # def put_the_test_here!


if __name__ == '__main__':

    import unittest

    # Note that I've altered how I run unittest for this module. This will run
    # all of the tests in this module, but none of the tests in any of the
    # other modules.
    unittest.main(module='module_1', verbosity=2)
