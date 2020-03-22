#Add Fractions
from math import gcd

#Least Common Multiple
def lcm(a, b):
	if type(a) is not int or type(b) is not int:
		raise Exception("Non-integer type.")

	return (a * b) // gcd(a, b)

#we want a list with fractions represented by tuples with no more than 2 members
def validate_add_fractions_arguments(fractions = None):
	if fractions is None:
		return True

	if type(fractions) is not list:
		raise Exception("Argument must be a list of 2 tuples.")

	for fraction in fractions:
		if type(fraction) is not tuple:
			raise Exception("Fractions must be represented by tuples.")

		if len(fraction) > 2:
			raise Exception("Too many members in fraction.")

		for member in fraction:
			if type(member) is not int:
				raise Exception("Non-integer fraction member.")

	return True

def add_fractions(fractions = None):
	

	validate_add_fractions_arguments(fractions)

	if fractions is None or fractions == list():
		return (0,)


	result = None

	for fraction in fractions:


		if len(fraction) == 0:
			continue
		elif len(fraction) == 1:
			numerator = fraction[0]
			denominator = 1
		else:
			numerator, denominator = fraction


		if denominator == 0:
			raise Exception("Zero division!")
		if numerator == 0:
			continue


		if (numerator < 0 and denominator < 0) or (numerator > 0 and denominator < 0):
			numerator *= -1
			denominator *= -1


		if result is None:
			result = [numerator, denominator]
		else:
			rnumerator, rdenominator = result

			while (rdenominator != denominator):
				buf = lcm(rdenominator, denominator)

				multiple = buf//rdenominator
				rdenominator *= multiple
				rnumerator *= multiple

				multiple = buf//denominator
				denominator *= multiple
				numerator *= multiple

			result = [rnumerator + numerator, rdenominator]


	if result is None:
		return (0,)
	else:
		return tuple(result)

def main():
	pass

if __name__ == '__main__':
	main()