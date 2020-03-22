import unittest
from sort_array_of_fractions import (
	sort_array_of_fractions, 
	validate_sort_array_of_fractions_arguments, 
	format_fraction, 
	is_greater_than, 
	find_max, 
	getpos_min
)

class test_validate_sort_array_of_fractions_arguments(unittest.TestCase):
	
	def test_with_bad_type(self):
		e = None

		try:
			validate_sort_array_of_fractions_arguments({})
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Bad type. Expected list of tuples.")

	def test_with_bad_fraction_type(self):
		e = None

		try:
			validate_sort_array_of_fractions_arguments([(1, 2), "stringyboi"])
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Bad fraction type. Expected tuple.")

	def test_all_fraction_members_are_integer(self):
		e = None

		try:
			validate_sort_array_of_fractions_arguments([(1, 2), (5.5, 4)])
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Non-integer fraction member.")

	def test_triple_fraction(self):
		e = None

		try:
			validate_sort_array_of_fractions_arguments([(1, 2), (3, 4, 5)])
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Fraction with more than 2 members.")

	def test_empty_fraction(self):
		e = None

		try:
			validate_sort_array_of_fractions_arguments([()])
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Empty fraction.")

class test_is_than(unittest.TestCase):

	def test_for_zero_division(self):
		e = None

		try:
			is_greater_than((1,2), (3,0))
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Zero division!")

	def test_is_greater(self):
		e = None

		leftFrac1 = (10, 1)
		rightFrac1 = (5, 1)

		leftFrac2 = (0, )
		rightFrac2 = (3, 3)

		leftFrac3 = (-10, )
		rightFrac3 = (20, 2)

		leftFrac4 = (7, 14)
		rightFrac4 = (14, 28)

		try:
			result1 = is_greater_than(leftFrac1, rightFrac1)
			result2 = is_greater_than(leftFrac2, rightFrac2)
			result3 = is_greater_than(leftFrac3, rightFrac3)
			result4 = is_greater_than(leftFrac4, rightFrac4)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertTrue(result1)
		self.assertFalse(result2)
		self.assertFalse(result3)
		self.assertFalse(result4)

class test_getpos_min(unittest.TestCase):
	
	def test_with_fractions(self):
		e = None

		array = [(0, 100), (2, 20), (1, 1), (40, 1)]
		expected = 0

		try:
			result = getpos_min(array)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(expected, result)

class test_find_max(unittest.TestCase):
	pass

class test_sort_array_of_fractios(unittest.TestCase):
	
	def test_with_empty_list(self):
		e = None
	
		try:
			result = sort_array_of_fractions([])
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual([], result)

	def test_with_sorted_list(self):
		e = None

		array1 = [(0, 100), (2, 20), (1, 1), (40, 1)]
		rule1 = True

		array2 = [(-10, 1), (-1, 1), (-1, 10), (0, 100)]
		rule2 = True

		array3 = [(-100, 10), (0,), (10, 5),  (5,), (50, 5)]
		rule3 = True

		array4 = [(10,), (90, 90), (-14, 7)]
		rule4 = False

		try:
			result1 = sort_array_of_fractions(array1, rule1)
			result2 = sort_array_of_fractions(array2, rule2)
			result3 = sort_array_of_fractions(array3, rule3)
			result4 = sort_array_of_fractions(array4, rule4)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(array1, result1)
		self.assertEqual(array2, result2)
		self.assertEqual(array3, result3)
		self.assertEqual(array4, result4)

	def test_with_backwards_sorted_list(self):
		e = None

		array = [(40, 1), (1, 1), (2, 20), (0, 100)]
		rule = True

		expected = [(0, 100), (2, 20), (1, 1), (40, 1)]

		try:
			result = sort_array_of_fractions(array, rule)

		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(expected, result)

	def test_with_balanced_list(self):
		e = None

		array1 = [(1,), (27, 277), (88, 90), (6, -90)]
		rule1 = False

		array2 = [(1,), (-2,), (90, 88), (-3000, -5)]
		rule2 = True

		expected1 = [(1,), (88, 90), (27, 277), (6, -90)]
		expected2 = [(-2,), (1,), (90, 88), (-3000, -5)]

		try:
			result1 = sort_array_of_fractions(array1, rule1)

		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(expected1, result1)

if __name__ == '__main__':
	unittest.main()