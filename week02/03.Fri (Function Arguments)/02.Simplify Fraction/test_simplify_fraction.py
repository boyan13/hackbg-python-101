import unittest
from simplify_fraction import simplify_fraction, validate_simplify_fraction_arguments, gcd

class test_validate_simplify_fraction_arguments(unittest.TestCase):

	def test_with_wrong_type(self):
		#ARRANGE
		e = None
		li = []

		#ACT
		try:
			result = validate_simplify_fraction_arguments(li)
		except Exception as exc:
			e = exc

		#ASSERT
		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Argument must be of type tuple.")

	def test_with_non_integer_numerator_and_no_denominator(self):
		#ARRANGE
		e = None
		fraction = (6.6,)

		#ACT
		try:
			result = validate_simplify_fraction_arguments(fraction)
		except Exception as exc:
			e = exc

		#ASSERT
		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Non-integer member in fraction.")

	def test_with_triple_fraction(self):
		#ARRANGE
		e = None
		fraction = (1, 2, 3)

		#ACT
		try:
			result = validate_simplify_fraction_arguments(fraction)
		except Exception as exc:
			e = exc

		#ASSERT
		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Fraction contains more than 2 members.")

	def test_with_non_integer_denominator(self):
		#ARRANGE
		e = None
		fraction = (5, 10.5)

		#ACT
		try:
			result = validate_simplify_fraction_arguments(fraction)
		except Exception as exc:
			e = exc

		#ASSERT
		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Non-integer member in fraction.")

class test_simplify_fraction(unittest.TestCase):

	def test_with_no_arguments(self):
		#ARRANGE
		e = None
		empty_tuple = tuple()

		expected = (0,)

		#ACT
		try:
			result = simplify_fraction(empty_tuple)
		except Exception as exc:
			e = exc

		#ASSERT
		self.assertIsNone(e)
		self.assertEqual(expected, result)

	def test_with_one_argument(self):
		#ARRANGE
		e = None
		fraction = (6,)

		expected = (6,)

		#ACT
		try:
			result = simplify_fraction(fraction)
		except Exception as exc:
			e = exc

		#ASSERT
		self.assertIsNone(e)
		self.assertEqual(expected, result)

	def test_with_zero_numerator(self):
		#ARRANGE
		e = None
		fraction = (0, 17)

		expected = (0,)

		#ACT
		try:
			result = simplify_fraction(fraction)
		except Exception as exc:
			e = exc

		#ASSERT
		self.assertIsNone(e)
		self.assertEqual(expected, result)

	def test_with_passed_zero_denominator(self):
		#ARRANGE
		e = None
		fraction = (17, 0)

		#ACT
		try:
			result = simplify_fraction(fraction)
		except Exception as exc:
			e = exc

		#ASSERT
		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Zero division!")

	def test_simplify_fraction(self):
		#ARRANGE
		e = None
		fraction1 = (16, -80)
		fraction2 = (-183, -669)
		fraction3 = (-500, 2005)
		fraction4 = (9000, 666)
		fraction5 = (2, 8)

		expected1 = (1,-5)
		expected2 = (-61,-223)
		expected3 = (-100, 401)
		expected4 = (500, 37)
		expected5 = (1, 4)

		#ACT
		try:
			result1 = simplify_fraction(fraction1)
			result2 = simplify_fraction(fraction2)
			result3 = simplify_fraction(fraction3)
			result4 = simplify_fraction(fraction4)
			result5 = simplify_fraction(fraction5)

		except Exception as exc:
			e = exc

		#ASSERT
		self.assertIsNone(e)
		self.assertEqual(expected1, result1)
		self.assertEqual(expected2, result2)
		self.assertEqual(expected3, result3)
		self.assertEqual(expected4, result4)
		self.assertEqual(expected5, result5)

if __name__ == '__main__':
	unittest.main()