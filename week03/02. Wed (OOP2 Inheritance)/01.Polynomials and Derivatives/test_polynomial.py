import unittest
from polynomial import Polynomial, PolyTerm

class test_polyTerm(unittest.TestCase):

	def test_parse(self):
		e = None
		input1 = "2x^3 + 3x + 1"
		input2 = "x^4+10*x^3"
		input3 = "x + X"
		expected1 = [(2, 'x', 3), (3, 'x', 1), 1]
		expected2 = [(1, 'x', 4), (10, 'x', 3)]
		expected3 = [(1, 'x', 1), (1, 'x', 1)]

		try:
			res1 = PolyTerm.parse(input1)
			res2 = PolyTerm.parse(input2)
			res3 = PolyTerm.parse(input3)
		except Exception as exc:
			e = exc 

		self.assertIsNone(e)
		self.assertEqual(expected1, res1)
		self.assertEqual(expected2, res2)
		self.assertEqual(expected3, res3)

	def test_parse_with_multiple_x(self):
		e = None

		bad = "2x^3*x + 3x + 1"

		try:
			PolyTerm.parse(bad)
		except Exception as exc:
			e = exc 

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Multiple x in term.")

	def test_parse_with_bad_term_type(self):
		e = None

		bad = "x^4+10*x^3 + stringiboi"

		try:
			PolyTerm.parse(bad)
		except Exception as exc:
			e = exc 

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Cannot parse.")

	def test_parse_with_non_integer_coefficient(self):
		e = None
		bad = "8x^5 + 5^"

		try:
			PolyTerm.parse(bad)
		except Exception as exc:
			e = exc 

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Non-integer coefficient.")

	def test_init_dunder(self):
		e = None

		try:
			pterm1 = PolyTerm((3,'x',2))
			pterm2 = PolyTerm(123)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(3, pterm1.__dict__["coefficient"])
		self.assertEqual('x', pterm1.__dict__["x"])
		self.assertEqual(2, pterm1.__dict__["power"])
		self.assertEqual(123, pterm2.__dict__["coefficient"])
		self.assertEqual('x', pterm2.__dict__["x"])
		self.assertEqual(0, pterm2.__dict__["power"])

class test_polynomial(unittest.TestCase):

	def test_init_dunder(self):
		e = None
		term1 = PolyTerm( (4,'x',2) )
		term2 = PolyTerm( (6,'x',3) )
		term3 = PolyTerm( 8 )

		try:
			p = Polynomial([term1, term2, term3])
		except Exception as exc:
			e = exc 

		self.assertIsNone(e)
		self.assertEqual(p.__dict__["terms"][0], term1)
		self.assertEqual(p.__dict__["terms"][1], term2)
		self.assertEqual(p.__dict__["terms"][2], term3)

	def test_str_dunder(self):
		e = None
		term1 = PolyTerm( (4,'x',2) )
		term2 = PolyTerm( (6,'x',3) )
		term3 = PolyTerm( 8 )
		p = Polynomial([term1, term2, term3])
		expected = "4x^2 + 6x^3 + 8"

		try:
			res = f"{p}"
		except Exception as exc:
			e = exc 

		self.assertIsNone(e)
		self.assertEqual(expected, res)

	def test_derivative(self):
		e = None
		term1 = PolyTerm( (1,'x',4) )
		term2 = PolyTerm( (10,'x',3) )   
		p = Polynomial([term1, term2])
		expectedTerm1 = PolyTerm( (4,'x',3) )
		expectedTerm2 = PolyTerm( (30,'x',2) )
		expected = Polynomial([expectedTerm1, expectedTerm2])

		try:
			res = p.derivative()
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(f"{expected}", f"{res}")

if __name__ == '__main__':
	unittest.main()