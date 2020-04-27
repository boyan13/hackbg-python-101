import unittest
import os
from time import time
from performance import performance


@performance("test.txt")
def tester_func(*args, **kwargs):
    return 9


class Test_performance(unittest.TestCase):

    def setUp(self):
        with open("test.txt", 'w'):
            pass

    def test_return_is_preserved(self):
        e = None

        try:
            res = tester_func()
        except Exception as exc:
            e = exc

        self.assertIsNone(e)
        self.assertEqual(res, 9)

    def test_timing(self):
        e = None
        expected = "tester_func was called and took 0 seconds to complete\n"

        try:
            tester_func()
        except Exception as exc:
            e = exc

        filetext = str()
        with open("test.txt", 'r') as f:
            filetext = f.read()

        self.assertIsNone(e)
        self.assertEqual(filetext, expected)

    def tearDown(self):
        if os.path.isfile("test.txt"):
            os.remove("test.txt")


if __name__ == '__main__':
    unittest.main()
