"""
test_module_0.py

A suite of tests for module_0.py
These are based on unittest. You can run them from the command line
by typing:  `python setup.py test
"""
import unittest

from learn import module_0 as m0


class TestModule0(unittest.TestCase):

    def test_000_something(self):
        # print("test000")
        # The following test checks that the value 'True' is true.
        # We expect this test should pass with no problems.
        # More importantly, can you find where the results of this test get
        # reported when you run the test?
        self.assertTrue(True)

    def test_first_returns_true(self):
        expected = True
        actual = m0.hello_world()
        self.assertEqual(expected, actual, msg="hello_world() didn't return "
                         "True.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
