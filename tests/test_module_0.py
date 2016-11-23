"""
test_module_0.py

A suite of tests for module_0.py
These are based on unittest. You can run them from the command line
by typing:  `python setup.py test
"""
import unittest

import module_0 as m0


class TestModule0(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        print("test000")
        assert True

    def test_first_returns_true(self):
        expected = True
        actual = m0.hello_world()
        self.assertEqual(expected, actual, msg="hello_world() did not return True.")



