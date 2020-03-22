#Fractions OOP
from math import gcd

class IntegerFraction:
	
	#DUNDERS
	def __init__ (self, a, b):
		if type(a) is not int or type(b) is not int:
			raise Exception("Non-integer type error.")

		if b == 0:
			raise Exception("Zero division!")

		self.numerator = a
		self.denominator = b

	def __str__ (self):
		return f"{self.numerator}/{self.denominator}"

	def __add__ (self, other):
		sf = self.simplified()
		of = other.simplified()

		sfn = sf.__dict__["numerator"]
		sfd = sf.__dict__["denominator"]
		ofn = of.__dict__["numerator"]
		ofd = of.__dict__["denominator"] 

		if sfd == ofd:
			return IntegerFraction(sfn + ofn, sfd).simplified()
		else:
			#least common multiple algorithm
			lcm = sfd * ofd // gcd(sfd, ofd)

			buf = lcm // sfd
			sfd *= buf
			sfn *= buf

			buf = lcm // ofd
			ofd *= buf
			ofn *= buf

			return IntegerFraction(sfn + ofn, sfd).simplified()

	def __gt__ (self, other):
		sf = self.simplified()
		of = other.simplified()

		sfn = sf.__dict__["numerator"]
		sfd = sf.__dict__["denominator"]
		ofn = of.__dict__["numerator"]
		ofd = of.__dict__["denominator"] 

		if sfd != ofd:
			#least common multiple algorithm
			lcm = sfd * ofd // gcd(sfd, ofd)

			buf = lcm // sfd
			sfd *= buf
			sfn *= buf

			buf = lcm // ofd
			ofd *= buf
			ofn *= buf

		return sfn > ofn

	def __eq__ (self, other):
		sf = self.simplified()
		of = other.simplified()

		sfn = sf.__dict__["numerator"]
		sfd = sf.__dict__["denominator"]
		ofn = of.__dict__["numerator"]
		ofd = of.__dict__["denominator"] 

		if sfd < 0:
			sfn *= -1
			sfd *= -1

		if ofd < 0:
			ofn *= -1
			ofd *= -1

		return sfn == ofn and sfd == ofd

	#PUBLIC METHODS

	def simplified(self):
		numerator = self.numerator
		denominator = self.denominator

		buf = gcd(numerator, denominator)

		while (buf != 1):
			numerator //= buf
			denominator //= buf
			buf = gcd(numerator, denominator)

		return IntegerFraction(numerator, denominator)

def main():
	pass

if __name__ == '__main__':
	main()