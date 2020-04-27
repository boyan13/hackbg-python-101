import unittest
from accepts_decorator import accepts


@accepts(int, str, type)
def tester_func(*args):
    pass


class Test_accepts(unittest.TestCase):

    def test_with_matching_types(self):
        e = None

        try:
            tester_func(123, "testing", float)
        except Exception as exc:
            e = exc

        self.assertIsNone(e)

    def test_with_not_matching_types_raises_type_error(self):
        expected1 = "Argument \'456\' of \'tester_func\' is not str"
        expected2 = "Argument \'testing\' of \'tester_func\' is not int"
        expected3 = "Argument \'789\' of \'tester_func\' is not type"

        with self.assertRaises(TypeError) as cm1:
            tester_func(123, 456, str)

        with self.assertRaises(TypeError) as cm2:
            tester_func("testing", 123, int)

        with self.assertRaises(TypeError) as cm3:
            tester_func(123, "testing", 789)

        self.assertEqual(str(cm1.exception), expected1)
        self.assertEqual(str(cm2.exception), expected2)
        self.assertEqual(str(cm3.exception), expected3)

    def test_with_additional_func_args(self):
        # Since those args are not mentioned in the decorator args,
        # they can be whatever. They should never raise excepions!
        e = None

        try:
            tester_func(123, "testing", float, ValueError, "more testing", tester_func)
        except Exception as exc:
            e = exc

        self.assertIsNone(e)


if __name__ == '__main__':
    unittest.main()
