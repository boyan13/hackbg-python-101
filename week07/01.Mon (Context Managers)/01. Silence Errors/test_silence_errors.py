import unittest
from silence_errors import silence_exception, func_silence_exception


class Test_silence_exception(unittest.TestCase):

    def test_silence_an_exception(self):
        e = None

        try:
            with silence_exception(ValueError):
                raise ValueError("Test")
        except Exception as exc:
            e = exc

        self.assertIsNone(e)

    def test_dont_silence_side_exceptions(self):
        e = None

        try:
            with silence_exception(ValueError):
                raise TypeError("Test")
        except Exception as exc:
            e = exc

        self.assertIsNotNone(e)
        self.assertEqual(str(e), "Test")

    def test_silence_an_exception_if_message_is_same(self):
        e = None

        try:
            with silence_exception(ValueError, "Test"):
                raise ValueError("Test")
        except Exception as exc:
            e = exc

        self.assertIsNone(e)

    def test_dont_silence_an_exception_with_different_message(self):
        e = None

        try:
            with silence_exception(ValueError, "Test"):
                raise TypeError("Testing")
        except Exception as exc:
            e = exc

        self.assertIsNotNone(e)
        self.assertEqual(str(e), "Testing")

    def test_passing_non_exception_type_raises_exception(self):
        e1, e2, e3 = None, None, None

        try:
            with silence_exception("BOBODDY"):
                pass
        except Exception as exc:
            e1 = exc

        try:
            with silence_exception(list):
                pass
        except Exception as exc:
            e2 = exc

        try:
            with silence_exception(ValueError, 12):
                pass
        except Exception as exc:
            e3 = exc

        self.assertIsNotNone(e1)
        self.assertIsNotNone(e2)
        self.assertIsNotNone(e3)
        self.assertEqual(str(e1), "Expected an exception type.")
        self.assertEqual(str(e2), "Expected an exception type.")
        self.assertEqual(str(e3), "Expected string.")


if __name__ == '__main__':
    unittest.main()