import unittest
from add_fractions import add_fractions, validate_add_fractions_arguments, lcm


class test_lcm(unittest.TestCase):

	def test_with_non_integer(self):
		e = None

		try:
			lcm(6.6, 4)
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Non-integer type.")

class test_validate_add_fractions_arguments(unittest.TestCase):

	def test_with_bad_type(self):
		e = None

		try:
			validate_add_fractions_arguments({})
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Argument must be a list of 2 tuples.")

	def test_with_list_of_non_tuples(self):
		e = None

		try:
			validate_add_fractions_arguments( [ (1,2), [3,5] ] )
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Fractions must be represented by tuples.")

	def test_with_triple_fraction(self):
		e = None

		try:
			validate_add_fractions_arguments( [ (2,3), (4,10,6) ] )
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Too many members in fraction.")

	def test_with_bad_fraction_member_type(self):
		e = None

		try:
			validate_add_fractions_arguments( [ (4,6), (5,4.4) ] )
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Non-integer fraction member.")

class test_add_fractions(unittest.TestCase):

	def test_with_zero_denominator(self):
		e = None
		li = [(1,2), (4,4), (6,0)]

		try:
			add_fractions(li)
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Zero division!")

	def test_with_empty_list(self):
		e = None
		emptyList = []
		expected = (0,)

		try:
			result = add_fractions(emptyList)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(expected, result)

	def test_with_zero_numerator(self):
		e = None
		li = [(1,2), (0,4), (2,8)]
		expected = (6,8)
		
		try:
			result = add_fractions(li)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(expected, result)

	def test_with_negative_numbers(self):
		e = None
		fractions1 = [(1, -2), (-10, 4), (-2, -8)]
		fractions2 = [(-3, 7), (-4, -15), (8, -2)]
		fractions3 = [(0, -3), (9, 4), (-7, -6), (2, 2)]

		expected1 = (-22, 8)
		expected2 = (-874, 210)
		expected3 = (53, 12)

		try:
			result1 = add_fractions(fractions1)
			result2 = add_fractions(fractions2)
			result3 = add_fractions(fractions3)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(expected1, result1)
		self.assertEqual(expected2, result2)
		self.assertEqual(expected3, result3)

	def test_with_fractions_missing_denominator(self):
		e = None
		fractions = [(4,7), (2,)]
		expected = (18,7)
		
		try:
			result = add_fractions(fractions)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(expected, result)

	def test_with_one_fraction(self):
		e = None
		fractions1 = [(1,2)]
		fractions2 = [(0,)]
		fractions3 = [(8,)]

		expected1 = (1,2)
		expected2 = (0,)
		expected3 = (8,1)

		
		try:
			result1 = add_fractions(fractions1)
			result2 = add_fractions(fractions2)
			result3 = add_fractions(fractions3)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(expected1, result1)
		self.assertEqual(expected2, result2)
		self.assertEqual(expected3, result3)

if __name__ == '__main__':
	unittest.main()