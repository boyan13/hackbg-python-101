#Polynomials and Derivatives

class PolyTerm:
	
	# rawTerm is a list of either tuples (coefficient, 'x', power of x) or int (just coefficient)
	def __init__ (self, rawTerm):
		if type(rawTerm) is not int and type(rawTerm) is not tuple:
			raise TypeError("Bad base type.")
			
		if type(rawTerm) is int:
			self.coefficient = rawTerm
			self.x = 'x'
			self.power = 0

		else:
			if len(rawTerm) != 3:
				raise ValueError("Bad argument number.")

			self.coefficient, self.x, self.power = rawTerm

			if (
			type(self.coefficient) is not int or
			(type(self.x) is not str and self.x != 'x') or
			type(self.power) is not int
			):
				raise TypeError("Bad type during unpacking.")

	# Parse string input as list of raw terms for PolyTerm initialization
	@staticmethod
	def parse(instring):

		# Split into raw string terms to be further parsed
		rawTerms = instring.strip().split("+")
		result = []

		for rawTerm in rawTerms:

			# Clear white spaces
			rawTerm = rawTerm.replace(" ", "")

			# Validate term syntax
			for i in range(len(rawTerm)):
				buf = rawTerm[i]

				if (
				not buf.isnumeric() and 
				buf != 'x' and 
				buf != 'X' and
				buf != '*' and 
				buf != '^'
				):
					raise Exception("Cannot parse.")

				if buf == 'X': 
					# Make lowercase
					left, right = rawTerm.split('X')
					rawTerm = left + 'x' + right

			# Validate only 1 x per term, if 0 then it's only a coefficient
			c = rawTerm.count('x')

			if c > 1:
				raise Exception("Multiple x in term.")
			if c == 1:
				coefficient, power = rawTerm.split('x')
			else:
				if rawTerm.isnumeric():
					result.append(int(rawTerm))
					continue
				else:
					raise TypeError("Non-integer coefficient.")

			# Determine coefficient's value
			if coefficient == "":
				coefficient = 1
			else:
				if not coefficient[-1:].isnumeric(): #check for *
					coefficient = coefficient[:-1]

				if coefficient.isnumeric():
					coefficient = int(coefficient)

			# Determine power's value
			if power == "":
				power = 1
			else:
				if not power[0].isnumeric(): #check for ^
					power = power[1:]

				if power.isnumeric():
					power = int(power)

			result.append( (coefficient, 'x', power) )

		return result


class Polynomial:

	#terms is a list of PolyTerms
	def __init__ (self, terms):
		if type(terms) is not list:
			raise TypeError("Bad type.")

		for term in terms:
			if type(term) is not PolyTerm:
				raise TypeError("Bad term type.")

		self.terms = terms

	def __str__ (self):
		out = str()

		for term in self.terms:
			if term.power == 0:
				out += str(term.coefficient)
			else:
				out += f"{term.coefficient}{term.x}^{term.power}"
			out += " + "

		return out[:-3]


	def derivative(self):
		derivative = []

		for term in self.terms:
			if term.power == 0: # x = 1 => is redund
				continue
			elif term.power == 1:
				derivedTerm = PolyTerm((term.coefficient, 'x', 0))
				derivative.append(derivedTerm)
			else:
				derivedCoefficient = term.coefficient*term.power
				derivedPower = term.power - 1
				derivedTerm = PolyTerm((derivedCoefficient, 'x', derivedPower))
				derivative.append(derivedTerm)

		return Polynomial(derivative)





