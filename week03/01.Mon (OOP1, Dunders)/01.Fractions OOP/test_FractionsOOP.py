import unittest
from FractionsOOP import IntegerFraction

class test_IntegerFraction(unittest.TestCase):
	
	def test_init_dunder_with_bad_type(self):
		e = None

		try:
			res = IntegerFraction("5", "6")
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Non-integer type error.")

	def test_init_dunder_with_zero_denominator(self):
		e = None

		try:
			res = IntegerFraction(1, 0)
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Zero division!")

	def test_init_dunder(self):
		e = None

		try:
			res = IntegerFraction(1, 2)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(res.__dict__["numerator"], 1)
		self.assertEqual(res.__dict__["denominator"], 2)
	
	def test_str_dunder(self):
		e = None

		try:
			res = IntegerFraction(1, 2)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(f"{res}", "1/2")

	def test_eq_dunder(self):

		self.assertTrue(IntegerFraction(100, 200) == IntegerFraction(1, 2))
		self.assertTrue(IntegerFraction  (-1, -2) == IntegerFraction(1, 2))
		self.assertFalse(IntegerFraction   (1, 2) == IntegerFraction(2, 1))
		self.assertTrue(IntegerFraction    (0, 2) == IntegerFraction(0, -5))
		self.assertTrue(IntegerFraction   (-1, 1) == IntegerFraction(1, -1))

	def test_add_dunder(self):
		e = None

		try:
			res1 = IntegerFraction(1, 2) + IntegerFraction(2, 4)
			res2 = IntegerFraction(0, 5) + IntegerFraction(1, 6)
			res3 = IntegerFraction(4, 7) + IntegerFraction(6, 14)
			res4 = IntegerFraction(-5, -9) + IntegerFraction(3, 8)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(IntegerFraction(1, 1), res1)
		self.assertEqual(IntegerFraction(1, 6), res2)
		self.assertEqual(IntegerFraction(1, 1), res3)
		self.assertEqual(IntegerFraction(67 ,72), res4)

	def test_gt_dunder(self):

		self.assertTrue(IntegerFraction(1, 2) > IntegerFraction(0, 2))
		self.assertFalse(IntegerFraction(0, 2) > IntegerFraction(0, 4))
		self.assertTrue(IntegerFraction(1, 2) > IntegerFraction(-2, 1))
		self.assertFalse(IntegerFraction(-2, 1) > IntegerFraction(2, -1))

	def test_simplified(self):
		e = None

		try:
			res1 = IntegerFraction(5,10).simplified()
			res2 = IntegerFraction(1, 2).simplified()
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(IntegerFraction(1,2), res1)
		self.assertEqual(IntegerFraction(1,2), res2)

	def test_simplified_with_a_negative_number(self):
		e = None

		try:
			res = IntegerFraction(-5,10).simplified()
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(IntegerFraction(-1, 2), res)
		

if __name__ == '__main__':
	unittest.main()